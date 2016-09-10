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

    expectedNextConcern = mockConversationDriver.getNextConcernName()
    assert concern == expectedNextConcern

    # rivescript.getNextConcern will fetch actual concern from the UserConcernsFactory
    _clearFactory()
    concern_factory.UserConcernsFactory._usersessions[userid] = mockConversationDriver

def _clearFactory():
    concern_factory.UserConcernsFactory._usersessions = dict()

def test_isDistressSignificantFor_yes():
    concern = "some distressful concern"
    _addMockToFactory(someuserid, concern)

    actualDecision = rivescriptmacros.isDistressSignificantFor(someuserid, concern)

    assert actualDecision

def test_isDistressSignificantFor_not():
    concern = "not a distressful concern"
    _addMockToFactory(someuserid, concern)

    actualDecision = rivescriptmacros.isDistressSignificantFor(someuserid, concern)

    assert not actualDecision

def test_isDistressSignificantFor_null_userid():
    concern = "doesn't matter"

    with pytest.raises(KeyError):
        actualDecision = rivescriptmacros.isDistressSignificantFor(None, concern)

def test_isDistressSignificantFor_null_concern():
    concern = "some concern"
    _addMockToFactory(someuserid, concern)

    with pytest.raises(KeyError):
        actualDecision = rivescriptmacros.isDistressSignificantFor(someuserid, None)
