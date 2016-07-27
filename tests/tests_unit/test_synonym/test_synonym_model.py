import pytest
import mock_word2vecmodel
from synonym.synonym_model import *

def test_synonymmodel():
    assert hasattr(SynonymModel, "get_synonyms")

def test_Word2VecSynonymModel():
    model = Word2VecSynonymModel(word2vecmodel="dummy model")

    assert issubclass(type(model), SynonymModel)

def test_Word2VecSynonymModel_mocked():
    model = mock_word2vecmodel.get_mock()
    model = Word2VecSynonymModel(word2vecmodel=model)
    synonyms = model.get_synonyms("dad")

    assert type(synonyms) is list
    for synonym in synonyms:
        assert type(synonym) is str

def test_Word2VecSynonymModel_mocked_withcondition():
    model = mock_word2vecmodel.get_mock()
    model = Word2VecSynonymModel(word2vecmodel=model)
    synonyms = model.get_synonyms("dad", 100)

    assert type(synonyms) is list
    assert len(synonyms) == 100
    for synonym in synonyms:
        assert type(synonym) is str
