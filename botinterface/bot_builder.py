import bot_rivescript

def build():
    return bot_rivescript.BotRivescript()
# I want the builder to be able to add stuff to a bot, a preprocessing layer,
# a bot brain and a postprocessing layer ... all this is doing is build a bot
# brain. Maybe it's best to work the bot interface object first

class BotBuilder(object):
    def addPreprocessor(preprocessor):
        pass

    def addPostprocessor(postprocessor):
        pass
