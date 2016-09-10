'''Module to define the conversation data model'''


class Conversation(object):
    '''Class to define a conversation'''
    def __init__(self, userid):
        self._userid = userid
        self._messages = []

    def append(self, message):
        '''To append a message to this conversation'''
        self._messages.append(message)
