'''Module to define a concrete keyword extractor that extracts only the first
keyword it finds in the message'''
import re
import keyword_extractor


class SingleKeywordExtractor(keyword_extractor.KeywordExtractor):
    '''Class to extract the first keyword from the set of templates'''
    def __init__(self):
        self._substringStart = "{{"
        self._substringEnd = "}}"
        self._keywordDelimiter = '\''

    def parseSearchParameter(self, message):
        return self._parseSearchParameter(message)

    def _parseSearchParameter(self, message):
        '''To parse search parameters within the system output message'''
        containerContent = self._parseKeywordContainer(message)
        keyword = self._parseKeyword(containerContent)

        return keyword.strip()

    def _parseKeywordContainer(self, message):
        '''To retrieve the content of the first keyword container found'''
        keywordContainerRE = self._compileRegularExpression(self._substringStart, self._substringEnd)
        containerContent = self._getMatchingGroups(message, keywordContainerRE)

        return containerContent

    def _parseKeyword(self, substringWithKeywords):
        '''To extract the content of the first keyword found within a keyword
        container'''
        keywordDelimiterRE = self._compileRegularExpression(self._keywordDelimiter, self._keywordDelimiter)
        keyword = self._getMatchingGroups(substringWithKeywords, keywordDelimiterRE)

        return keyword

    def _getMatchingGroups(self, searchSubject, regularExpression):
        '''To get the first element of the groups matching the regularExpression
        within the searchSubject'''
        try:
            results = re.search(regularExpression, searchSubject)
            target = results.groups()[0]
        except (TypeError, AttributeError):
            target = ""

        return target

    def _compileRegularExpression(self, startingRE, endingRE):
        '''To build up a regular expression that will extract the content of
        isolated instances of the specified delimiters'''
        return "{start}([^{end}]*){end}".format(start=startingRE, end=endingRE)
