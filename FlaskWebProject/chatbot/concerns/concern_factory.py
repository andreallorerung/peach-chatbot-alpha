import user_concerns

class UserConcernsFactory(object):
    '''Factory class that returns an appropriate UserConcerns object per userid.
    Responsible for associating userids with concerns'''

    '''Collection of user sessions with the chatbot'''
    _usersessions = dict()

    @staticmethod
    def _create_concerns():
        '''Creates a new UserConcerns data model for the userid'''
        new_concern = user_concerns.UserConcerns()
        return new_concern

    @classmethod
    def getUserConcerns(cls, userid):
        '''Returns the UserConcerns data model for the userid'''
        try:
            return cls._usersessions[userid]
        except KeyError:
            new_concern = cls._create_concerns()
            cls._usersessions[userid] = new_concern

            return new_concern
