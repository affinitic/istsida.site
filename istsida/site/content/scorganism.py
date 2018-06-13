# -*- coding: utf-8 -*-

from DateTime import DateTime

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

from istsida.site.interfaces import ISCOrganism
from istsida.site.config import PRODUCT_NAME

SCOrganismSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((
    atapi.StringField('url',
        required = False,
        searchable = True,
        validators = ('isURL',),
        widget = atapi.StringWidget(
                    label = "Site Web",
                    description="Entrer l'adresse du site web de l'organisme.",
                    size = 40)
    ),
    atapi.LinesField('focal',
        required = False,
        enforceVocabulary = True,
        vocabulary_factory = "istsida.vocabularies.points",
        widget = atapi.InAndOutWidget(
            label="Point focal",
            size = 5)
    ),
    atapi.ImageField('logo',
        required = False,
        original_size = (800,600),
        sizes = {
            'preview' : (400,400),
            'mini'    : (200, 200),
            'tile'    : (64,64),
        },
        widget = atapi.ImageWidget(label="Logo",)
    ),
    atapi.TextField('address',
        searchable = True,
        default_output_type = 'text/x-html-safe',
        widget = atapi.RichWidget(
                        label = "Coordonnées",
                        description = "Adresses, téléphones, e-mails,...",
                        rows = 5)
    ),
    atapi.TextField('contact',
        searchable = True,
        default_output_type = 'text/x-html-safe',
        widget = atapi.RichWidget(
                        label = "Contact(s)",
                        description = "Noms, téléphones et emails de la ou des personnes de contact.",
                        rows = 5)
    ),
    atapi.TextField('mission',
        searchable = True,
        default_output_type = 'text/x-html-safe',
        widget = atapi.RichWidget(
                        label = "Missions",
                        description = "Brêve description des missions et des activités.",
                        rows = 5)
    ),
    atapi.LinesField('activity',
        required = True,
        vocabulary_factory = "istsida.vocabularies.activities",
        widget = atapi.MultiSelectionWidget(
            label="Activités",
            format = 'checkbox')
    ),
    atapi.LinesField('types',
        required = True,
        vocabulary_factory = "istsida.vocabularies.types",
        widget = atapi.MultiSelectionWidget(
            label="Type d'organisme",
            format = 'checkbox')
    ),
    atapi.LinesField('region',
        required = True,
        vocabulary_factory = "istsida.vocabularies.regions",
        widget = atapi.InAndOutWidget(
            label="Couverture géographique",
            size = 5)
    ),
    atapi.LinesField('public',
        required = True,
        vocabulary_factory = "istsida.vocabularies.publics",
        widget = atapi.InAndOutWidget(
            label="Public(s) ciblé(s)",
            description="Choisir le ou les publics cibles.",
            size = 10)
    ),
    atapi.TextField('updateContact',
        required = False,
        widget = atapi.TextAreaWidget(
                label = "Contact pour la mise à jour",
                description="Nom et coordonnées d’un contact pour la mise à jour de la fiche descriptive.",
                size = 5)
    ),
    atapi.DateTimeField('updateDate',
        default_method=DateTime,
        widget = atapi.CalendarWidget(
                label="Date de mise à jour",
                show_hm=False)
    ),
))

SCOrganismSchema['title'].widget.label = "Nom de l'organisme"
SCOrganismSchema['description'].widget.visible = {'edit':'invisible', 'view':'invisible'}

class SCOrganism(base.ATCTContent):
    """Un organisme"""
    implements(ISCOrganism)

    meta_type = "SCOrganism"
    schema = SCOrganismSchema


atapi.registerType(SCOrganism, PRODUCT_NAME)
