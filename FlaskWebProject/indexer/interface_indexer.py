class IndexerInterface(object):

    '''Indexer Interface'''

    def __init__(self):
        raise NotImplementedError("IndexerInterface is an interface")

    def build(self, urlToTextMap):
        raise NotImplementedError("IndexerInterface is an interface")
