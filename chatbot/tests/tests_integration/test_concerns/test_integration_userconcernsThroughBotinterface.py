from botinterface.bot_rivescript import BotRivescript
import bot_builder
from concerns import concern_factory
from messagelog.message import Message


# set_up
bot = bot_builder.build()

USERID = "localuser"
mostDistressful = "urinary"
macrotopicForMostDistressful = "physical"
concernsForThisUser = {
    "urinary":  9,
    "mouth": 7
}

def setglobal():
    msg = Message(USERID, "set global")
    bot.reply(msg)

def resetphysical():
    setglobal()
    msg = Message(USERID, "discuss physical")
    reply = bot.reply(msg)
    assert "physical" in reply

def initializeConcerns():
    userConcerns = concern_factory.UserConcernsFactory.getUserConcerns(USERID)
    userConcerns.setInitialUserConcerns(concernsForThisUser)

def movedIntoPhysical():
    # mentioning expected issue (or any physical issue)
    message = "something breathing something"

    msg = Message(USERID, message)
    reply = bot.reply(msg)

    return "Does the problem present itself in particular conditions?" == reply

def skipTopicDiscussion():
    internalVariableNameForCountingMessagesReceivedOnTopic = "counter"
    numberOfMessagesReceivedOnTopic = 3 # pretending this has actually happened
    bot._interpreter._rivescriptInterpreter.set_uservar(USERID,
                        internalVariableNameForCountingMessagesReceivedOnTopic,
                        str(numberOfMessagesReceivedOnTopic))

def test_moveToNextTopic():
    resetphysical()
    initializeConcerns()
    skipTopicDiscussion()

    # perform:
    message = "bla bla bla"

    msg = Message(USERID, message)
    reply = bot.reply(msg)

    #test
    assert mostDistressful in reply
    assert macrotopicForMostDistressful in reply
    assert movedIntoPhysical()
    # print reply
    # assert False

def test_make_query():
    setglobal()
    initializeConcerns()
    bot.createUserSession(USERID)

    skipTopicDiscussion()

    # perform:
    message = "anything"

    msg = Message(USERID, message)
    reply = bot.reply(msg)

    assert mostDistressful == getCurrentMicroTopic()
    assert "Before we move on" in reply

    message = "yes"

    msg = Message(USERID, message)
    reply = bot.reply(msg)
    assert "find more information here" in reply

def test_make_query_no():
    setglobal()
    initializeConcerns()
    bot.createUserSession(USERID)

    skipTopicDiscussion()

    # perform:
    message = "anything"

    msg = Message(USERID, message)
    reply = bot.reply(msg)

    assert mostDistressful == getCurrentMicroTopic()
    assert "Before we move on" in reply

    message = "no"

    msg = Message(USERID, message)
    reply = bot.reply(msg)
    assert "next topic" in reply

def getCurrentMicroTopic():
    currentTopicInternalVariableName = "microtopic"
    return bot._interpreter._rivescriptInterpreter.get_uservar(USERID, currentTopicInternalVariableName)
