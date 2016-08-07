from messagelog.conversation_logging import ConversationLogger
import mock_message

def test_init():
    assert hasattr(ConversationLogger, "logUserMessage")

def test_logusermessage():
    message = mock_message.MessageMock("username","wow")
    ConversationLogger.logUserMessage(message)

    assert thatConversationForUserContains(message)

def thatConversationForUserContains(message):
    userid = message.getUserid()
    conversation = ConversationLogger._conversations[userid]

    return (message in conversation._messages)
