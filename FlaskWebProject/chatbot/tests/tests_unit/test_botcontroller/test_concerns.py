import pytest
from botcontroller.concerns import Concerns, ConcernsFactory
import collections

def test_init():
    var = Concerns()# var = Concerns("id0")

    # assert "id0" == var["userid"]
    assert var is not None
    # with pytest.raises(KeyError):
        # var["get_something_that_isn't_there"]
    assert None is var["get_something_that_isn't_there"]

def test_setget():
    var = Concerns()

    var["something"] = 99
    assert 99 == var["something"]
