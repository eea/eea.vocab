""" Mime-types vocabulary
"""
import operator
from zope.interface import implements
from zope.component import queryUtility
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from Products.MimetypesRegistry.interfaces import IMimetypesRegistryTool
from eea.vocab.utils import compare

class MimeTypesVocabulary(object):
    """ Return vocabululary from mimetypes_registry
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        """ See IVocabularyFactory interface
        """
        mtr = queryUtility(IMimetypesRegistryTool)
        items = ((str(mime), mime.title_or_id() or str(mime))
                 for mime in mtr.mimetypes())
        items = sorted(items, key=operator.itemgetter(1), cmp=compare)

        return SimpleVocabulary([
            SimpleTerm(item[0], item[0], item[1]) for item in items])
