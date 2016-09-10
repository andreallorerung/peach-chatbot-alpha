import pytest
from concerns.concern import Concern
import collections

# setup
distressScore = 42
concern = Concern(distressScore)

def test_init():
    assert concern is not None

def test_getDistressScore():
    assert distressScore == concern.getDistressScore()

def test_addressed():
    assert not concern.hasBeenAddressed()

    concern.setAddressed()
    assert concern.hasBeenAddressed()
