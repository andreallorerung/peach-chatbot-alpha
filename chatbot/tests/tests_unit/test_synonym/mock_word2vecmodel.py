class MockWord2VecModel(object):

    def __init__(self):
        pass

    def intersect_word2vec_format(self, fname,
                                    binary=False,
                                    encoding='utf8',
                                    unicode_errors='strict'):
        pass

    def similar_by_word(self, word, topn=10, restrict_vocab=None):
        words = ["{}{}".format(word, n) for n in range(topn)]
        return words

def get_mock():

    return MockWord2VecModel()
