'''Module to drive the chatbot brain through the highlighted topics'''


class ConversationDriver(object):
    '''Class to drive the conversation through the questionnaire topics'''
    def __init__(self, userid):
        raise NotImplementedError("ConversationDriver is an interface")

    def setInitialUserConcerns(self, concerns):
        '''To set the initial user concerns extracted independently of the
        chatbot system'''
        raise NotImplementedError("ConversationDriver is an interface")

    def getNextConcernName(self):
        '''To retur the name of the next unaddressed user concern on the list,
        or None when there are no concerns, or no unaddressed concerns'''
        raise NotImplementedError("ConversationDriver is an interface")

    def getConcernScore(self, concern):
        '''To return the concern distress score'''
        raise NotImplementedError("ConversationDriver is an interface")


    def concernHasBeenAddressed(self, concern):
        '''To decide whether a concern has been addressed'''
        raise NotImplementedError("ConversationDriver is an interface")
