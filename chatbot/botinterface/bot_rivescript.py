'''Module to define one implementation of the general interface to the chatbot'''
import interpreter
import message_processor
import bot_abstract


class BotRivescript(bot_abstract.BotInterface):
    '''Concrete class to define a general interface for the chatbot'''
    def __init__(self, preprocessor=None,
                       interpreter=None,
                       postprocessor=None):
        '''The chatbot interface includes an optional message preprocessing and
        reply postprocessing layers'''
        self._preprocessor = preprocessor
        self._interpreter = interpreter
        self._postprocessor = postprocessor

    def createUserSession(self, userInfo):
        self._interpreter.createUserSession(userInfo)

    def reply(self, message):
        userid = message.getUserid()
        messagecontent = self._preprocess(message.getContent())
        reply = self._interpreter.reply(userid, messagecontent)
        reply = self._postprocess(reply)

        return reply

    def _preprocess(self, message):
        '''To tell the preprocessor to preprocess the message (if the
        preprocessor has been initialized)'''
        if self._preprocessor is not None:
            return self._preprocessor.process(message)
        else:
            return  message

    def _postprocess(self, reply):
        '''To tell the postprocessor to postprocess the message (if the
        postprocessor has been initialized)'''
        if self._postprocessor is not None:
            return self._postprocessor.process(reply)
        else:
            return reply
