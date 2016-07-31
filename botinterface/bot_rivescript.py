import rivescript
import bot_abstract


class BotRivescript(bot_abstract.BotInterface):

    def __init__(self, preprocessor=None,
                       interpreter=rivescript.RiveScript(),
                       postprocessor=None):
        self.preprocessor   = preprocessor
        self.interpreter    = interpreter
        self.postprocessor  = postprocessor

    def reply(self, message):
        message = self._preprocess(message)
        reply = interpreter.reply(message)
        reply = self._postprocess(reply)

        return reply

    def _preprocess(self, message):
        if self.preprocessor is not None:
            return self.preprocessor.process(message)
        else:
            return  message

    def _postprocess(self, reply):
        if self.postprocessor is not None:
            return self.postprocessor.process(reply)
        else:
            return reply
