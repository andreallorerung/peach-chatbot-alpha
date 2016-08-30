import preprocess.stopwords_remover

class MockSingleStopwordRemover(preprocess.stopwords_remover.StopwordRemover):
    def __init__(self, word):
        super(preprocess.stopwords_remover.StopwordRemover)
        self.stopwords = [word]
