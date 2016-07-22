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

    def __init__(self, userid, scores=collections.defaultdict()):
        self._userid = userid
        self._scores = scores

    def __getitem__(self, item):
        if item == "userid":
            return self._userid
        else:
            return self._check_key(item)

    def __setitem__(self, item, value):
        if item == "userid":
            raise ValueError("Cannot set the userid property of a Concerns "
            "object, it is necessary to reinitialize the instance to change "
            "userid")
        else:
            self._scores[item] = value

    def _check_key(self, item):
        try:
            return self._scores[item]
        except KeyError:
            return None

class ConcernsFactory(object):
    '''Factory class that returns an appropriate Concerns object per userid'''

    _usersessions = collections.defaultdict()

    @staticmethod
    def _create_concerns(userid):
        new_concern = Concerns(userid) #isn't there a bit of pernicious reduncancy here? userid is stored both in Concerns and ConcernsFactory
        return new_concern

    @classmethod
    def getConcerns(cls, userid):
        try:
            return cls._usersessions[userid]
        except KeyError:
            new_concern = cls._create_concerns(userid)
            cls._usersessions[userid] = new_concern

            return new_concern