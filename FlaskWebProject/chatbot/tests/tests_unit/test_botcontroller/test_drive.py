import collections
from rivescript import RiveScript
from botcontroller.drive_chat import ConversationDriver
from botcontroller.concerns import ConcernsFactory
from botinterface.message import Message

conversationDriver = ConversationDriver(RiveScript())
someuserid = "toby"
def test_hasrivescript():
    assert hasattr(conversationDriver, "rivescriptInterpreter")

def test_rivescriptInterpreterIsRivescript():
    assert RiveScript is type(conversationDriver.rivescriptInterpreter)

def test_reply():
    message = "Hello"

    replied = conversationDriver.reply(message)

    assert replied is not None

def test_setissuesforuser():
    issues = [("respiratory", 5),
            ("urinary",  8),
            ("sleeping", 2),
            ("chores", 1),
            ("caring-responsibilities", 4),
            ("relative-friend", 7),
            ("faith", 9),
            ("meaning", 11),
            ("regret", 9),
            ("partner", 3)]

    someuserid = "toby"

    conversationDriver.setIssuesForUser(someuserid, issues)

    assert theseConcernsHaveBeenStoredForTheUser(issues, someuserid)

def theseConcernsHaveBeenStoredForTheUser(issues, userid):
    for issue in issues:
        if not issueScoreHasBeenStoredForUser(issue, userid):
            return False

    return True

def issueScoreHasBeenStoredForUser(issue, userid):
        userConcers = ConcernsFactory.getConcerns(userid)
        issueName = issue[0]
        issueScore = issue[1]
        return userConcers[issueName] == issueScore
