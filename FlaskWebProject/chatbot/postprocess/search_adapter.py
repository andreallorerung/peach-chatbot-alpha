'''Module to define the interface to implement for an adapter to a search engine'''


class SearchAdapter(object):
    '''Interface a search engine adapter is expected to implement'''
    def __init__(self):
        raise NotImplementedError("SearchAdapter is an interface")

    def search(self, keyword):
        '''To perform a search query with the provided keyword'''
        raise NotImplementedError("SearchAdapter is an interface")
