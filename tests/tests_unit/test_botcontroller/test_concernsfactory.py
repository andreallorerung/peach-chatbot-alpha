import pytest
from botcontroller.concerns import Concerns
from botcontroller.concerns import ConcernsFactory

def test_getitem():
    concern_for_id0 = ConcernsFactory.getConcerns("id0")

    assert concern_for_id0 is ConcernsFactory.getConcerns("id0")
