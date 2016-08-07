class Conversation(object):
    def __init__(self, userid):
        self._userid = userid
        self._messages = []

    def append(self, message):
        self._checkUserId(message)
        self._messages.append(message)

    def _checkUserId(self, message):
        messageUserId = message.getUserid()
        if messageUserId != self._userid:
            raise KeyError("Attempted to append message with userid '{}' to a "
            "conversation with userid '{}'. Message does not belong to this "
            "conversation.".format(messageUserId, self._userid))
