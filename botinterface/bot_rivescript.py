'''Module to define one implementation of the general interface to the chatbot'''
import rivescript
import bot_abstract


class BotRivescript(bot_abstract.BotInterface):
    '''Concrete class to define a general interface for the chatbot'''
    def __init__(self, preprocessor=None,
                       interpreter=rivescript.RiveScript(),
                       postprocessor=None):
        '''The chatbot interface includes an optional message preprocessing and
        reply postprocessing layers'''
        self.preprocessor   = preprocessor
        self.interpreter    = interpreter
        self.postprocessor  = postprocessor

    def reply(self, message):
        message = self._preprocess(message)
        reply = interpreter.reply(message)
        reply = self._postprocess(reply)

        return reply

    def _preprocess(self, message):
        '''To tell the preprocessor to preprocess the message (if the
        preprocessor has been initialized)'''
        if self.preprocessor is not None:
            return self.preprocessor.process(message)
        else:
            return  message

    def _postprocess(self, reply):
        '''To tell the postprocessor to postprocess the message (if the
        postprocessor has been initialized)'''
        if self.postprocessor is not None:
            return self.postprocessor.process(reply)
        else:
            return reply
