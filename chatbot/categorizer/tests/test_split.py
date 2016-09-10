import pprint
import categorize.dataset_splitting
from utils.mock_classifier import data

def test_split_shuffle():
    train_set, dev_set, test_set = categorize.dataset_splitting.split(data, \
                                                                shuffle = True)
    print "\n\nTrain set:"
    pprint.pprint(train_set)
    print "\n\nDev set:"
    pprint.pprint(dev_set)
    print "\n\nTest set:"
    pprint.pprint(test_set)

    assert train_set
    assert dev_set
    assert test_set

    for pair in train_set:
        assert pair not in dev_set
        assert pair not in test_set

    for pair in dev_set:
        assert pair not in train_set
        assert pair not in test_set

    for pair in test_set:
        assert pair not in train_set
        assert pair not in dev_set

def test_split_nodev():
    train_set, dev_set, test_set = \
    categorize.dataset_splitting.split(data, devsizepercent=0.0)

    assert train_set
    assert not dev_set
    assert test_set

def test_split_onlytrain():
    train_set, dev_set, test_set = \
    categorize.dataset_splitting.split(data, devsizepercent=0.0, \
                                             testsizepercent=0.0)

    assert train_set
    assert not dev_set
    assert not test_set

def test_split_noshuffle():
    train_set, dev_set, test_set = categorize.dataset_splitting.split(data, \
                                                                shuffle = False)

    assert train_set == data[2:]
