# -*- coding: utf-8 -*-

from Products.Archetypes import atapi
from Products.CMFCore import utils

from istsida.site import config

def initialize(context):

    import content
    
    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(config.PRODUCT_NAME),
        config.PRODUCT_NAME)

    for atype, constructor in zip(content_types, constructors):
        utils.ContentInit('%s: %s' % (config.PRODUCT_NAME, atype.portal_type),
            content_types      = (atype,),
            permission         = config.ADD_PERMISSIONS[atype.portal_type],
            extra_constructors = (constructor,),
            ).initialize(context)
