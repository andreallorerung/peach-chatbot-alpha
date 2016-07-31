from preprocess.stemming_lancaster import Lancaster

class MessagePreprocessor(object):
    def __init__(self):
        pass

    def _stem(self, message):
        stemmer = Lancaster()
        tokens = self._tokenize(message)

        stemmed_tokens = [stemmer.stem_word(token) for token in tokens]
        stemmed_message = " ".join(stemmed_tokens)

        return stemmed_message

    def _tokenize(self, sentence):
        '''To split a sentence into tokens'''
        return str(sentence).split()
