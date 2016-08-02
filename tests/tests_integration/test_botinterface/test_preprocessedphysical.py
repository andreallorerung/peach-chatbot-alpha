from botinterface.bot_rivescript import BotRivescript
from botinterface.preprocessor import MessagePreprocessor
from botinterface.message import Message

# set_up
bot = BotRivescript(preprocessor = MessagePreprocessor())
USERID = "localuser"

def setglobal():
    msg = Message(USERID, "set global")
    bot.reply(msg)

def resetphysical():
    setglobal()
    msg = Message(USERID, "discuss physical")
    reply = bot.reply(msg)
    assert "physical" in reply

def test_problem_questions():
    resetphysical()

    # perform:
    messages = ["my breathing problem ...", "It affects ...", "There's also ...",
    "Ok", "this test message should fail the test"]

    for msg in messages[:1]:
        reply = bot.reply(Message(USERID, msg))
        # test:
        assert "problem" in reply
