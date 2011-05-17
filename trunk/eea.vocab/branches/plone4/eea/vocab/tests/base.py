from Products.PloneTestCase import PloneTestCase
from Products.PloneTestCase.layer import onsetup
from Products.Five import zcml
from Products.Five import fiveconfigure


PRODUCTS = ['ATVocabularyManager', 'FiveSite', 'eea.vocab']

@onsetup
def setup_package():
    fiveconfigure.debug_mode = True
    import Products.Five
    import Products.FiveSite
    import eea.vocab
    zcml.load_config('meta.zcml', Products.Five)
    zcml.load_config('configure.zcml', Products.Five)
    zcml.load_config('configure.zcml', Products.FiveSite)
    zcml.load_config('configure.zcml', eea.vocab)
    fiveconfigure.debug_mode = False

    PloneTestCase.installProduct('Five')
    for i in PRODUCTS:
        PloneTestCase.installProduct(i)

setup_package()
PloneTestCase.setupPloneSite(products=PRODUCTS)


class VocabFunctionalTestCase(PloneTestCase.FunctionalTestCase):
    """ """
