'''Module to define the interface to a search query keyword extractor from a
system reply'''


class KeywordExtractor(object):
    '''Interface a keyword extractor is expected to implement'''
    def __init__(self):
        raise NotImplementedError("KeywordExtractor is an interface")

    def parseSearchParameter(self, message):
        '''To extract a search parameter from the message argument'''
        raise NotImplementedError("KeywordExtractor is an interface")
