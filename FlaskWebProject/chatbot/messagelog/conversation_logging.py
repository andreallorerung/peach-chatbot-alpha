import conversation as conversation_module
import message as message_module

MESSAGE_USERNAME_FOR_SYSTEM = "system"

class ConversationLogger(object):

    # userid -> conversation
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
    def logSystemReplyForUser(cls, replyContent, userid):
        message = message_module.Message(MESSAGE_USERNAME_FOR_SYSTEM,
                                                replyContent)

        conversation = cls._retrieveConversationFor(userid)
        conversation.append(message)
