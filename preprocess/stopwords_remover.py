'''Module to define stopword remover interface'''


class StopwordRemover(object):
    '''Abstract class to define the stopwords remover interface, provides base
    implementation of stopwords removal that subclasses may wish to override.
    Subclasses are expected to have a self.stopwords property defining the set
    of tokens to filter out.'''

    def __init__(self):
        raise NotImplementedError("StopwordRemover is an abstract class")

    def removeStopwords(self, tokens):
        '''To return a sentence without stopwords'''
        tokens_without_stopwords = self._excludeStopwords(tokens)

        return tokens_without_stopwords

    def _excludeStopwords(self, tokens):
        '''To return a filtered list of tokens'''
        tokens_without_stopwords = []

        for token in tokens:
            if not self._isStopword(token):
                tokens_without_stopwords.append(token)

        return tokens_without_stopwords

    def _isStopword(self, word):
        '''To decide whether a word is a stopword'''
        word = str(word).lower()
        if word in self.stopwords:
            return True
        else:
            return False
