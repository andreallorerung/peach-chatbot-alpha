import pytest
from botcontroller.concerns import Concerns
from botcontroller.concerns import ConcernsFactory

def test_getitem():
    concern_for_id0 = ConcernsFactory.get("id0")

    assert concern_for_id0 is ConcernsFactory.get("id0")
