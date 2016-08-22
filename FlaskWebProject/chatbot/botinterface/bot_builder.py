import rivescript
import bot_rivescript

def build():
    return bot_rivescript.BotRivescript()

class BotBuilder(object):

    def __init__(self):
        self.preprocessor = None
        self.postprocessor = None
        self.interpreter = None
        self.brain = None

    def addBrain(self, brain):
        self.brain = brain

    def addPreprocessor(self, preprocessor):
        self.preprocessor = preprocessor

    def addPostprocessor(self, postprocessor):
        self.postprocessor = postprocessor

    def build(self):
        self.interpreter = rivescript.RiveScript()

        return bot_rivescript.BotRivescript(
            preprocessor=self.preprocessor,
            postprocessor=self.postprocessor,
            interpreter=self.interpreter,
            brain=self.brain)
