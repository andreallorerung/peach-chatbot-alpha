'''Module to define what methods an implementation of an interface to the
chatbot must implement'''


class BotInterface(object):
    '''Interface to define the methods that an implementation of an interface to
    the chatbot must implement'''
    def __init__(self):
        raise NotImplementedError("BotInterface is an interface")

    def reply(self, message):
        '''To return a reply given the message'''
        raise NotImplementedError("BotInterface is an interface")
