'''Module to define the interface of a pattern interpreter'''


class Interpreter(object):
    """docstring for ."""
    def __init__(self):
        raise NotImplementedError("Interpreter is an interface")

    def createUserSession(self, userinfo):
        '''To start a usersession for the userinfo'''
        raise NotImplementedError("Interpreter is an interface")

    def reply(self, userid, message):
        '''To return a reply for the userid given the message'''
        raise NotImplementedError("Interpreter is an interface")
