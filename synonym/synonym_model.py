'''Module to define the objects that will extract synonyms for words'''


class SynonymModel(object):
    '''To define the interface a model of synonyms is expected to implement'''

    def __init__():
        raise NotImplementedError("SynonymModel is an interface")

    def get_synonyms(word, max_no_of_synonyms):
        '''To return synonyms for the specified word, up to max_no_of_synonyms
        '''
        raise NotImplementedError("SynonymModel is an interface")


class Word2VecSynonymModel(SynonymModel):
    '''To define a concrete model of synonyms that is built on top of the
    word2vec algorithm'''
    def __init__(self, word2vecmodel):
        '''To initialize a model of synonyms that has a word2vec model'''
        self.model = word2vecmodel

    def get_synonyms(self, word, max_no_of_synonyms=10):
        return self.model.similar_by_word(word, max_no_of_synonyms)
