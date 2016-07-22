import py.test
from botcontroller import macros

def test_format_issue_list():
    macros.set_issue("userid", "respiratory", 5)
    macros.set_issue("userid", "urinary", 8)
    macros.set_issue("userid", "sleeping", 9)
    macros.set_issue("userid", "chores", 4)
    macros.set_issue("userid", "relative-friend", 10)

    issue_list = macros.get_all_issues("userid")
    formatted_issue_list = macros.format_issue_list(issue_list)

    assert "relative-friend: 10\nsleeping: 9\nurinary: 8\nrespiratory: 5\nchores: 4\n" == (formatted_issue_list)

def test_all_issues():
    macros.set_issue("userid", "respiratory", 5)
    macros.set_issue("userid", "urinary", 8)
    macros.set_issue("userid", "sleeping", 9)
    macros.set_issue("userid", "chores", 4)
    macros.set_issue("userid", "relative-friend", 10)

    issue_list = macros.get_all_issues("userid")

    assert ("relative-friend", 10) == issue_list[0]
    assert ("sleeping", 9)         == issue_list[1]
    assert ("urinary", 8)          == issue_list[2]
    assert ("respiratory", 5)      == issue_list[3]
    assert ("chores", 4)           == issue_list[4]

def test_setget():
    macros.set_issue("userid", "breathing", 7)

    assert 7 == macros.get_issue("userid", "breathing")
