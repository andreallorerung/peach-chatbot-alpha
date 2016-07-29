from nltk.stem.lancaster import LancasterStemmer
from preprocess.stemming import Stemmer

class Lancaster(Stemmer):

    def __init__(self):
        self.stemmer = LancasterStemmer()

    def stem_word(self, word):
        return self.stemmer.stem(word)
