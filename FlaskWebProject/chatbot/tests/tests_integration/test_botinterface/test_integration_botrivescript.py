import bot_builder
from botinterface.rivescript_proxy import RiveScriptProxy
from botinterface.bot_rivescript import BotRivescript
from botinterface.preprocessor import MessagePreprocessor
import preprocess.preprocessor_builder
from messagelog.message import Message

builder = bot_builder.BotBuilder()
builder.addPreprocessor(None)
bot = builder.build()

def test_reply_nopreprocess():
    message = Message("localuser", "set global")

    expectedsubstring = "ERR"
    actual = bot.reply(message)

    assert expectedsubstring in actual

def test_reply_withpreprocess():
    message = Message("localuser", "set global")

    bot = BotRivescript(preprocessor = preprocess.preprocessor_builder.build(),
                        interpreter=RiveScriptProxy())

    expected = "Topic set to global"
    actual = bot.reply(message)

    assert expected == actual
