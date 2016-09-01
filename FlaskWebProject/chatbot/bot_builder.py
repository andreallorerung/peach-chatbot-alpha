import rivescript
import botinterface.rivescript_proxy
import botinterface.bot_rivescript
import preprocess.preprocessor_builder
import postprocess.postprocessor_builder

def build():
    preprocessor = preprocess.preprocessor_builder.build()
    postprocessor = postprocess.postprocessor_builder.build()
    interpreter = botinterface.rivescript_proxy.RiveScriptProxy(\
                        rivescriptInterpreter=rivescript.RiveScript(debug=False))
    return botinterface.bot_rivescript.BotRivescript(preprocessor=preprocessor,
                                interpreter=interpreter,
                                postprocessor=postprocessor)

class BotBuilder(object):

    def __init__(self):
        self.preprocessor = preprocess.preprocessor_builder.build()
        self.postprocessor = postprocess.postprocessor_builder.build()
        self.interpreter = None
        self.brain = "./brain"

    def addBrain(self, brain):
        self.brain = brain

    def addPreprocessor(self, preprocessor):
        self.preprocessor = preprocessor

    def addPostprocessor(self, postprocessor):
        self.postprocessor = postprocessor

    def addInterpreter(self, interpreter):
        self.interpreter = interpreter

    def build(self):
        if self.interpreter is None:
            productionRiveScript = rivescript.RiveScript(debug=False)
            self.interpreter = botinterface.rivescript_proxy.RiveScriptProxy(rivescriptInterpreter=productionRiveScript,brain=self.brain)

        return botinterface.bot_rivescript.BotRivescript(
            preprocessor=self.preprocessor,
            postprocessor=self.postprocessor,
            interpreter=self.interpreter)
