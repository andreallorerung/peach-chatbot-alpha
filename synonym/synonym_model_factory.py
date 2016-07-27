'''Module to define the way concrete synonym generators are instantiated'''
from gensim.models.word2vec import Word2Vec
from synonym_model import Word2VecSynonymModel


class SynonymModelFactory(object):
    '''To provide an appropriate synonym model'''

    _synonym_model = None

    @classmethod
    def getModel(cls):
        if cls._synonym_model:
            return cls._synonym_model
        else:
            cls._synonym_model = \
            Word2VecSynonymModel(word2vecmodel=Word2Vec.load_word2vec_format(
                './synonym/.trainedWord2Vec/GoogleNews-vectors-negative300.bin',
                binary=True))
            return cls._synonym_model
