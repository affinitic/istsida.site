# -*- coding: utf-8 -*-

from zope.interface import implements
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from zope.app.schema.vocabulary import IVocabularyFactory

ACTIVITIES = [
    ('accompagnement-projets', "Accompagnement de projets"),
    ('accompagnement-psycho-social', "Accompagnement psycho-social"),
    ('ateliers', "Activités/ateliers conviviaux avec le(s) public(s) cible(s)"),
    ('animations', "Animations/séances d’information avec le(s) public(s) cible(s)"),
    ('centre-documentation', "Centre de documentation"),
    ('depistage', "Dépistage"),
    ('etablir-guidelines', "Etablir un consensus / des recommandations / guidelines"),
    ('groupes-reflexion', "Groupes de parole/réflexion/self-help avec le(s) public(s) cible(s)"),
    ('lobbying', "Lobbying politique/institutionnel/commercial"),
    ('preservatif-lubrifiant', "Mise à disposition / distribution de préservatifs et lubrifiant"),
    ('diffusion-outils-prevention', "Mise à disposition et diffusion d’outils de prévention / d’information / pédagogiques pour le(s) public(s) cible(s)"),
    ('materiel-reduction-risques', "Mise à disposition et diffusion de matériel de réduction des risques"),    
    ('organisation-evenement', "Organisation d’événement (expo, conférence, concert…)"),
    ('concertation-professionnel', "Organiser la concertation entre professionnels"),
    ('traitement', "Prise en charge médicale / traitement"),
    ('production-outils', "Production d’outils adaptés pour les professionnels"),
    ('production-outils-prevention', "Production d’outils de prévention adaptés pour le(s) public(s) cible(s)"),
    ('projets-prevention', "Projets de prévention par les pairs / relais communautaires"),
    ('recueil-donnees', "Recherche et recueil de données"),
    ('information-professionnel', "Séances d’information/ de formation pour professionnels"),
    ('travail-proximite', "Travail de proximité (rue, internet, festivals, milieux de vie, communauté)"),
    ('vaccination', "Vaccination"),
]

REGIONS = {
    'be': "Belgique",
    'fl': "Communauté flamande",
    'fr': "Communauté française",
    'br': "Bruxelles",
    'bw': "Province du Brabant Wallon",
    'ha': "Province du Hainaut",
    'li': "Province de Liège",
    'lu': "Province du Luxembourg",
    'na': "Province de Namur",
}

POINTS = {
    'population': "Population générale",
    'enfant': "Enfants et jeunes",
    'migrant': "Personnes migrantes",
    'hsffsf': "HSH et FSF",
    'drogue': "Usagers de drogues injecteurs",
    'enceinte': "Femmes enceintes",
    'prostituee': "Prostituées féminines",
    'prostitue': "Prostitués masculins",
    'detenu': "Personnes détenues",
    'festif': "Public festif",
}

PUBLICS = {
    'population': "Population générale",
    'enfant': "Enfants et jeunes",
    'seropositif': "Personnes séropositives",
    'migrant': "Personnes migrantes",
    'hsh': "Hommes qui ont des rapports sexuels avec des hommes (HSH)",
    'fsf': "Femmes qui ont des rapports sexuels avec des femmes (FSF)",
    'enceinte': "Femmes enceintes et les femmes séropositives ayant récemment accouché",
    'drogue': "Usagers de drogues injecteurs (UDI)",
    'prostituee': "Prostituées féminines",
    'prostitue': "Prostitués masculins",
    'detenu': "Personnes détenues",
    'fetard': "Public festif",
    'professionel': "Professionnels",
}

TYPES = {
    'communautaire': "Service communautaire de promotion de la santé",
    'prevention': "Organisme de prévention",
    'universitaire': "Service scientifique et universitaire",
    'familial': "Planning familial",
    'administration': "Administration",
    'international': "Organisme étranger ou international",
    'local': "Centre local de promotion de la santé",
    'accompagnement': "Organisme d'accompagnement et de prise en charge",
    'point': "Point focal",
}

class ActivitiesVocabulary(object):
    """
    Activities
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        items = [SimpleTerm(key, item) for key, item in ACTIVITIES]
        return SimpleVocabulary(items)

ActivitiesVocabularyFactory = ActivitiesVocabulary()

class RegionsVocabulary(object):
    """
    Regions
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        items = [SimpleTerm(key, item) for key, item in REGIONS.items()]
        return SimpleVocabulary(items)

RegionsVocabularyFactory = RegionsVocabulary()

class PointsVocabulary(object):
    """
    Focal Points
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        items = [SimpleTerm(key, item) for key, item in POINTS.items()]
        return SimpleVocabulary(items)

PointsVocabularyFactory = PointsVocabulary()
          
class PublicsVocabulary(object):
    """
    Publics
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        items = [SimpleTerm(key, item) for key, item in PUBLICS.items()]
        return SimpleVocabulary(items)

PublicsVocabularyFactory = PublicsVocabulary()
        
class TypesVocabulary(object):
    """
    Types
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        items = [SimpleTerm(key, item) for key, item in TYPES.items()]
        return SimpleVocabulary(items)

TypesVocabularyFactory = TypesVocabulary()
