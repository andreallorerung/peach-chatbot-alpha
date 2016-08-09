'''
This module defines a data module class named "UserConcerns" that wraps around a
dictionary in order to provide limited access to a set of
"concern"-"distress score" pairs. It also provides facilities to build
and associate UserConcerns instances to userids.

Each userid should be associated with a single concerns data model in order to
account for multiple concurrent users of the chatbot component.
'''


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
