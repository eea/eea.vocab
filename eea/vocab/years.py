""" Years vocabulary
"""
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

# Temporal coverage vocabulary
class DatasetYears(object):
    """ Dataset years vocabulary
    """
    implements(IVocabularyFactory)

    def __call__(self, context=None):
        terms = [SimpleTerm(str(key), str(key), str(key))
                 for key in reversed(range(1750, 2099))]
        return SimpleVocabulary(terms)
