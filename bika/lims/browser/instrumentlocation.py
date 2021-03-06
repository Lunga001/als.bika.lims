# -*- coding: utf-8 -*-

from bika.lims.controlpanel.bika_instruments import InstrumentsView
from bika.lims import bikaMessageFactory as _


class InstrumentLocationInstrumentsView(InstrumentsView):

    def __init__(self, context, request):
        super(InstrumentLocationInstrumentsView, self).__init__(context, request)
        url = self.portal.absolute_url()
        url += "/bika_setup/bika_instruments/"
        self.context_actions = {_('Add'):
                                {'url': url + 'createObject?type_name=Instrument',
                                'icon': '++resource++bika.lims.images/add.png'}}

    def isItemAllowed(self, obj):
        location = obj.getInstrumentLocation() if obj else None
        return location.UID() == self.context.UID() if location else False
