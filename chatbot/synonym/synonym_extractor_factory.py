'''Module to define the way concrete synonym generators are instantiated'''
from gensim.models.word2vec import Word2Vec
from synonym_word2vecextractor import Word2VecSynonymExtractor

MODELLOCATION = './synonym/trainedWord2Vec/GoogleNews-vectors-negative300.bin'


class SynonymExtractorFactory(object):
    '''To provide an appropriate synonym extractor'''

    _synonym_extractor = None

    @classmethod
    def getExtractor(cls):
        '''To provide an appropriate synonym extractor object'''
        if cls._synonym_extractor:
            return cls._synonym_extractor
        else:
            cls._synonym_extractor = SynonymExtractorFactory._initializeInstance(MODELLOCATION)
            return cls._synonym_extractor

    @staticmethod
    def _initializeInstance(modelLocation):
        '''To initialize the synonym extractor instance (singleton)'''
        trainedModel = Word2Vec.load_word2vec_format(modelLocation, binary=True)
        return Word2VecSynonymExtractor(word2vecmodel=trainedModel)
