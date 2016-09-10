'''Module defining an equivalence class.'''


class EquivalenceClasses(object):
    '''An equivalence class is here implemented as a dictionary with multiple keys
    for the same value.

    Adapted from original implementation here:
    http://stackoverflow.com/a/11105962/6219368'''

    def __init__(self, **kwargs):
        self._keys = {}
        self._data = {}
        for k, v in kwargs.iteritems():
            self[k] = v

    def __getitem__(self, key):
        try:
            return self._data[key]
        except KeyError:
            return self._data[self._keys[key]]

    def __setitem__(self, key, val):
        try:
            self._data[self._keys[key]] = val
        except KeyError:
            first_key, other_keys = self._extract_keys(key)

            self._data[first_key] = val
            for k in other_keys:
                self._keys[k] = first_key

    def _extract_keys(self, key):
        '''Extract many keys from a single key-tuple. Returns the first element
        of the tuple and a list of the rest of the elements in the tuple'''
        if isinstance(key, tuple):
           if not key:
              raise ValueError(u'Empty tuple cannot be used as a key')
           first_key, other_keys = key[0], key[1:]
        else:
            first_key = key
            other_keys = []

        return first_key, other_keys

    @classmethod
    def from_dict(cls, dictionary):
        '''Builds an equivalnce class from a dictionary'''
        result = cls()
        for key, val in dictionary.items():
            result[key] = val
        return result
