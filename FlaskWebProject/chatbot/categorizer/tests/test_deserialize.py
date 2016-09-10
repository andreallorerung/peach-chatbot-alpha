import categorize.classifier_deserializer
from utils.mock_classifier import get_mock

def test_good():
    classifier = \
    categorize.classifier_deserializer.deserialize("tests/dump/serialized.pickle")

    # Label is a property of the nltk.classify.NaiveBayesClassifier class which
    # is not the same class textblob.classifiers.NaiveBayesClassifier.
    # Notice how the lookup for a labels() property does not fail, however, due
    # to the implementation of the latter as a subclass of an abstract class
    # exposing such a method.
    #
    # See: https://github.com/nltk/nltk/blob/develop/nltk/classify/naivebayes.py
    # , from line 43;
    # and https://github.com/sloria/TextBlob/blob/dev/textblob/classifiers.py ,
    # from line 274
    actual = classifier.labels()
    expected = get_mock().labels()

    assert expected == actual
