from botinterface import bot_builder

builder = bot_builder.BotBuilder()

def test_build_minimal():
    bot = bot_builder.build()

    assert hasattr(bot, "reply")

def test_init():

    assert builder is not None
