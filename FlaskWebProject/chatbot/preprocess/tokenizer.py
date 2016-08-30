
class Tokenizer(object):
    def __init__(self):
        raise NotImplementedError("Tokenizer is an interface")

    def tokenize(self, sentence):
        raise NotImplementedError("Tokenizer is an interface")
