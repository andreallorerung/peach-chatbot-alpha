'''Module to define the interface of a stemmer'''


class Stemmer(object):
    '''Interface a stemmer must implement'''
    def __init__(self):
        raise NotImplementedError("Stemmer is an interface")

    def stemWord(word):
        raise NotImplementedError("Stemmer is an interface")
