from synonym.synonym_model_factory import SynonymModelFactory
from mock_word2vecmodel import MockWord2VecModel

def test_returnifinitialized():
    SynonymModelFactory._synonym_model = MockWord2VecModel()

    model = SynonymModelFactory.getModel()

    assert type(model) is MockWord2VecModel
