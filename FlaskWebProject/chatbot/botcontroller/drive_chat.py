'''Module to drive the chatbot brain through the highlighted topics'''
import concerns

class ConversationDriver(object):
    '''Class to drive the conversation through the questionnaire topics'''
    def __init__(self, rivescriptInterpreter):
        self.rivescriptInterpreter = rivescriptInterpreter

    def setIssuesForUser(self, userid, issues):
        for issue in issues:
            self._setIssueForUser(userid, *issue) #each issue is a pair

    def _setIssueForUser(self, userid, issueName, issueScore):
        '''Sets an issue score for the current user'''
        concerns = concerns.ConcernsFactory.getConcerns(userid)
        concerns[issueName] = issueScore

    def reply(self, message):
        return "hello"
        # initialized: issue set to most distressful

        # if all issues have been discussed finalize user session,
        # by asking the user to terminate conversation, user can at
        # this point only ask for a specific topic or agree to
        # ending conversation

        # loop body:
        # set topic in interpreter
        # forward preprocessed message to interpreter
        # get reply and return reply
        # interpreter can ask permission to change topic
        # in which case mark current topic as discussed

        # when is discussion saved? discussion must be saved one level
        # above in order to have access to unprocessed user input

    def moveToNextIssue(self):
        pass

    def hasTopicBeenCovered(self):
        pass
