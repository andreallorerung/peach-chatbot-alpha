import pytest
import collections
from rivescript import RiveScript
from concerns.drive_chat import ConversationDriver
from concerns.concern_factory import UserConcernsFactory
from messagelog.message import Message

currentuserid = "toby"
conversationDriver = ConversationDriver(currentuserid)

initialConcerns = [("respiratory", 5),
        ("urinary",  8),
        ("sleeping", 2),
        ("chores", 1),
        ("caring-responsibilities", 4),
        ("relative-friend", 7),
        ("faith", 9),
        ("meaning", 11),
        ("regret", 9),
        ("partner", 3)]

def test_hasuserid():
    attributeName = "userid"
    assert hasattr(conversationDriver, attributeName)

def test_setinitialconcerns():
    conversationDriver.setInitialUserConcerns(initialConcerns)

    assert theseUserConcernsHaveBeenStoredForTheUser(initialConcerns, currentuserid)

def theseUserConcernsHaveBeenStoredForTheUser(concerns, currentuserid):
    for concern in concerns:
        if not concernScoreHasBeenStoredForUser(concern, currentuserid):
            return False

    return True

def concernScoreHasBeenStoredForUser(concern, currentuserid):
        userConcers = UserConcernsFactory.getUserConcerns(currentuserid)
        concernName = concern[0]
        expectedConcernScore = concern[1]

        concern = userConcers[concernName]
        actualConcernScore = concern.getDistressScore()
        return ( expectedConcernScore == actualConcernScore )

def test_concernsHaveBeenSorted():
    sortedConcernScores = getConcernScoresByNames(currentuserid, conversationDriver.sortedUserConcernNames)

    expectedOrderedList = sorted(sortedConcernScores, reverse=True)
    assert expectedOrderedList == sortedConcernScores #asser that list is sorted in descending order

def getConcernScoresByNames(userid, namesOfConcerns):
    userConcerns = UserConcernsFactory.getUserConcerns(userid)
    concernScores = []

    for concernName in namesOfConcerns:
        concern = userConcerns[concernName]
        distressScore = concern.getDistressScore()

        concernScores.append(distressScore)

    return concernScores

def test_concernhasbeenaddressed():
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
    nextConcern = conversationDriver.getNextConcern()
    expected = "meaning"

    assert expected == nextConcern

def test_getNextConcern_middle():
    concernNames = ["meaning", "faith"]
    markManyConcerns(concernNames)

    nextConcern = conversationDriver.getNextConcern()
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
    nextConcern = conversationDriver.getNextConcern()
    assert nextConcern is None

def test_getNextConcern_concernsNamesListEmpty():
    conversationDriver.sortedUserConcernNames = None

    with pytest.raises(TypeError):
        nextConcern = conversationDriver.getNextConcern()
