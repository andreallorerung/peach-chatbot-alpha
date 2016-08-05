'''Module to define an interface for a message processor'''


class MessagePreprocessorInterface(object):
    '''Interface a message preprocessor is expected to implement'''
    def __init__(self):
        raise NotImplementedError("MessagePreprocessorInterface is an interface")

    def process(self, sentence):
        '''To preprocess the sentence'''
        raise NotImplementedError("MessagePreprocessorInterface is an interface")
