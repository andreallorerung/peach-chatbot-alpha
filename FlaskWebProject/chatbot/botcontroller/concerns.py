'''
This module defines a data module class named "UserConcerns" that wraps around a
dictionary in order to provide limited access to a set of
"concern"-"distress score" pairs. It also provides facilities to build
and associate UserConcerns instances to userids.

Each userid should be associated with a single concerns data model in order to
account for multiple concurrent users of the chatbot component.
'''
import collections


class Concern(object):
    def __init__(self, distressScore):
        self.distressScore
        self.addressed = False

    def getDistressScore(self):
        return self.distressScore

    def hasBeenAddressed(self):
        return self.addressed

    def setAddressed(self):
        self.addressed = True

class UserConcerns(object):
    '''Data model for a user's concerns'''

    def __init__(self):
        self._concernsMap = dict()

    def __getitem__(self, item):
        return self._check_key(item)

    def __setitem__(self, item, value):
        self._concernsMap[item] = value

    def _check_key(self, item):
        '''Checks to see if a value for the "item" parameter has been stored
        in the map'''
        try:
            return self._concernsMap[item]
        except KeyError:
            return None

class UserConcernsFactory(object):
    '''Factory class that returns an appropriate UserConcerns object per userid.
    Responsible for associating userids with concerns'''

    '''Collection of user sessions with the chatbot'''
    _usersessions = dict()

    @staticmethod
    def _create_concerns():
        '''Creates a new UserConcerns data model for the userid'''
        new_concern = UserConcerns()
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
