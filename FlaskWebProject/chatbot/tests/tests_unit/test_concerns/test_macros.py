import pytest
import mock_conversationdriver
from concerns import rivescriptmacros
from concerns import concern_factory

someuserid = "macrosuserid"

def test_validateparameternumber_true():
    args = ["11", "twenty two"]

    expected = True
    actual = rivescriptmacros.validateParametersNumber(args, num=2)

    assert expected is actual

def test_validateparameternumber_false():
    args = ["eleven"]

    with pytest.raises(ValueError):
        rivescriptmacros.validateParametersNumber(args, num=3)

def test_validateparameternumber_nullargs():
    args = None

    with pytest.raises(ValueError):
        rivescriptmacros.validateParametersNumber(args)

def test_validateparameternumber_0num():
    args = ["twelve", "12"]

    expected = True
    actual = rivescriptmacros.validateParametersNumber(args, num=-1)
    assert expected is actual

def test_validateparameternumber_nullnum():
    args = ["Hello"]

    expected = True
    actual = rivescriptmacros.validateParametersNumber(args, num=None)
    assert expected is actual

def test_increase():
    args = ['11']
    value = args[0]

    result = rivescriptmacros.increase(value)

    assert '12' == result

def test_increase_notanumber():
    args = ['help']
    value = args[0]

    with pytest.raises(ValueError):
        result = rivescriptmacros.increase(value)

def test_increase_none():
    args = [None]
    value = args[0]

    with pytest.raises(TypeError):
        result = rivescriptmacros.increase(value)

def test_getNextConcern():
    expectedNextConcern = "meaning"
    _addMockToFactory(someuserid, expectedNextConcern)

    actualNextConcern = rivescriptmacros.getNextConcern(someuserid)
    assert expectedNextConcern == actualNextConcern

def test_getNextConcern_noconcerns():
    expectedNextConcern = None
    _addMockToFactory(someuserid, expectedNextConcern)

    actualNextConcern = rivescriptmacros.getNextConcern(someuserid)
    assert expectedNextConcern == actualNextConcern

def test_getNextConcern_noneuserid():
    noneUserid = None
    expectedNextConcern = "cats"
    _addMockToFactory(noneUserid, expectedNextConcern)

    actualNextConcern = rivescriptmacros.getNextConcern(noneUserid)
    assert expectedNextConcern == actualNextConcern

def _addMockToFactory(userid, concern):
    mockConversationDriver = \
        mock_conversationdriver.mockForUserWithConcern(someuserid, concern)

    expectedNextConcern = mockConversationDriver.getNextConcern()
    assert concern == expectedNextConcern

    # rivescript.getNextConcern will fetch actual concern from the UserConcernsFactory
    concern_factory.UserConcernsFactory._usersessions[userid] = mockConversationDriver


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
