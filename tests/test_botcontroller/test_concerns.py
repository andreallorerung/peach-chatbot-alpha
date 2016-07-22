import pytest
from botcontroller.concerns import Concerns

def test_init():
    var = Concerns("id0")

    assert "id0" == var["userid"]
    # with pytest.raises(KeyError):
        # var["get_something_that_isn't_there"]
    assert None is var["get_something_that_isn't_there"]

def test_setget():
    var = Concerns("id0")

    var["something"] = 99
    assert 99 == var["something"]

def test_setget_excpt():
    var = Concerns("id0")

    with pytest.raises(ValueError):
        var["userid"] = "id98"
