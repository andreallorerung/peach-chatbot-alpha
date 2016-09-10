from messagelog.conversation_logging import ConversationLogger
import mock_message

userid = "jak"

def test_init():
    assert hasattr(ConversationLogger, "logUserMessage")

def test_logusermessage():
    message = mock_message.MessageMock(userid, "wow")
    ConversationLogger.logUserMessage(message)

    assert _thatConversationForUserContains(message)

def _thatConversationForUserContains(message):
    userid = message.getUserid()
    conversation = ConversationLogger._conversations[userid]

    return (message in conversation._messages)

def test_logsystemreplyforuser():
    replyContent = "system can talk"

    ConversationLogger.logSystemReplyForUser(replyContent, userid)

    assert _thatConversationForUserContainsReply(userid, replyContent)

def _thatConversationForUserContainsReply(userid, replyContent):
    conversation = ConversationLogger._conversations[userid]

    return _conversationContainsMessageWithContent(conversation, replyContent)

def _conversationContainsMessageWithContent(conversation, messageContent):
    for message in conversation._messages:
        if messageContent == message.getContent():
            return True

    return False
