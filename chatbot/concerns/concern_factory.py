'''Module to define creational logic for user concerns data models'''
import drive_conversation

class UserConcernsFactory(object):
    '''Factory class that returns an appropriate DistressConversationDriver
    object per userid. Responsible for associating userids with concerns'''

    '''Collection of user sessions with the chatbot'''
    _usersessions = dict()

    @staticmethod
    def _create_concerns(userid):
        '''Creates a new DistressConversationDriver data model for the userid'''
        new_concern = drive_conversation.DistressConversationDriver(userid)
        return new_concern

    @classmethod
    def getUserConcerns(cls, userid):
        '''Returns the DistressConversationDriver data model for the userid'''
        try:
            return cls._usersessions[userid]
        except KeyError:
            new_concern = cls._create_concerns(userid)
            cls._usersessions[userid] = new_concern

            return new_concern
