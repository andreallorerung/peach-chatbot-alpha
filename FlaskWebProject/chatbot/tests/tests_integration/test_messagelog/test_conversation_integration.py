import pytest
from messagelog.conversation import Conversation
from botinterface.message import Message

userid = "mac"
conversation = Conversation(userid)

def test_appendmessage():
    content = "I am well"
    message = Message(userid, content)
    conversation.append(message)

    assert message in conversation._messages

def test_appendmessage_wronguserid():
    wrongid = "frank"
    content = "I am not well"

    message = Message(wrongid, content)

    with pytest.raises(KeyError):
        conversation.append(message)
