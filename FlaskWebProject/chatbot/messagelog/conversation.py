class Conversation(object):
    def __init__(self, userid):
        self._userid = userid
        self._messages = []

    def append(self, message):
        self._messages.append(message)
