import messagelog.conversation_logging
import botinterface.bot_rivescript
import messagelog.message
import bot_builder

mockbrain = "tests/tests_integration/test_messagelog/mockbrain.rive"
builder = bot_builder.BotBuilder()
builder.addPreprocessor(None)
builder.addPostprocessor(None)
builder.addBrain(mockbrain)
bot = builder.build()
# bot = botinterface.bot_rivescript.BotRivescript(brain=mockbrain)
ConversationLogger = messagelog.conversation_logging.ConversationLogger

userid = "bob"
usermessage = messagelog.message.Message(userid, "Hello this is bob")
expectedreply = "Hello bob this is system"

def _sendUserMessageAndLog(userid, message):
    ConversationLogger.logUserMessage(message)
    reply = bot.reply(message)
    assert reply is not None
    ConversationLogger.logSystemReplyForUser(reply, userid)
    return reply

systemreply = _sendUserMessageAndLog(userid, usermessage)

def test_usermessagelogged():
    conversation = _getConversationForUser(userid)
    assert usermessage in conversation._messages

def test_systemreplied():
    assert expectedreply == systemreply

def test_systemreplylogged():
    conversation = _getConversationForUser(userid)
    assert _replyIsInConversation(systemreply, conversation)

def _replyIsInConversation(reply, conversation):
    for message in conversation._messages:
        if reply == message.getContent():
            return True

    return False

def _getConversationForUser(userid):
    return ConversationLogger._conversations[userid]

def test_sendManyMessages():
    manyMessagesUserid = "tom"

    messages = [
    messagelog.message.Message(manyMessagesUserid, "Hello"),
    messagelog.message.Message(manyMessagesUserid, "I am fine and you?"),
    messagelog.message.Message(manyMessagesUserid, "I want to talk about the weather")
    ]

    for message in messages:
        _sendUserMessageAndLog(manyMessagesUserid, message)

    expectedConversation = [
    messagelog.message.Message(manyMessagesUserid, "Hello"),
    messagelog.message.Message("system", "Hello, how are you?"),
    messagelog.message.Message(manyMessagesUserid, "I am fine and you?"),
    messagelog.message.Message("system", "I feel overworked and (ironically) cannot wait to start my new job in september, what would you like to talk about?"),
    messagelog.message.Message(manyMessagesUserid, "I want to talk about the weather"),
    messagelog.message.Message("system", "Leaves are already falling, it feels like autumn already")
    ]

    loggedConversation =  _getConversationForUser(manyMessagesUserid)
    loggedMessages = loggedConversation._messages

    for expectedMessage, actualMessage in zip(expectedConversation, loggedMessages):
        assert expectedMessage.getContent() == actualMessage.getContent()
        assert expectedMessage.getUserid() == actualMessage.getUserid()
