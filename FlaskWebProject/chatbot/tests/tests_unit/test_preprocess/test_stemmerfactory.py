from preprocess import stemmer_factory

def test_factory():
    stemmer = stemmer_factory.get_stemmer()

    assert hasattr(stemmer, "stem")
