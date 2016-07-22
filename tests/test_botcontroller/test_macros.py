import py.test
from botcontroller import macros

def test_setget():
    macros.set_issue("userid", "breathing", 7)

    assert 7 == macros.get_issue("userid", "breathing")
