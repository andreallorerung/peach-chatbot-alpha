import postprocess.search_adapter


class MockSearch(postprocess.search_adapter.SearchAdapter):
    def __init__(self):
        pass
        
    def search(self, keyword):
        return "http://www.{}.com".format(keyword)
