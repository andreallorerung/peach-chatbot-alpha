from botinterface.bot_rivescript import BotRivescript
from botinterface.preprocessor import MessagePreprocessor
import bot_builder
from messagelog.message import Message

# set_up
bot = bot_builder.build()
USERID = "localuser"

def setglobal():
    msg = Message(USERID, "set global")
    bot.reply(msg)

def resetphysical():
    setglobal()
    msg = Message(USERID, "discuss physical")
    reply = bot.reply(msg)
    assert "physical" in reply

def test_intro_reply():
    resetphysical()

    message = "my breathing problem ..."
    msg = Message(USERID, message)
    reply = bot.reply(msg)

    print "User message:'{}'".format(message)
    print "Bot reply:'{}'".format(reply)

    assert "Does the problem present itself in particular conditions?" == reply

def test_problem_questions():
    resetphysical()

    message = "my breathing problem ..."
    msg = Message(USERID, message)
    reply = bot.reply(msg)

    print "User message:'{}'".format(message)
    print "Bot reply:'{}'".format(reply)

    # perform:
    messages = ["It affects ...", "There's also ...",
    "Ok", "this test message should fail the test"]

    for message in messages[:3]:
        msg = Message(USERID, message)
        reply = bot.reply(msg)
        print "User message:'{}'".format(message)
        print "Bot reply:'{}'".format(reply)
        print "counter variable value:{}".format(bot._interpreter._rivescriptInterpreter.get_uservar(USERID, "counter"))
        # test:
        assert "severe" in reply or "often" in reply or "affecting" in reply

    msg = Message(USERID, messages[3])
    reply = bot.reply(msg)
    print "User message:'{}'".format(message)
    print "Bot reply:'{}'".format(reply)
    assert "I believe we have covered all the concerns" in reply
