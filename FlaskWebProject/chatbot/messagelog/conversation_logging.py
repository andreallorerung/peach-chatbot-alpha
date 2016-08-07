import conversation as conversation_module

class ConversationLogger(object):

    _conversations = dict()

    @classmethod
    def logUserMessage(cls, message):
        userid = message.getUserid()
        conversation = cls._retrieveConversationFor(userid)

        conversation.append(message)

    @classmethod
    def _retrieveConversationFor(cls, userid):

        conversation = None
        try:
            conversation = cls._conversations[userid]

        except KeyError:
            conversation = conversation_module.Conversation(userid)
            cls._conversations[userid] = conversation

        return conversation

    @classmethod
    def logSystemReply(cls, message):
        pass
