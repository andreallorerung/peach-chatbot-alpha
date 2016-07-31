import nltk.tokenize.simple
from preprocess.stemming_lancaster import Lancaster


class MessagePreprocessor(object):
    def __init__(self):
        self.stemmer = Lancaster()
        self.tokenizer = nltk.tokenize.simple.SpaceTokenizer()

    def _stem(self, message):
        tokens = self._tokenize(message)

        stemmed_tokens = [self.stemmer.stem_word(token) for token in tokens]
        stemmed_message = " ".join(stemmed_tokens)

        return stemmed_message

    def _tokenize(self, sentence):
        '''To split a sentence into tokens'''
        return self.tokenizer.tokenize(sentence)
