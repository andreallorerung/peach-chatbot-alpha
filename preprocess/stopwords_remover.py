'''Module to define stopword remover interface'''


class StopwordRemover(object):
    '''Abstract class to define the stopwords remover interface, provides base
    implementation of stopwords removal that subclasses may wish to override.
    Subclasses are expected to have a self.stopwords property defining the set
    of tokens to filter out.'''

    def __init__(self):
        raise NotImplementedError("StopwordRemover is an abstract class")

    def removeStopwords(self, input):
        '''To remove stopwords from the input parameter'''
        raise NotImplementedError("StopwordRemover is an abstract class")

    def _removeStopwords(self, sentence):
        '''To return a sentence without stopwords'''
        tokens = self._tokenize(sentence)
        tokens_without_stopwords = self._excludeStopwords(tokens)
        sentence_without_stopwords = " ".join(tokens_without_stopwords)

        return sentence_without_stopwords

    def _tokenize(self, sentence):
        '''To split a sentence into tokens'''
        return str(sentence).split()

    def _excludeStopwords(self, tokens):
        '''To return a filtered list of tokens'''
        tokens_without_stopwords = []

        for token in tokens:
            if not self._isStopword(token):
                tokens_without_stopwords.append(token)

        return tokens_without_stopwords

    def _isStopword(self, word):
        '''To decide whether a word is a stopword'''
        word = word.lower()
        if word in self.stopwords:
            return True
        else:
            return False
