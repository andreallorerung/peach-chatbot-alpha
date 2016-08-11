'''Module to drive the chatbot brain through the highlighted topics'''


class ConversationDriver(object):
    '''Class to drive the conversation through the questionnaire topics'''
    def __init__(self, userid):
        raise NotImplementedError("ConversationDriver is an interface")

    def setInitialUserConcerns(self, concerns):
        raise NotImplementedError("ConversationDriver is an interface")

    def getNextConcernName(self):
        raise NotImplementedError("ConversationDriver is an interface")

    def concernHasBeenAddressed(self, concern):
        raise NotImplementedError("ConversationDriver is an interface")
