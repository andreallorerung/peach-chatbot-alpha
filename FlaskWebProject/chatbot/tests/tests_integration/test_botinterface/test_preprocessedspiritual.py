from botinterface.bot_rivescript import BotRivescript
from botinterface.preprocessor import MessagePreprocessor
from messagelog.message import Message

# set_up
bot = BotRivescript(preprocessor = MessagePreprocessor())
USERID = "localuser"

def setglobal():
    msg = Message(USERID, "set global")
    bot.reply(msg)

def resetspiritual():
    setglobal()
    msg = Message(USERID, "discuss spiritual")
    reply = bot.reply(msg)
    assert "spiritual" in reply

def test_faith():
    resetspiritual()

    # perform:
    messages = ["I have lost belief",
    "I have lost faith",
    "I stopped going to church"]

    for msg in messages[:]:

        reply = bot.reply(Message(USERID, msg))
        # test:
        found = False
        good_replies = ["Have you spoken to anyone in your spiritual community about this?"]

        for good_reply in good_replies:
            if good_reply in reply:
                found = True
                break

        assert found, reply

def test_meaning():
    resetspiritual()

    # perform:
    messages = [
    "I don't think I value my life",
    "what is the purpose of it all?",
    "I don't believe there is any meaning to life"]

    for msg in messages[:]:

        reply = bot.reply(Message(USERID, msg))
        # test:
        found = False
        good_replies = ["Do you feel this lack of meaning is due to not having or being able to pursue goals or objectives in your life?"]

        for good_reply in good_replies:
            if good_reply in reply:
                found = True
                break

        assert found, reply

def test_regret():
    resetspiritual()

    # perform:
    messages = [
    "I have lived a life of immorality",
    "I have have been evil and regret it",
    "I worry for my conscience",
    "I wish I could go back and ...",
    "I wish to make formal apologies",
    "I believe I have been immoral"]

    for msg in messages[:]:

        reply = bot.reply(Message(USERID, msg))
        # test:
        found = False
        good_replies = ["Do you believe there is any way for you to make up for your mistakes?"]

        for good_reply in good_replies:
            if good_reply in reply:
                found = True
                break

        assert found, reply
