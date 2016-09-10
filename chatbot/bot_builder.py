'''Module to define creational logic for a chatbot'''
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
    '''Class to define a chatbot builder'''
    def __init__(self):
        self.preprocessor = preprocess.preprocessor_builder.build()
        self.postprocessor = postprocess.postprocessor_builder.build()
        self.interpreter = None
        self.brain = "./brain"

    def addBrain(self, brain):
        '''To specify the brain of the chatbot'''
        self.brain = brain

    def addPreprocessor(self, preprocessor):
        '''To specify a message preprocessor for the chatbot'''
        self.preprocessor = preprocessor

    def addPostprocessor(self, postprocessor):
        '''To specify a message postprocessor for the chatbot'''
        self.postprocessor = postprocessor

    def addInterpreter(self, interpreter):
        '''To specify the language interpreter for the chatbot'''
        self.interpreter = interpreter

    def build(self):
        '''To assemble and return the chatbot instance'''
        if self.interpreter is None:
            productionRiveScript = rivescript.RiveScript(debug=False)
            self.interpreter = botinterface.rivescript_proxy.RiveScriptProxy(
                rivescriptInterpreter=productionRiveScript, brain=self.brain)

        return botinterface.bot_rivescript.BotRivescript(
            preprocessor=self.preprocessor,
            postprocessor=self.postprocessor,
            interpreter=self.interpreter)
