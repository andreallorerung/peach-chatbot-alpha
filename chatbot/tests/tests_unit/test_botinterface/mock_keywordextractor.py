import postprocess.keyword_extractor


class MockKeywordextractor(postprocess.keyword_extractor.KeywordExtractor):

    def __init__(self):
        pass

    def parseSearchParameter(self, message):
        return "smoking"
