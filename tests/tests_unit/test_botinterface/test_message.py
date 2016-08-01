from botinterface.message import Message

message = Message("user01", "Hello")

def test_init():

    assert "user01" == message.userid
    assert "Hello" == message.content

def test_getuserid():

    expected = "user01"
    actual = message.getUserid()

    assert expected == actual

def test_getcontent():

    expected = "Hello"
    actual = message.getContent()

    assert expected == actual
