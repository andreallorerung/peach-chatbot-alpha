import pytest
import collections
from rivescript import RiveScript
from botcontroller.drive_chat import ConversationDriver
from botcontroller.concerns import UserConcernsFactory
from botinterface.message import Message

currentuserid = "toby"
conversationDriver = ConversationDriver(currentuserid)

def test_hasuserid():
    attributeName = "userid"
    assert hasattr(conversationDriver, attributeName)

# def test_reply():
#     message = "Hello"
#
#     replied = conversationDriver.reply(message)
#
#     assert replied is not None

def test_setinitialconcerns():
    concerns = [("respiratory", 5),
            ("urinary",  8),
            ("sleeping", 2),
            ("chores", 1),
            ("caring-responsibilities", 4),
            ("relative-friend", 7),
            ("faith", 9),
            ("meaning", 11),
            ("regret", 9),
            ("partner", 3)]

    currentuserid = "toby"

    conversationDriver.setInitialUserConcerns(concerns)

    assert theseUserConcernsHaveBeenStoredForTheUser(concerns, currentuserid)

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
