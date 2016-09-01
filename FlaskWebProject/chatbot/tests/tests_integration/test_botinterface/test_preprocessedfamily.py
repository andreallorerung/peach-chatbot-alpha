from botinterface.bot_rivescript import BotRivescript
from botinterface.preprocessor import MessagePreprocessor
import bot_builder
from messagelog.message import Message

# set_up
bot = bot_builder.build()
USERID = "localuser"

def senddummymessage():
    content = "dummy"
    msg = Message(USERID, content)
    bot.reply(msg)

def setglobal():
    msg = Message(USERID, "set global")
    actual = bot.reply(msg)
    expected = "Topic set to global"

    assert expected == actual

def resetfamily():
    setglobal()
    msg = Message(USERID, "discuss family")
    reply = bot.reply(msg)
    assert "family" in reply

def test_enter_family_topic():
    setglobal()

    # perform:
    messages = ["discuss family", "discuss my family"
    "I wish to change the topic please and talk about family",
    "desire to discuss the family",
    "I want to talk about family issues"]

    for msg in messages:
        reply = bot.reply(Message(USERID, msg))
        # test:
        assert "talk about family" in reply

def test_enter_relativefriend():
    resetfamily()

    # perform:
    messages = ["discuss friend", "I think my mate ...", "aunt",
    "I like my aunt but I don't like my uncle",
    "my nephew hates me but my dad doesn't"
    "discuss relativefriend",]

    for msg in messages[:]:
        reply = bot.reply(Message(USERID, msg))
        # test:
        assert "What is it" in reply
        senddummymessage()
        resetfamily()

def test_issue_identified():
    resetfamily()

    # perform:
    messages = ["discuss friend", "I think my mate ...", "aunt",
    "I like my aunt but I don't like my uncle",
    "my nephew hates me but my dad doesn't",
    "my wife does not talk to me anymore"]

    replies = []
    for msg in messages[:]:
        nextreply = bot.reply(Message(USERID, msg))
        replies.append(nextreply)
        # reset to family topic
        senddummymessage()
        resetfamily()

    # test:
    assert "them" in replies[0]
    assert "them" in replies[1]
    assert "them" in replies[2]
    # Wrong answer: sets uservar "aunt" when it should be "uncle"
    assert "them" in replies[3]
    # Wrong answer: sets uservar "dad" when it should be nephew
    assert "them" in replies[4]
    assert "partner" in replies[5]

def test_description():
    # perform:
    messages = ["she doesn't like me anymore",
    "he has been very mean", "we used to be best friends but now ..."]

    for msg in messages[:]:
        senddummymessage()
        resetfamily()
        # problem with cousin
        m = "cousin"
        bot.reply(Message(USERID, m))

        reply = bot.reply(Message(USERID, msg))
        # test:
        assert "you would like to tell me" in reply

def test_yes():
    # perform:
    messages = ["yes",
    "yea","yeah" ]

    for msg in messages[:]:
        senddummymessage()
        resetfamily()

        # problem with cousin
        m = "cousin"
        reply = bot.reply(Message(USERID, m))

        m = "they are mean"
        reply = bot.reply(Message(USERID, m))
        # "would you like to tell me anything else about this?"
        reply = bot.reply(Message(USERID, msg))
        # test:
        assert "what is it" in reply.lower()

def test_yes_and():
    # perform:
    messages = ["the problem is also that ...",
    "yes there is something else",
    "yea there is this: ...", ]

    for msg in messages[:]:
        senddummymessage()
        resetfamily()
        # problem with cousin
        m = "cousin"
        reply = bot.reply(Message(USERID, m))
        print reply
        # problem with cousin
        m = "they are mean"
        reply = bot.reply(Message(USERID, m))
        print reply
        # "would you like to tell me anything else about this?"
        reply = bot.reply(Message(USERID, msg))
        # test:
        assert "I believe we have covered all the concerns" in reply
