from nltk.stem.lancaster import LancasterStemmer
from stemming import Stemmer

class Lancaster(Stemmer):

    def __init__(self):
        self.stemmer = LancasterStemmer()

    def stemWord(self, word):
        return self.stemmer.stem(word)
