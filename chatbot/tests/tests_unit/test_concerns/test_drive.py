import pytest
import collections
from rivescript import RiveScript
from concerns.drive_conversation import DistressConversationDriver
from concerns.concern_factory import UserConcernsFactory
from concerns.concern import Concern
from messagelog.message import Message


currentuserid = "toby"
initialConcerns = {"respiratory": 5,
        "urinary":  8,
        "sleeping": 2,
        "chores": 1,
        "caring-responsibilities": 4,
        "relative-friend": 7,
        "faith": 9,
        "meaning": 11,
        "regret": 9,
        "partner": 3}
conversationDriver = DistressConversationDriver(currentuserid)

def test_createconcernobjects():
    assert isdictofconcernobjects(conversationDriver._createConcernObjectsDict(initialConcerns))

def isdictofconcernobjects(candidate):
    assert type(candidate) is dict
    for key, value in candidate.iteritems():
        assert type(value) is Concern

        return True

def test_hasuserid():
    attributeName = "userid"
    assert hasattr(conversationDriver, attributeName)

def test_setinitialconcerns():
    conversationDriver.setInitialUserConcerns(initialConcerns)
    assert theseUserConcernsHaveBeenStoredForTheUser(initialConcerns, currentuserid)

def theseUserConcernsHaveBeenStoredForTheUser(concernsDict, currentuserid):
    for concernName, concernValue in concernsDict.iteritems():
        if not concernScoreHasBeenStoredForUser(concernName, concernValue, currentuserid):
            return False

    return True

def concernScoreHasBeenStoredForUser(concernName, expectedValue, currentuserid):
    storedConcern = conversationDriver.userConcerns[concernName]

    return expectedValue == storedConcern.getDistressScore()
        # userConcers = UserConcernsFactory.getUserConcerns(currentuserid)
        # concernName = concern[0]
        # expectedConcernScore = concern[1]
        #
        # concern = userConcers[concernName]
        # actualConcernScore = concern.getDistressScore()
        # return ( expectedConcernScore == actualConcernScore )

def test_concernsHaveBeenSorted():
    sortedConcernScores = getConcernScoresByNames(currentuserid, conversationDriver.sortedUserConcernNames)

    expectedOrderedList = sorted(sortedConcernScores, reverse=True)
    assert expectedOrderedList == sortedConcernScores #assert that list is sorted in descending order

def getConcernScoresByNames(userid, namesOfConcerns):
    concernScores = []

    for concernName in namesOfConcerns:
        distressScore = initialConcerns[concernName]

        concernScores.append(distressScore)

    return concernScores

def test_concernhasbeenaddressed():
    if len(conversationDriver.userConcerns) == 0:
        conversationDriver.setInitialUserConcerns(initialConcerns)

    concernName = "sleeping"
    conversationDriver._markAddressed(concernName)

    assert conversationDriver.concernHasBeenAddressed(concernName)

def test_concernhasbeenaddressed_noconcern():
    concernName = "yawning"

    with pytest.raises(KeyError):
        conversationDriver._markAddressed(concernName)

def test_not_concernhasbeenaddressedforuser():
    concernName = "respiratory"
    assert not conversationDriver.concernHasBeenAddressed(concernName)

def test_getNextConcern_initial():
    nextConcern = conversationDriver.getNextConcernName()
    expected = "meaning"

    assert expected == nextConcern

def test_getNextConcern_middle():
    concernNames = ["meaning", "faith"]
    markManyConcerns(concernNames)

    nextConcern = conversationDriver.getNextConcernName()
    expected = "regret"
    assert expected == nextConcern

def markManyConcerns(concernNames):
    for nextConcernName in concernNames:
        conversationDriver._markAddressed(nextConcernName)

def test_getNextConcern_noMoreConcerns():
    concernNames = ["respiratory","urinary","sleeping","chores",
    "caring-responsibilities","relative-friend","faith","meaning","regret",
    "partner"]

    markManyConcerns(concernNames)
    nextConcern = conversationDriver.getNextConcernName()
    assert nextConcern is None

def test_getNextConcern_concernsNamesListEmpty():
    conversationDriver.sortedUserConcernNames = None

    with pytest.raises(TypeError):
        nextConcern = conversationDriver.getNextConcernName()

def test_getConcernScore():
    concernName = "respiratory"

    concernScore = conversationDriver.getConcernScore(concernName)
    expectedScore = 5

    assert concernScore is not None
    assert expectedScore == concernScore

def test_getConcernScore_other():
    concernName = "faith"

    concernScore = conversationDriver.getConcernScore(concernName)
    expectedScore = 9

    assert concernScore is not None
    assert expectedScore == concernScore


def test_getConcernScore_no_such_concern():
    concernName = "gulliver-hurts"

    with pytest.raises(KeyError):
        concernScore = conversationDriver.getConcernScore(concernName)

def test_getConcernScore_null():
    concernName = None

    with pytest.raises(KeyError):
        concernScore = conversationDriver.getConcernScore(concernName)
