'''Module to define the message decorating logic for a single decoration'''
import string
import message_decorator


class MessageDecoratorSingle(message_decorator.MessageDecorator):
    '''Class to define the message decorating logic for a single decoration'''
    def __init__(self):
        self._substringStart = "{{"
        self._substringEnd = "}}"

    def decorateMessageWith(self, message, toDecorateWith):
        return self._decorateMessage(message, toDecorateWith)

    def _decorateMessage(self, message, toDecorateWith):
        '''To define the process of decorating'''
        templatedMessage = self._replaceDelimitedSubstring(message)
        decoratedMessage = self._substituteTemplateWith(templatedMessage, toDecorateWith)

        return decoratedMessage

    def _replaceDelimitedSubstring(self, message):
        '''To replace substrings delimited by the private properties of this
        class with templates'''
        try:
            beginningMessageSlice, endingMessageSlice = self._sliceMessage(message)
        except ValueError:
            # this is raised when the expected substrings indicating the start
            # and end of the message are found. The design of the class should
            # be improved to allow this comment to be removed.
            return message

        templatedMessage = "{}{}{}".format(
                                beginningMessageSlice,
                                "$toReplace",
                                endingMessageSlice)

        return templatedMessage

    def _sliceMessage(self, message):
        '''To slice the message based on its structure as parsed'''
        startingIndexOfSubstringToReplace = message.index(self._substringStart)
        endingIndexOfSubstringToReplace = message.index(self._substringEnd) + len(self._substringEnd)

        beginningMessageSlice = message[:startingIndexOfSubstringToReplace]
        endingMessageSlice = message[endingIndexOfSubstringToReplace:]
        return beginningMessageSlice, endingMessageSlice

    def _substituteTemplateWith(self, message, result):
        '''To replace template with information to decorate the message with'''
        template = string.Template(message)
        decoratedMessage = template.substitute(toReplace=result)

        return decoratedMessage
