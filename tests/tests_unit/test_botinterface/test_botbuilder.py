from botinterface import bot_builder

def test_build_minimal():
    bot = bot_builder.build()

    assert hasattr(bot, "reply")
