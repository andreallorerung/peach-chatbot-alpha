'''Module to define the way concrete synonym generators are instantiated'''
from gensim.models.word2vec import Word2Vec


class SynonymModelBuilder(object):
    '''To provide an appropriate synonym model'''

    _model

    @classmethod
    def buildW2CModel(cls):
        if _synonym_model:
            return _synonym_model
        else:
            _synonym_model =
            Word2VecSynonymModel(word2vecmodel=Word2Vec.load_word2vec_format(
                './synonym/.trainedWord2Vec/GoogleNews-vectors-negative300.bin',
                binary=True))
            return _synonym_model
