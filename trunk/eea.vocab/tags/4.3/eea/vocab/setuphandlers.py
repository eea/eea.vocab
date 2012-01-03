""" Setup various
"""
from eea.vocab.atvocabs import vocabs
import logging

logger = logging.getLogger('eea.vocab.setuphandlers')

def setupATVocabularies(portal):
    """ Installs all AT-based Vocabularies
    """
    if portal.readDataFile('eea.vocab.txt') is None:
        return

    vkeys = vocabs.keys()
    atvm = portal.getSite().portal_vocabularies

    for vkey in vkeys:
        if vkey in atvm.objectIds():
            logger.info("Skipped adding %s vocabulary, already exists" % vkey)
            continue

        logger.info("Adding vocabulary %s" % vkey)

        atvm.invokeFactory('SimpleVocabulary', vkey)
        vocab = atvm[vkey]
        for (ikey, value) in vocabs[vkey]:
            vocab.invokeFactory('SimpleVocabularyTerm', ikey)
            vocab[ikey].setTitle(value)
