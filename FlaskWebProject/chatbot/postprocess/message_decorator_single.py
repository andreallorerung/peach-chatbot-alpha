import string
import message_decorator


class MessageDecoratorSingle(message_decorator.MessageDecorator):
    def __init__(self):
        self._substringStart = "{{"
        self._substringEnd = "}}"

    def decorateMessageWith(self, message, toDecorateWith):
        return self._decorateMessage(message, toDecorateWith)

    def _decorateMessage(self, message, toDecorateWith):
        templatedMessage = self._replaceDelimitedSubstring(message)
        decoratedMessage = self._substituteTemplateWith(templatedMessage, toDecorateWith)

        return decoratedMessage

    def _replaceDelimitedSubstring(self, message):
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
        startingIndexOfSubstringToReplace = message.index(self._substringStart)
        endingIndexOfSubstringToReplace = message.index(self._substringEnd) + len(self._substringEnd)

        beginningMessageSlice = message[:startingIndexOfSubstringToReplace]
        endingMessageSlice = message[endingIndexOfSubstringToReplace:]
        return beginningMessageSlice, endingMessageSlice

    def _substituteTemplateWith(self, message, result):
        template = string.Template(message)
        decoratedMessage = template.substitute(toReplace=result)

        return decoratedMessage
