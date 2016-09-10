'''Module to define a simple tokenizer'''
import nltk.tokenize.simple
import tokenizer


class SimpleTokenizerProxy(tokenizer.Tokenizer):
    '''Class to define a simple tokenizer, proxying the nltk package'''
    def __init__(self):
        self.simpleTokenizer = nltk.tokenize.simple.SpaceTokenizer()

    def tokenize(self, sentence):
        return self.simpleTokenizer.tokenize(sentence)
