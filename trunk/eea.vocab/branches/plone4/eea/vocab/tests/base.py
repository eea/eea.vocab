""" Tests setup
"""
from Products.PloneTestCase import PloneTestCase
from Products.PloneTestCase.layer import onsetup
from Products.Five import zcml
from Products.Five import fiveconfigure
import eea.vocab

PloneTestCase.installProduct('ATVocabularyManager')

@onsetup
def setup_package():
    """ Setup
    """
    fiveconfigure.debug_mode = True
    zcml.load_config('configure.zcml', eea.vocab)
    fiveconfigure.debug_mode = False

setup_package()
PloneTestCase.setupPloneSite(extension_profiles=('eea.vocab:default',))

class VocabFunctionalTestCase(PloneTestCase.FunctionalTestCase):
    """ Vocab Functional Test Case """
