import nltk.tokenize.simple
import tokenizer


class SimpleTokenizerProxy(tokenizer.Tokenizer):
    def __init__(self):
        self.simpleTokenizer = nltk.tokenize.simple.SpaceTokenizer()

    def tokenize(self, sentence):
        return self.simpleTokenizer.tokenize(sentence)
