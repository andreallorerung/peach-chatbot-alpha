'''Module to define an stopwords remover that wraps around the standard nltk
stopwords remover'''
import nltk.corpus
import stopwords_remover


class StopwordRemoverNLTK(stopwords_remover.StopwordRemover):
    '''Class to define nltk stopwords remover'''
    def __init__(self):
        super(stopwords_remover.StopwordRemover)
        self.stopwords = nltk.corpus.stopwords.words("english")

    def removeStopwords(self, sentence):
        return self._removeStopwords(sentence)
