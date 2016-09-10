'''Module to define a concrete system reply processor'''


class MessagePostprocessor(object):
    '''Class to postprocess a system reply by decorating it with the result
    of a search query, if the system reply cointained a template to decorate
    with such result'''
    def __init__(self, keywordExtractor, searchAdapter, messageDecorator):
        self._keywordExtractor = keywordExtractor
        self._searchEngineAdapter = searchAdapter
        self._messageDecorator = messageDecorator

    def process(self, message):
        self._validateMessage(message)

        keywordFound = self._extractKeyword(message)
        result = self._search(keywordFound)
        decoratedMessage = self._decorateMessage(message, result)

        return decoratedMessage

    def _validateMessage(self, message):
        if message is None:
            raise TypeError("Invalid type '{}' was passed to the "
                    "MessagePostprocessor".format(type(message)))

    def _extractKeyword(self, message):
        '''To extract a search keyword from the message'''
        return self._keywordExtractor.parseSearchParameter(message)

    def _search(self, keyword):
        '''To perform a search by the keyword'''
        return self._searchEngineAdapter.search(keyword)

    def _decorateMessage(self, message, result):
        '''To decorate a message with the result'''
        return self._messageDecorator.decorateMessageWith(message, result)
