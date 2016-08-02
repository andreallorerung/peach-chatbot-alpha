import botinterface.bot_abstract

def getMock():
    return MockInterpreter()

class MockInterpreter(botinterface.bot_abstract.BotInterface):
    def __init__(self):
        pass

    def reply(self, userid, message):
        return "Hello"
