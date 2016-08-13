'''Module to provide an implementation of a preprocessor'''
import nltk.tokenize.simple
import message_processor
from preprocess import stemming_lancaster, stopwords_remover_lenient


class MessagePreprocessor(message_processor.MessageProcessor):
    '''Class to implement the interface of a message processor'''
    def __init__(self):
        '''To set appropriate objects to the properties of the preprocessor'''
        self.tokenizer = nltk.tokenize.simple.SpaceTokenizer()
        self.stopword_remover = stopwords_remover_lenient.\
                                StopwordRemoverLenient()
        self.stemmer = stemming_lancaster.Lancaster()

    def process(self, sentence):
        tokens = self._tokenize(sentence)
        tokens = self._remove_stopwords(tokens)
        tokens = self._stem(tokens)

        processed_sentence = self._join(tokens)
        return processed_sentence

    def _stem(self, tokens):
        '''To return a stemmed set of tokens'''
        return [self.stemmer.stem_word(token) for token in tokens]

    def _remove_stopwords(self, tokens):
        '''To return a set of tokens where stopwords have been removed'''
        return self.stopword_remover.removeStopwords(tokens)

    def _tokenize(self, sentence):
        '''To split a sentence into tokens'''
        return self.tokenizer.tokenize(sentence)

    def _join(self, tokens):
        '''To join the split tokens back together'''
        return " ".join(tokens)
