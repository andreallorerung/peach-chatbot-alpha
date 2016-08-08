from botcontroller import rivescriptmacros

someuserid = "macrosuserid"

# def test_format_issue_list():
#     rivescriptmacros.setIssue(someuserid, "respiratory", 5)
#     rivescriptmacros.setIssue(someuserid, "urinary", 8)
#     rivescriptmacros.setIssue(someuserid, "sleeping", 9)
#     rivescriptmacros.setIssue(someuserid, "chores", 4)
#     rivescriptmacros.setIssue(someuserid, "relative-friend", 10)
#
#     issue_list = rivescriptmacros.get_all_issues(someuserid)
#     formatted_issue_list = rivescriptmacros.format_issue_list(issue_list)
#
#     assert "relative-friend: 10\nsleeping: 9\nurinary: 8\nrespiratory: 5\nchores: 4\n" == (formatted_issue_list)
#
# def test_all_issues():
#     rivescriptmacros.setIssue(someuserid, "respiratory", 5)
#     rivescriptmacros.setIssue(someuserid, "urinary", 8)
#     rivescriptmacros.setIssue(someuserid, "sleeping", 9)
#     rivescriptmacros.setIssue(someuserid, "chores", 4)
#     rivescriptmacros.setIssue(someuserid, "relative-friend", 10)
#
#     issue_list = rivescriptmacros.get_all_issues(someuserid)
#
#     assert ("relative-friend", 10) == issue_list[0]
#     assert ("sleeping", 9)         == issue_list[1]
#     assert ("urinary", 8)          == issue_list[2]
#     assert ("respiratory", 5)      == issue_list[3]
#     assert ("chores", 4)           == issue_list[4]
#
# def test_setget():
#     rivescriptmacros.setIssue(someuserid, "breathing", 7)
#
#     assert 7 == rivescriptmacros.get_issue(someuserid, "breathing")
