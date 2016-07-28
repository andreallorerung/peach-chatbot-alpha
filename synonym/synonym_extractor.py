'''Module to define the objects that will extract synonyms for words'''


class SynonymExtractor(object):
    '''To define the interface a extractor of synonyms is expected to implement
    '''

    def __init__():
        raise NotImplementedError("SynonymExtractor is an interface")

    def extractSynonyms(word, max_no_of_synonyms):
        '''To return synonyms for the specified word, up to max_no_of_synonyms
        '''
        raise NotImplementedError("SynonymExtractor is an interface")
