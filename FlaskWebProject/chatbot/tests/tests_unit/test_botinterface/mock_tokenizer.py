import preprocess.tokenizer

class MockTokenizer(preprocess.tokenizer.Tokenizer):
    def __init__(self):
        pass

    def tokenize(self, sentence):
        return sentence.split()
