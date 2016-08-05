from botinterface.bot_rivescript import BotRivescript
from botinterface.preprocessor import MessagePreprocessor
from botinterface.message import Message

# set_up
bot = BotRivescript(preprocessor = MessagePreprocessor())
USERID = "localuser"

def setglobal():
    # enter global topic:
    msg = Message(USERID, "set global")
    bot.reply(msg)

def test_setglobal():
    # enter global topic:
    msg = Message(USERID, "set global")
    actual = bot.reply(msg)
    expected = "Topic set to global"

    assert expected == actual

def test_change_topic():
    setglobal()

    # perform:
    messages = ["desire discuss other",
    "desire to change topic",
    "I want to change the topic",
    "I wish to change the topic please",
    "I want to talk about something else"]

    for msg in messages[:]:
        reply = bot.reply(Message(USERID, msg))
        # test:
        assert "would you like to" in reply, msg

def test_not_change_topic():
    setglobal()

    # perform:
    messages = ["do not desire to change topic", "I no want to change the topic",
    "I will nay wish to change the topic please"]

    for msg in messages:
        reply = bot.reply(Message(USERID, msg))

        # test:
        assert "the topic then" in reply, msg

def test_discuss():
    setglobal()

    # perform:
    messages = ["discuss physical", "want talk emotional",
    "wish discuss spiritual",
    "I wish to discuss my spiritual",
    "I wish to discuss my spiritual concerns please"]

    for msg in messages:
        reply = bot.reply(Message(USERID, msg))

        # test:
        assert "talk about" in reply, msg
        setglobal() #set back to global for next message

def test_change_topic_and():
    setglobal()

    # perform:
    messages = ["do desire to change topic and discuss physical",
    "I want to change the topic and talk emotional problems",
    "I really want change the topic please and speak about family"]

    for msg in messages:
        reply = bot.reply(Message(USERID, msg))

        # test:
        assert "'s talk about" in reply, msg
        setglobal()
