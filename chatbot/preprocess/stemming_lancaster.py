'''Module to define a stemmer using the Lancaster algorithm'''
from nltk.stem.lancaster import LancasterStemmer
from stemming import Stemmer

class Lancaster(Stemmer):
    '''Class to define a stemmer using the Lancaster algorithm'''
    def __init__(self):
        self.stemmer = LancasterStemmer()

    def stemWord(self, word):
        return self.stemmer.stem(word)
