'''
This module defines a data module class named "Concerns" that wraps around a
dictionary in order to provide limited access to a set of
"concern"-"distress score" pairs. It also provides facilities to build
and associate Concerns instances to userids.

Each userid should be associated with a single concerns data model in order to
account for multiple concurrent users of the chatbot component.
'''
import collections


class Concerns(object):
    '''Data model for a user's concerns'''

    def __init__(self):
        self._scores = dict()

    def __getitem__(self, item):
        return self._check_key(item)

    def __setitem__(self, item, value):
        self._scores[item] = value

    def _check_key(self, item):
        '''Checks to see if a value for the "item" parameter has been stored
        in the map'''
        try:
            return self._scores[item]
        except KeyError:
            return None

class ConcernsFactory(object):
    '''Factory class that returns an appropriate Concerns object per userid.
    Responsible for associating userids with concerns'''

    '''Collection of user sessions with the chatbot'''
    _usersessions = dict()

    @staticmethod
    def _create_concerns():
        '''Creates a new Concerns data model for the userid'''
        new_concern = Concerns()
        return new_concern

    @classmethod
    def getConcerns(cls, userid):
        '''Returns the Concerns data model for the userid'''
        try:
            return cls._usersessions[userid]
        except KeyError:
            new_concern = cls._create_concerns()
            cls._usersessions[userid] = new_concern

            return new_concern
