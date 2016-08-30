import preprocess.stemming

class MockStemmer(preprocess.stemming.Stemmer):
    def __init__(self):
        pass

    def stemWord(self, word):
        return word[:-1]
