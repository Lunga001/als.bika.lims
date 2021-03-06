# This file is part of Bika LIMS
#
# Copyright 2011-2016 by it's authors.
# Some rights reserved. See LICENSE.txt, AUTHORS.txt.

from bika.lims import bikaMessageFactory as _
from bika.lims.browser.bika_listing import BikaListingView
from bika.lims.browser.referencesample import ReferenceSamplesView
from bika.lims.controlpanel.bika_instruments import InstrumentsView


class SupplierInstrumentsView(InstrumentsView):
    def __init__(self, context, request):
        InstrumentsView.__init__(self, context, request)
        self.context = context
        self.request = request

    def isItemAllowed(self, obj):
        supp = obj.getRawSupplier() if obj else None
        return supp.UID() == self.context.UID() if supp else False


class SupplierReferenceSamplesView(ReferenceSamplesView):
    def __init__(self, context, request):
        ReferenceSamplesView.__init__(self, context, request)
        self.context = context
        self.request = request
        self.contentFilter['path']['query'] = '/'.join(
            context.getPhysicalPath())
        self.context_actions = {
            _('Add'): {'url': 'createObject?type_name=ReferenceSample',
                       'icon': '++resource++bika.lims.images/add.png'}}
        # Remove the Supplier column from the list
        del self.columns['Supplier']
        for rs in self.review_states:
            rs['columns'] = [col for col in rs['columns'] if col != 'Supplier']
        if 'disable_border' in self.request.other:
            del (self.request.other['disable_border'])


class ContactsView(BikaListingView):
    def __init__(self, context, request):
        BikaListingView.__init__(self, context, request)
        self.context = context
        self.request = request
        self.catalog = "portal_catalog"
        self.contentFilter = {
            'portal_type': 'SupplierContact',
            'path': {"query": "/".join(context.getPhysicalPath()),
                     "level": 0}
        }
        self.context_actions = {
            _('Add'): {
                'url': 'createObject?type_name=SupplierContact',
                'icon': '++resource++bika.lims.images/add.png'}
        }
        self.show_table_only = False
        self.show_sort_column = False
        self.show_select_row = False
        self.show_select_column = True
        self.pagesize = 50
        self.icon = self.portal_url + \
                    "/++resource++bika.lims.images/contact_big.png"
        self.title = self.context.translate(_("Contacts"))

        self.columns = {
            'getFullname': {
                'title': _('Full Name'),
                'replace_url': 'absolute_url'
            },
            'getEmailAddress': {'title': _('Email Address')},
            'getBusinessPhone': {'title': _('Business Phone')},
            'getMobilePhone': {'title': _('Mobile Phone')},
            'getFax': {'title': _('Fax')},
        }

        self.review_states = [
            {'id': 'default',
             'title': _('All'),
             'contentFilter': {},
             'columns': ['getFullname',
                         'getEmailAddress',
                         'getBusinessPhone',
                         'getMobilePhone',
                         'getFax']},
        ]

