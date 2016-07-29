import nltk.corpus

class StopwordRemover(object):
    def removeStopwords(input):
        raise NotImplementedError("StopwordRemover is an interface")

class StopwordRemoverNLTK(StopwordRemover):
    def __init__(self):
        self.stopwords = nltk.corpus.stopwords.words("english")

    def removeStopwords(self, sentence):
        tokens = self._tokenize(sentence)
        print "tokens for sentence:{}".format(tokens)
        for token in tokens:
            print "processing token:'{}'".format(token)
            if self._isStopword(token):
                tokens.remove(token) # I think modifying the list while iterating is causing issues

        sentence_without_stopwords = " ".join(tokens)

        return sentence_without_stopwords

    def _tokenize(self, sentence):
        return sentence.split()

    def _isStopword(self, word):
        if word in self.stopwords:
            return True
        else:
            return False
