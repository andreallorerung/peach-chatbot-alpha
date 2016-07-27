'''Module to define the way concrete synonym generators are instantiated'''
from gensim.models.word2vec import Word2Vec
from synonym_extractor import Word2VecSynonymExtractor


class SynonymExtractorFactory(object):
    '''To provide an appropriate synonym extractor'''

    _synonym_extractor = None

    @classmethod
    def getExtractor(cls):
        if cls._synonym_extractor:
            return cls._synonym_extractor
        else:
            cls._synonym_extractor = \
            Word2VecSynonymExtractor(word2vecmodel=Word2Vec.load_word2vec_format(
                './synonym/.trainedWord2Vec/GoogleNews-vectors-negative300.bin',
                binary=True))
            return cls._synonym_extractor
