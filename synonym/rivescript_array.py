'''Module to model a rivescript array'''

class RivescriptArray(object):
    '''Class to model a rivescript array as a python object'''

    def __init__(self, arrayName, arrayContent):
        self.arrayName = arrayName
        self.arrayContent = arrayContent

    def __str__(self):
        return RivescriptArray.formatArray(self.arrayName, self.arrayContent)

    @staticmethod
    def formatArray(name, array):
        '''Formats a pair of name, array content to a string conforming to the
        rivescript 2.0 standard: https://www.rivescript.com/wd/RiveScript#array
        '''
        formattedArray = "|".join(array)
        return "! array {} = {}".format(name, formattedArray)
