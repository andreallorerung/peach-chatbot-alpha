import rivescript
from botinterface.bot_rivescript import BotRivescript
from messagelog.message import Message
import mock_messageprocessor, mock_interpreter

bot = BotRivescript()

def test_init():

    assert bot is not None

def test_hasreply():

    assert hasattr(bot, "reply")

def test_hasbot():

    assert hasattr(bot, "_interpreter")
    # assert type(bot.interpreter) is rivescript.RiveScript

def test_haspreprocessor():

    assert hasattr(bot, "_preprocessor")

def test_haspostprocessor():

    assert hasattr(bot, "_postprocessor")

def test_init_customparameters():
    bot = BotRivescript(preprocessor="magic",postprocessor="super")

    assert bot._preprocessor == "magic"
    assert bot._postprocessor == "super"

def test_preandpostprocess_unchanged():

    preprocessed_message = bot._preprocess("do not change")
    postprocessed_message = bot._postprocess("do not change")

    assert "do not change" == preprocessed_message
    assert "do not change" == postprocessed_message

def test_process():
    mock_preprocessor = mock_messageprocessor.getProcessor()
    bot = BotRivescript(preprocessor=mock_preprocessor)

    preprocessed_message = bot._preprocess("change me")

    assert "Processed message: 'change me'" == preprocessed_message

def test_reply():
    bot = BotRivescript()
    bot._interpreter = mock_interpreter.getMock()

    expected = "Hello"
    actual = bot.reply(Message("id", "message"))

    assert expected == actual

def test_createusersession():
    userid = "toby"
    bot.createUserSession(userid)

    assert bot_recognizes_user(userid)

def get_expected_uservar_value():
    # rivescript returns 'None' when the user does not exist. It returns
    # "undefined" when the user exists but the variable has not been set,
    # see: http://rivescript.readthedocs.io/en/latest/rivescript.html#rivescript.rivescript.RiveScript.get_uservar
    return "undefined"

def bot_recognizes_user(userid):
    expected = get_expected_uservar_value()
    actual = bot._interpreter.get_uservar(userid, "the name of a variable that "
                                            "does not exist")

    return expected == actual
