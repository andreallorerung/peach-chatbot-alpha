'''Module to define a concrete implementation of a synonym extractor based on
the word2vec algorithm'''
from synonym_extractor import SynonymExtractor


class Word2VecSynonymExtractor(SynonymExtractor):
    '''To define a concrete extractor of synonyms that is built on top of the
    word2vec algorithm'''
    def __init__(self, word2vecmodel):
        '''To initialize an extractor of synonyms that has a word2vec model'''
        self.model = word2vecmodel

    def extractSynonyms(self, word, max_no_of_synonyms=10):
        vectors = self.model.similar_by_word(word, max_no_of_synonyms)
        similarWords = self._extractWords(vectors)
        return similarWords

    def _extractWords(self, vectors):
        '''Extracts the words from the vectors'''
        similarWords = []

        for vector in vectors:
            # first element of couple is the word, second is cosin distance
            # between the vector representing the word queried for within the
            # model and the next closest vector to this in the model, e.g.:
            # >>> model.similar_by_word("hopeless")
            #[(u'utterly_hopeless', 0.5964581370353699),
            # (u'forlorn', 0.5776818990707397),
            # (u'hopelessly', 0.5626010298728943),
            # (u'miserable', 0.5604095458984375),
            # (u'pathetic', 0.5594014525413513),
            # (u'pitiful', 0.5581729412078857),
            # (u'helpless', 0.5568423271179199),
            # (u'seemingly_hopeless', 0.5478963851928711),
            # (u'bleak', 0.547258198261261),
            # (u'futile', 0.5467945337295532)]
            word = vector[0]
            word = self._normalize(word)
            similarWords.append(word)

        return similarWords

    def _normalize(self, word):
        '''To replace '_' with ' '.
        The word2vec model also stores sequences of multiple words, or words
        broken by a return carriage as '_'-separated words. For example, it
        stores pairs such as "seemingly_hopeless" in this way, and words broken
        by a return carriage character appear as "educa_tion"'''

        return word.replace('_', ' ')
