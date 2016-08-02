'''Module to explify an implementation of a message postprocessor that decorates
a message by parsing a template (similarly to how angularjs decorates html)'''
import re


class MessagePostprocessorExample(object):
    '''Class to exemplify postprocessing a message'''
    def __init__(self):
        pass

    def process(self, output):
        '''To decorate an output message from the chatbot'''
        command = self._parse(output)
        queryKeyword = self._readKeyword(command)

        return self._query(queryKeyword)

    def _parse(self, output):
        '''To parse commands within the output message'''
        result = re.search("{{(.*)}}", output)
        target = result.groups(1)[0]

        return target.strip()

    def _readKeyword(self, command):
        '''To read a keyword within the command'''
        split = command.split('.')

        keywordField = split[1]

        result = re.search("'(.*)'", keywordField)
        target = result.groups(1)[0]

        return target.strip()

    def _query(self, keyword):
        '''To exemplify the result of a query given a keyword'''
        return "http://{}.com".format(keyword)
