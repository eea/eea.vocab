def setupATVocabularies(portal):
    """ Installs all AT-based Vocabularies """
    
    from eea.vocab.atvocabs import vocabs
    
    vkeys = vocabs.keys()
    atvm = portal.getSite().portal_vocabularies
    
    for vkey in vkeys:

        print "adding vocabulary %s" % vkey
        
        if hasattr(atvm, vkey):
            continue
        
        atvm.invokeFactory('SimpleVocabulary', vkey)
        vocab = atvm[vkey]
        for (ikey, value) in vocabs[vkey]:
            vocab.invokeFactory('SimpleVocabularyTerm', ikey)
            vocab[ikey].setTitle(value)
