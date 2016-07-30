import nltk.corpus


class StopwordRemover(object):
    def __init__(self):
        raise NotImplementedError("StopwordRemover is an abstract class")

    def removeStopwords(self, input):
        raise NotImplementedError("StopwordRemover is an abstract class")

    def _removeStopwords(self, sentence):
        tokens = self._tokenize(sentence)
        tokens_without_stopwords = self._excludeStopwords(tokens)
        sentence_without_stopwords = " ".join(tokens_without_stopwords)

        return sentence_without_stopwords

    def _tokenize(self, sentence):
        return str(sentence).split()

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
        super(StopwordRemover)
        self.stopwords = nltk.corpus.stopwords.words("english")

    def removeStopwords(self, sentence):
        return self._removeStopwords(sentence)

class StopwordRemoverLenient(StopwordRemover):
    def __init__(self):
        super(StopwordRemover)
        self.stopwords = set(['do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and',
        'but', 'if', 'or', 'as', 'of', 'at', 'by', 'for', 'with', 'about',
        'against', 'between', 'into', 'through', 'above', 'below', 'to', 'from',
        'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'such', 'too',
        'very', 's', 'can', 'will', 'just'])

    def removeStopwords(self, sentence):
        return self._removeStopwords(sentence)
