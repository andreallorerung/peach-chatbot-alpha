from synonym.synonym_extractor_factory import SynonymExtractorFactory
from mock_word2vecmodel import MockWord2VecModel

def test_returnifinitialized():
    assert SynonymExtractorFactory._synonym_extractor is None
    SynonymExtractorFactory._synonym_extractor = MockWord2VecModel()

    extractor = SynonymExtractorFactory.getExtractor()

    assert type(extractor) is MockWord2VecModel
