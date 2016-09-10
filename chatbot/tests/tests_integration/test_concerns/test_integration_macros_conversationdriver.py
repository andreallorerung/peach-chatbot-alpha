import pytest
from concerns import rivescriptmacros
from concerns.concern_factory import UserConcernsFactory

userid = "Dan"
concernsFew = {
    "loneliness": 10,
    "urinary":  9,
    "depression": 2,
    "meaning": 8,
    "mouth": 7,
    "chores": 5
}
conversationDriver = UserConcernsFactory.getUserConcerns(userid)

def setUpLazily():
    nextConcern = conversationDriver.getNextConcernName()
    if nextConcern is None:
        conversationDriver.setInitialUserConcerns(concernsFew)

def test_getNextConcern():
    setUpLazily()

    expected = "loneliness"
    actual = rivescriptmacros.getNextConcern(userid)

    assert expected == actual

def test_getsecondconcernafterfirst():
    setUpLazily()
    conversationDriver._markAddressed("loneliness")

    expected = "urinary"
    actual = rivescriptmacros.getNextConcern(userid)

    assert expected == actual

def test_runoutofconcerns():
    setUpLazily()

    for concernName, distressScore in concernsFew.iteritems():
        conversationDriver._markAddressed(concernName)

    actual = rivescriptmacros.getNextConcern(userid)
    assert actual is None

def test_noConcernsSetUp():
    setUpLazily()
    conversationDriver.userConcerns = dict()
    conversationDriver.sortedUserConcernNames = []

    actual = rivescriptmacros.getNextConcern(userid)
    assert actual is None

def test_noConcernsStoredButNamesStored():
    setUpLazily()
    conversationDriver.userConcerns = dict()

    assert not conversationDriver.userConcerns
    with pytest.raises(KeyError):
        actual = rivescriptmacros.getNextConcern(userid)
    # make state consistent again to not affect following tests:
    conversationDriver.sortedUserConcernNames = []

def test_sortedListOfNamesIsEmptyButConcernsStored():
    setUpLazily()
    assert conversationDriver.sortedUserConcernNames
    conversationDriver.sortedUserConcernNames = []
    assert not conversationDriver.sortedUserConcernNames

    actual = rivescriptmacros.getNextConcern(userid)
    assert actual is None
