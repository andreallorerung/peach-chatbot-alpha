'''Module to define a general way for synonyms to be stored for the chatbot
engine to use'''


class SynonymWriter(object):
    '''Class to define the interface of a synonym writer'''

    @staticmethod
    def writetofile(filepath, writemode='a', *synonyms):
        '''To write the specified variable length argument synonyms to the
        specified filepath with the specified writemode'''
        raise NotImplementedError("SynonymWriter is an interface")
