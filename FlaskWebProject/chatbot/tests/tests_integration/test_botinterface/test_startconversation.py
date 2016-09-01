import bot_builder
from concerns import concern_factory

bot = bot_builder.build()

USERID = "boop"
mostDistressful = "respiratory"
concernsForThisUser = {mostDistressful: 10,
            "pain": 7}

def initializeConcerns():
    userConcerns = concern_factory.UserConcernsFactory.getUserConcerns(USERID)
    userConcerns.setInitialUserConcerns(concernsForThisUser)

def test_start():
    initializeConcerns()
    bot.createUserSession(USERID)
    assert getCurrentMacroTopic() is not None
    assert "undefined" != getCurrentMacroTopic()
    assert mostDistressful == getCurrentMicroTopic()

def getCurrentMicroTopic():
    currentTopicInternalVariableName = "microtopic"
    return bot._interpreter._rivescriptInterpreter.get_uservar(USERID, currentTopicInternalVariableName)

def getCurrentMacroTopic():
    currentTopicInternalVariableName = "macrotopic"
    return bot._interpreter._rivescriptInterpreter.get_uservar(USERID, currentTopicInternalVariableName)
