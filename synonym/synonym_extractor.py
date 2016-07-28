'''Module to define the objects that will extract synonyms for words'''


class SynonymExtractor(object):
    '''To define the interface a extractor of synonyms is expected to implement'''

    def __init__():
        raise NotImplementedError("SynonymExtractor is an interface")

    def extractSynonyms(word, max_no_of_synonyms):
        '''To return synonyms for the specified word, up to max_no_of_synonyms
        '''
        raise NotImplementedError("SynonymExtractor is an interface")


class Word2VecSynonymExtractor(SynonymExtractor):
    '''To define a concrete extractor of synonyms that is built on top of the
    word2vec algorithm'''
    def __init__(self, word2vecmodel):
        '''To initialize an extractor of synonyms that has a word2vec model'''
        self.model = word2vecmodel

    def extractSynonyms(self, word, max_no_of_synonyms=10):
        return self.model.similar_by_word(word, max_no_of_synonyms)
