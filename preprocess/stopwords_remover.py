import nltk.corpus

class StopwordRemover(object):
    def __init__(self):
        raise NotImplementedError("StopwordRemover is an abstract class")

    def removeStopwords(self, input):
        raise NotImplementedError("StopwordRemover is an abstract class")

    def _tokenize(self, sentence):
        return sentence.split()

    def _excludeStopwords(self, tokens):
        tokens_without_stopwords = []

        for token in tokens:
            if not self._isStopword(token):
                tokens_without_stopwords.append(token)

        return tokens_without_stopwords

    def _isStopword(self, word):
        word = word.lower()
        if word in self.stopwords:
            return True
        else:
            return False

class StopwordRemoverNLTK(StopwordRemover):
    def __init__(self):
        super(StopwordRemoverNLTK)
        self.stopwords = nltk.corpus.stopwords.words("english")

    def removeStopwords(self, sentence):
        tokens = self._tokenize(sentence)

        tokens_without_stopwords = self._excludeStopwords(tokens)

        sentence_without_stopwords = " ".join(tokens_without_stopwords)

        return sentence_without_stopwords
