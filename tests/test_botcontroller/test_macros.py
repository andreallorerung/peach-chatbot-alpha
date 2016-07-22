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

    assert (formatted_issue_list[0]) == "relative-friend: 10"
    assert (formatted_issue_list[1]) == "sleeping: 9"
    assert (formatted_issue_list[2]) == "urinary: 8"
    assert (formatted_issue_list[3]) == "respiratory: 5"
    assert (formatted_issue_list[4]) == "chores: 4"

def test_all_issues():
    macros.set_issue("userid", "respiratory", 5)
    macros.set_issue("userid", "urinary", 8)
    macros.set_issue("userid", "sleeping", 9)
    macros.set_issue("userid", "chores", 4)
    macros.set_issue("userid", "relative-friend", 10)

    issue_list = macros.get_all_issues("userid")

    assert issue_list[0] == ("relative-friend", 10)
    assert issue_list[1] == ("sleeping", 9)
    assert issue_list[2] == ("urinary", 8)
    assert issue_list[3] == ("respiratory", 5)
    assert issue_list[4] == ("chores", 4)

def test_setget():
    macros.set_issue("userid", "breathing", 7)

    assert 7 == macros.get_issue("userid", "breathing")
