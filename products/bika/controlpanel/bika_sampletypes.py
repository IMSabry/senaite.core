from AccessControl import ClassSecurityInfo
from Products.ATContentTypes.content import schemata
from Products.Archetypes import atapi
from Products.Archetypes.ArchetypeTool import registerType
from Products.CMFCore import permissions
from Products.Five.browser import BrowserView
from Products.bika.browser.bika_listing import BikaListingView
from Products.bika.config import PROJECTNAME
from Products.bika import bikaMessageFactory as _
from Products.bika.content.bikaschema import BikaFolderSchema
from plone.app.content.browser.interfaces import IFolderContentsView
from plone.app.folder.folder import ATFolder, ATFolderSchema
from Products.bika.interfaces.controlpanel import ISampleTypes
from zope.interface.declarations import implements

class SampleTypesView(BikaListingView):
    implements(IFolderContentsView)
    contentFilter = {'portal_type': 'SampleType'}
    content_add_buttons = {_('Sample Type'): "createObject?type_name=SampleType"}
    title = _("Sample Types")
    description = ""
    show_editable_border = False
    show_table_only = False
    show_sort_column = False
    show_select_row = True
    show_select_column = False
    batch = True
    pagesize = 20

    columns = {
               'title_or_id': {'title': _('Title'), 'icon':'sampletype.png'},
               'SampleTypeDescription': {'title': _('Description')},
              }
    review_states = [
                    {'title_or_id': _('All'), 'id':'all',
                     'columns': ['title_or_id', 'SampleTypeDescription'],
                     'buttons':[{'cssclass': 'context',
                                 'title': _('Delete'),
                                 'url': 'folder_delete:method'}]},
                    ]

    def folderitems(self):
        items = BikaListingView.folderitems(self)
        for x in range(len(items)):
            if not items[x].has_key('brain'): continue
            obj = items[x]['brain'].getObject()
            items[x]['SampleTypeDescription'] = obj.SampleTypeDescription()
            items[x]['links'] = {'title_or_id': items[x]['url'] + "/edit"}

        return items

schema = ATFolderSchema.copy()
class SampleTypes(ATFolder):
    implements(ISampleTypes)
    schema = schema
    displayContentsTab = False
schemata.finalizeATCTSchema(schema, folderish = True, moveDiscussion = False)
atapi.registerType(SampleTypes, PROJECTNAME)
