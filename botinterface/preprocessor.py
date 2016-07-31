import nltk.tokenize.simple
from preprocess import stemming_lancaster, stopwords_remover_lenient


class MessagePreprocessor(object):
    def __init__(self):
        self.tokenizer = nltk.tokenize.simple.SpaceTokenizer()
        self.stopword_remover = stopwords_remover_lenient.\
                                StopwordRemoverLenient()
        self.stemmer = stemming_lancaster.Lancaster()

    def preprocess(self, sentence):
        tokens = self._tokenize(sentence)
        tokens = self._remove_stopwords(tokens)
        tokens = self._stem(tokens)

        processed_sentence = self._join(tokens)
        return processed_sentence

    def _stem(self, tokens):
        return [self.stemmer.stem_word(token) for token in tokens]

    def _remove_stopwords(self, tokens):
        return self.stopword_remover.removeStopwords(tokens)

    def _tokenize(self, sentence):
        '''To split a sentence into tokens'''
        return self.tokenizer.tokenize(sentence)

    def _join(self, tokens):
        '''To join the split tokens back together'''
        return " ".join(tokens)
