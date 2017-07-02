# This file is part of Bika LIMS
#
# Copyright 2011-2017 by it's authors.
# Some rights reserved. See LICENSE.txt, AUTHORS.txt.
from Acquisition import aq_inner
from Acquisition import aq_parent

from bika.lims import logger
from bika.lims.upgrade import upgradestep
from bika.lims.upgrade.utils import UpgradeUtils

product = 'bika.lims'
version = '3.2.0.170630'


@upgradestep(product, version)
def upgrade(tool):
    portal = aq_parent(aq_inner(tool))
    ut = UpgradeUtils(portal)
    ufrom = ut.getInstalledVersion(product)
    if ut.isOlderVersion(product, version):
        logger.info('Skipping upgrade of {0}: {1} > {2}'.format(
            product, ufrom, version))
        # The currently installed version is more recent than the target
        # version of this upgradestep
        return True

    logger.info('Upgrading {0}: {1} -> {2}'.format(product, ufrom, version))

    setup = portal.portal_setup

    # Added a 'skins' layer to als.lims for overriding bika.lims resources
    setup.runImportStepFromProfile('profile-als.lims:default', 'skins')

    # Refresh affected catalogs
    ut.refreshCatalogs()

    logger.info("{0} upgraded to version {1}".format(product, version))
    return True
