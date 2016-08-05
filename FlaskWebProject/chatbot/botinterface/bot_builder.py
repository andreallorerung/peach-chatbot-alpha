import bot_rivescript

def build():
    return bot_rivescript.BotRivescript()

class BotBuilder(object):

    def __init__(self):
        self.bot = None

    def addBrain(self, brain):
        pass

    def addPreprocessor(self, preprocessor):
        pass

    def addPostprocessor(self, postprocessor):
        pass
