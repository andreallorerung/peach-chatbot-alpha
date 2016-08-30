import rivescript
import botinterface.bot_rivescript
import preprocess.preprocessor_builder
import postprocess.postprocessor_builder

def build():
    preprocessor = preprocess.preprocessor_builder.build()
    postprocessor = postprocess.postprocessor_builder.build()
    return botinterface.bot_rivescript.BotRivescript(preprocessor=preprocessor,
                                interpreter=rivescript.RiveScript(debug=True),
                                postprocessor=postprocessor)

class BotBuilder(object):

    def __init__(self):
        self.preprocessor = preprocess.preprocessor_builder.build()
        self.postprocessor = postprocess.postprocessor_builder.build()
        self.interpreter = None
        self.brain = None

    def addBrain(self, brain):
        self.brain = brain

    def addPreprocessor(self, preprocessor):
        self.preprocessor = preprocessor

    def addPostprocessor(self, postprocessor):
        self.postprocessor = postprocessor

    def build(self):
        self.interpreter = rivescript.RiveScript(debug=False)

        return botinterface.bot_rivescript.BotRivescript(
            preprocessor=self.preprocessor,
            postprocessor=self.postprocessor,
            interpreter=self.interpreter,
            brain=self.brain)
