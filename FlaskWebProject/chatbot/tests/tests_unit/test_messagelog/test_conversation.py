from messagelog.conversation import Conversation
import mock_message

userid = "dan"
conversation = Conversation(userid)

def test_init():
    assert conversation is not None

def test_init_hasid():
    assert userid == conversation._userid

def test_init_hasmessages():
    assert conversation._messages is not None

def test_append():
    content = "hello"
    message = mock_message.MessageMock(userid, content)
    conversation.append(message)

    assert message in conversation._messages
