import pytest
from messagelog.conversation import Conversation
from messagelog.message import Message

userid = "mac"
conversation = Conversation(userid)

def test_appendmessage():
    content = "I am well"
    message = Message(userid, content)
    conversation.append(message)

    assert message in conversation._messages
