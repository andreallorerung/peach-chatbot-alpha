import rivescript
from botinterface.bot_rivescript import BotRivescript
import mock_messageprocessor

bot = BotRivescript()

def test_init():

    assert bot is not None

def test_hasreply():

    assert hasattr(bot, "reply")

def test_hasbot():

    assert hasattr(bot, "interpreter")
    # assert type(bot.interpreter) is rivescript.RiveScript

def test_haspreprocessor():

    assert hasattr(bot, "preprocessor")

def test_haspostprocessor():

    assert hasattr(bot, "postprocessor")

def test_init_customparameters():
    bot = BotRivescript(preprocessor="magic",postprocessor="super")

    assert bot.preprocessor == "magic"
    assert bot.postprocessor == "super"

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

def test_loaddirorfile():

    path_to_mockfile = ".\\tests\\tests_unit\\test_botinterface\mock_brain.rive"
    path_to_mockdir = ".\\tests\\tests_unit\\test_botinterface\mock_brain_dir"

    interpreter = bot._loadDirOrFile(rivescript.RiveScript(), path_to_mockfile)
    actual_bot_name_from_file = interpreter.get_variable("name")

    interpreter = bot._loadDirOrFile(rivescript.RiveScript(), path_to_mockdir)
    actual_bot_name_from_dir = interpreter.get_variable("name")

    expected_bot_name = "mocked"
    assert expected_bot_name == actual_bot_name_from_file
    assert expected_bot_name == actual_bot_name_from_dir
