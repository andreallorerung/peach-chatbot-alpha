import messagelog.conversation_logging
import botinterface.bot_rivescript
import botinterface.message

mockbrain = "tests/tests_integration/test_messagelog/mockbrain.rive"
bot = botinterface.bot_rivescript.BotRivescript(brain=mockbrain)
ConversationLogger = messagelog.conversation_logging.ConversationLogger

userid = "bob"
usermessage = botinterface.message.Message(userid, "Hello this is bob")
expectedreply = "Hello bob this is system"

def sendUserMessage():
    ConversationLogger.logUserMessage(usermessage)
    systemreply = bot.reply(usermessage)
    assert systemreply is not None
    return systemreply

systemreply = sendUserMessage()

def test_usermessagelogged():
    conversation = ConversationLogger._conversations[userid]
    assert usermessage in conversation._messages

def test_systemreplied():
    assert expectedreply == systemreply
