import rivescript
from botinterface.bot_rivescript import BotRivescript
import mock_messageprocessor

def test_init():
    bot = BotRivescript()

    assert bot is not None

def test_hasreply():
    bot = BotRivescript()

    assert hasattr(bot, "reply")

def test_hasbot():
    bot = BotRivescript()

    # assert hasattr(bot, "interpreter")
    assert type(bot.interpreter) is rivescript.RiveScript

def test_haspreprocessor():
    bot = BotRivescript()

    assert hasattr(bot, "preprocessor")

def test_haspostprocessor():
    bot = BotRivescript()

    assert hasattr(bot, "postprocessor")

def test_init_customparameters():
    bot = BotRivescript(preprocessor="magic",postprocessor="super")

    assert bot.preprocessor == "magic"
    assert bot.postprocessor == "super"

def test_preandpostprocess_unchanged():
    bot = BotRivescript()

    preprocessed_message = bot._preprocess("do not change")
    postprocessed_message = bot._postprocess("do not change")

    assert "do not change" == preprocessed_message
    assert "do not change" == postprocessed_message

def test_process():
    mock_preprocessor = mock_messageprocessor.getProcessor()
    bot = BotRivescript(preprocessor=mock_preprocessor)

    preprocessed_message = bot._preprocess("change me")

    assert "Processed message: 'change me'" == preprocessed_message
