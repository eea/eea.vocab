=========
eea.vocab
=========

eea.vocab provides vocabularies commonly used through the EEA Site. It
was designed to be small and light so that other products using one of these
vocabularies wouldn't have to depend on other heavy weight products or
copy/paste code. #2584

eea.vocab provides a GenericSetup profile and is easily installed via the
quickinstaller tool. There's a couple of vocabularies that gets installed:

  >>> from Products.CMFCore.utils import getToolByName
  >>> from Products.ATVocabularyManager.config import TOOL_NAME as ATVOCABULARYTOOL
  >>> atvm = getToolByName(portal, ATVOCABULARYTOOL, None)
  >>> hasattr(atvm, 'themes')
  True
  >>> hasattr(atvm, 'countries')
  True
