'''To define a proxy to the RiveScript package'''
import interpreter
import rivescript
import rivescript_loader


class RiveScriptProxy(interpreter.Interpreter):
    def __init__(self, brain="./brain",rivescriptInterpreter=rivescript.RiveScript()):
        self._rivescriptInterpreter =\
                    rivescript_loader.loadBrain(rivescriptInterpreter, brain)

    def createUserSession(self, userInfo):
        # userinfo is expected to be just the userid *by this implementation!*
        userid = userInfo
        self._enterGlobalTopicFor(userid)
        self._moveToFirstConcernFor(userid)

    def _enterGlobalTopicFor(self, userid):
        reply = self._rivescriptInterpreter.reply(userid, "set glob")

    def _moveToFirstConcernFor(self, userid):
        reply = self._rivescriptInterpreter.reply(userid,
                                "internal matcher to start the conversation")

    def reply(self, userid, message):
        return self._rivescriptInterpreter.reply(userid, message)
