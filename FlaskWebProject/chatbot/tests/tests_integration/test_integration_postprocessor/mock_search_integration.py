import postprocess.search_adapter


class MockSearch(postprocess.search_adapter.SearchAdapter):
    def __init__(self):
        pass

    def search(self, keyword):
        if keyword is None or len(keyword) < 0:
            return None
        else:
            return "http://www.{}.com".format(keyword)
