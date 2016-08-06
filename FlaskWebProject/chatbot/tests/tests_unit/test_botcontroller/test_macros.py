from botcontroller import rivescriptmacros

def test_format_issue_list():
    rivescriptmacros.set_issue("userid", "respiratory", 5)
    rivescriptmacros.set_issue("userid", "urinary", 8)
    rivescriptmacros.set_issue("userid", "sleeping", 9)
    rivescriptmacros.set_issue("userid", "chores", 4)
    rivescriptmacros.set_issue("userid", "relative-friend", 10)

    issue_list = rivescriptmacros.get_all_issues("userid")
    formatted_issue_list = rivescriptmacros.format_issue_list(issue_list)

    assert "relative-friend: 10\nsleeping: 9\nurinary: 8\nrespiratory: 5\nchores: 4\n" == (formatted_issue_list)

def test_all_issues():
    rivescriptmacros.set_issue("userid", "respiratory", 5)
    rivescriptmacros.set_issue("userid", "urinary", 8)
    rivescriptmacros.set_issue("userid", "sleeping", 9)
    rivescriptmacros.set_issue("userid", "chores", 4)
    rivescriptmacros.set_issue("userid", "relative-friend", 10)

    issue_list = rivescriptmacros.get_all_issues("userid")

    assert ("relative-friend", 10) == issue_list[0]
    assert ("sleeping", 9)         == issue_list[1]
    assert ("urinary", 8)          == issue_list[2]
    assert ("respiratory", 5)      == issue_list[3]
    assert ("chores", 4)           == issue_list[4]

def test_setget():
    rivescriptmacros.set_issue("userid", "breathing", 7)

    assert 7 == rivescriptmacros.get_issue("userid", "breathing")
