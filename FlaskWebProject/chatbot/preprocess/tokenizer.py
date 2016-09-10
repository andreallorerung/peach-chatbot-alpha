'''Module to define the interface of a tokenizer'''


class Tokenizer(object):
    '''Interface a tokenizer must conform to'''
    def __init__(self):
        raise NotImplementedError("Tokenizer is an interface")

    def tokenize(self, sentence):
        raise NotImplementedError("Tokenizer is an interface")
