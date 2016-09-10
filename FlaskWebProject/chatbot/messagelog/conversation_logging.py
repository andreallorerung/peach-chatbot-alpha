'''Module to define the conversation logging logic'''
import conversation as conversation_module
import message as message_module


MESSAGE_USERNAME_FOR_SYSTEM = "system"

class ConversationLogger(object):
    '''Class responsible for logging conversations between users and system'''
    # userid -> conversation
    _conversations = dict()

    @classmethod
    def logUserMessage(cls, message):
        '''To log a message on behalf of a user'''
        userid = message.getUserid()
        conversation = cls._retrieveConversationFor(userid)
        conversation.append(message)

    @classmethod
    def _retrieveConversationFor(cls, userid):
        '''To retrieve the conversation for a given user'''
        conversation = None
        try:
            conversation = cls._conversations[userid]

        except KeyError:
            conversation = conversation_module.Conversation(userid)
            cls._conversations[userid] = conversation

        return conversation

    @classmethod
    def logSystemReplyForUser(cls, replyContent, userid):
        '''To log a reply produced by the system for a conversation with the
        given user'''
        message = message_module.Message(MESSAGE_USERNAME_FOR_SYSTEM,
                                                replyContent)

        conversation = cls._retrieveConversationFor(userid)
        conversation.append(message)
