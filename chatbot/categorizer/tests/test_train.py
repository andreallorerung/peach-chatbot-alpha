import pytest
import categorize.training
from textblob.classifiers import BaseClassifier
from utils.mock_classifier import data

def test_good():
    classifier = categorize.training.train(data)
    assert isinstance(classifier, BaseClassifier)
