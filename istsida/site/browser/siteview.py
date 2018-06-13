# -*- coding: utf-8 -*-

from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

class SiteView(BrowserView):
    
    def organism_vocabulary(self, name):
        factory = getUtility(IVocabularyFactory, name=name)
        regions = factory(self.context)
        return dict([(term.value,term.token) for term in regions])
    