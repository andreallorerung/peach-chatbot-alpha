class ExtractorInterface(object):

    ''' Extractor Interface'''

    def __init__(self):
        raise NotImplementedError("ExtractorInterface is an interface")

    def extract(self, urlList):
        raise NotImplementedError("ExtractorInterface is an interface")
