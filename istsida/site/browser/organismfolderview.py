# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

class OrganismFolderViewView(BrowserView):
    
    def organism_brains(self, activity='', public='', region='', title='', type_=''):
        strip_title = title.strip()
        if strip_title:
            strip_title = strip_title + '*'
        pc = getToolByName(self.context, 'portal_catalog')
        brains = pc.searchResults(portal_type='SCOrganism',
                        sc_index_activities=activity,
                        sc_index_publics=public,
                        sc_index_regions=region,
                        sc_index_types=type_,
                        Title=strip_title,
                        path='/'.join(self.context.getPhysicalPath()),
                        sort_on='sortable_title')
        return brains
        
