import pytest
import mock_word2vecmodel
from synonym.synonym_extractor import SynonymExtractor
from synonym.synonym_word2vecextractor import Word2VecSynonymExtractor

def test_synonymmodel_interface():
    assert hasattr(SynonymExtractor, "extractSynonyms")

def test_Word2VecSynonymExtractor_dummy():
    model = Word2VecSynonymExtractor(word2vecmodel="dummy model")
    assert issubclass(type(model), SynonymExtractor)

def test_Word2VecSynonymExtractor_mocked():
    model = mock_word2vecmodel.get_mock()
    model = Word2VecSynonymExtractor(word2vecmodel=model)
    synonyms = model.extractSynonyms("dad")

    assert type(synonyms) is list
    for synonym in synonyms:
        assert type(synonym) is str

def test_Word2VecSynonymExtractor_mocked_withcondition():
    model = mock_word2vecmodel.get_mock()
    model = Word2VecSynonymExtractor(word2vecmodel=model)
    synonyms = model.extractSynonyms("dad", max_no_of_synonyms=100)

    assert type(synonyms) is list
    assert len(synonyms) == 100
    for synonym in synonyms:
        assert type(synonym) is str
