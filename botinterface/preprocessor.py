import nltk.tokenize.simple
from preprocess import stemming_lancaster


class MessagePreprocessor(object):
    def __init__(self):
        self.stemmer = stemming_lancaster.Lancaster()
        self.tokenizer = nltk.tokenize.simple.SpaceTokenizer()

    def _stem(self, tokens):
        stemmed_tokens = [self.stemmer.stem_word(token) for token in tokens]

        return stemmed_tokens

    # def _remove_stopwords(self, )

    def _tokenize(self, sentence):
        '''To split a sentence into tokens'''
        return self.tokenizer.tokenize(sentence)

    def _join(self, tokens):
        '''To join the split tokens back together'''
        return " ".join(tokens)
