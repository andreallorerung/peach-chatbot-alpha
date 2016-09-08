'''Module to provide an implementation of a preprocessor'''


class MessagePreprocessor(object):
    '''Class to implement the interface of a message processor'''
    def __init__(self, tokenizer, stopwordRemover, stemmer):
        '''To set appropriate objects to the properties of the preprocessor'''
        self.tokenizer = tokenizer
        self.stopwordRemover = stopwordRemover
        self.stemmer = stemmer

    def process(self, sentence):
        tokens = self._tokenize(sentence)
        tokens = self._removeStopwords(tokens)
        tokens = self._stem(tokens)

        processedSentence = self._join(tokens)
        return processedSentence

    def _stem(self, tokens):
        '''To return a stemmed set of tokens'''
        return [self.stemmer.stemWord(token) for token in tokens]

    def _removeStopwords(self, tokens):
        '''To return a set of tokens where stopwords have been removed'''
        return self.stopwordRemover.removeStopwords(tokens)

    def _tokenize(self, sentence):
        '''To split a sentence into tokens'''
        return self.tokenizer.tokenize(sentence)

    def _join(self, tokens):
        '''To join the split tokens back together'''
        return " ".join(tokens)
