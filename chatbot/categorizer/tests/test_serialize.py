import categorize.classifier_serializer
from utils.mock_classifier import get_mock
from textblob.classifiers import NaiveBayesClassifier

def test_good():
    classifier = get_mock()
    categorize.classifier_serializer.serialize(classifier, "tests/dump/serialized.pickle")

    # assert file has content
    import os
    assert os.stat("tests/dump/serialized.pickle").st_size != 0
