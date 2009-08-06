import doctest
import unittest
from eea.vocab.tests.base import VocabFunctionalTestCase
from Testing.ZopeTestCase import FunctionalDocFileSuite


OPTIONFLAGS = (
        doctest.REPORT_ONLY_FIRST_FAILURE |
        doctest.ELLIPSIS |
        doctest.NORMALIZE_WHITESPACE
)

def test_suite():
    return unittest.TestSuite((
            FunctionalDocFileSuite('README.txt',
                  optionflags=OPTIONFLAGS,
                  package='eea.vocab',
                  test_class=VocabFunctionalTestCase),
              ))


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
