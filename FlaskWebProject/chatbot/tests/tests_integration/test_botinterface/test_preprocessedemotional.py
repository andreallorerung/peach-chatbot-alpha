from botinterface.bot_rivescript import BotRivescript
from botinterface.preprocessor import MessagePreprocessor
import botinterface.bot_builder
from messagelog.message import Message

# set_up
bot = botinterface.bot_builder.build()
USERID = "localuser"

def setglobal():
    # enter global topic:
    msg = Message(USERID, "set global")
    bot.reply(msg)

def setemotional():
    msg = Message(USERID, "discuss emotional")
    bot.reply(msg)

def resetToEmotional():
    setglobal()
    setemotional()

def test_enter_emotional():
    setglobal()

    messages = ["discuss emotional"]

    for msg in messages:
        reply = bot.reply(Message(USERID, msg))
        # test:
        assert "talk about emotional" in reply

def test_planning_interests():
    resetToEmotional()

    # perform:
    messages = ["I do not want to make plans anymore",
    "I used to work on my projects I don't anymore",
    "I do not enjoy sport", "I used to have hobbies"]

    for msg in messages[:]:
        reply = bot.reply(Message("localuser", msg))
        # test:
        found = False
        good_replies = ["Do you believe your loss of interest may be related to a loss of meaning or purpose?"]

        for good_reply in good_replies:
            if good_reply in reply:
                found = True
                break

        assert found, msg

def test_expressing():
    resetToEmotional()

    # perform:
    messages = ["I find difficulties voicing my state",
     "I never want to show how I feel",
     "conveying my emotions has always been difficult"]

    for msg in messages[:]:

        reply = bot.reply(Message(USERID, msg))
        # test:
        found = False
        good_replies = ["Do you feel you have problems expressing yourself in general or in particular situatons/with particular people?"]

        for good_reply in good_replies:
            if good_reply in reply:
                found = True
                break

        assert found, reply

def test_anger():
    resetToEmotional()

    # perform:
    messages = ["I throw tantrums for no reason",
    "I lose my temper more easily now",
    "I am disappointed with my parents behaviour"]

    for msg in messages[:]:

        reply = bot.reply(Message(USERID, msg))
        # test:
        found = False
        good_replies = ["What is it that frustrates you?"]

        for good_reply in good_replies:
            if good_reply in reply:
                found = True
                break

        assert found, reply

def test_guilt():
    resetToEmotional()

    # perform:
    messages = ["I feel guilty", "I had a lapse"]

    for msg in messages[:]:

        reply = bot.reply(Message(USERID, msg))
        # test:
        found = False
        good_replies = ["Does your guilt arises from something you take responsibility for?"]

        for good_reply in good_replies:
            if good_reply in reply:
                found = True
                break

        assert found, reply

def test_loneliness():
    resetToEmotional()

    # perform:
    messages = ["I am so lonely", "I feel alienated",
    "none of my friends are there for me"]

    for msg in messages[:]:

        reply = bot.reply(Message(USERID, msg))
        # test:
        found = False
        good_replies = ["Have you lost contact with friends and family?"]

        for good_reply in good_replies:
            if good_reply in reply:
                found = True
                break

        assert found, reply

def test_depression():
    resetToEmotional()

    # perform:
    messages = ["I never felt down for this long before",
    "it's like I'm permanently unhappy",
    "I believe I am depressed",
    "Absolutely hopeless",
    "No hope to continue living",
    "I have always been brave but I never faced a situation so discouraging",
    "unachievable"]

    for msg in messages[:]:

        reply = bot.reply(Message(USERID, msg))
        # test:
        found = False
        good_replies = ["Do you feel there is something other than your condition causing you to feel this way?"]

        for good_reply in good_replies:
            if good_reply in reply:
                found = True
                break

        assert found, reply

def test_worry():
    resetToEmotional()

    # perform:
    messages = ["I am afraid of what will happen next",
    "I am anxious for the future of those I will be leaving behind",
    "I suffer from anxiety and panic attacks"]

    for msg in messages[:]:

        reply = bot.reply(Message(USERID, msg))
        # test:
        found = False
        good_replies = ["Have you expressed these feelings to anyone before?"]

        for good_reply in good_replies:
            if good_reply in reply:
                found = True
                break

        assert found, reply
