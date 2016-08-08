'''Module to drive the chatbot brain through the highlighted topics'''
import operator
import topics
import concerns

class ConversationDriver(object):
    '''Class to drive the conversation through the questionnaire topics'''
    def __init__(self, userid):
        self.userid = userid
        self.sortedUserConcernsNames = self._sortUserConcerns()

    def setInitialUserConcerns(self, concerns):
        for concern in concerns:
            self._setConcern(*concern) #each concern is a pair
        self.sortedUserConcernNames = self._sortUserConcerns()

    def _setConcern(self, concernName, concernScore):
        '''Sets an concern score for the current user'''
        userConcerns = concerns.UserConcernsFactory.getUserConcerns(self.userid)
        userConcerns[concernName] = concerns.Concern(concernScore)

    def _sortUserConcerns(self):
        unsortedUserConcerns = self._getUserConcernsAsCoupleOfNameAndScore(self.userid)
        sortedUserConcerns = self._sortConcernsByDistressScore(unsortedUserConcerns)

        sortedUserConcernNames = []
        for concern in sortedUserConcerns:
            sortedUserConcernNames.append(concern[0])

        return sortedUserConcernNames

    @staticmethod
    def _getUserConcernsAsCoupleOfNameAndScore(userid):
        userConcerns = concerns.UserConcernsFactory.getUserConcerns(userid)
        unsortedUserConcerns = []

        for concernName in topics.ALL_TOPICS:
            concern = userConcerns[concernName]
            if concern is not None:
                distressScore = concern.getDistressScore()
                unsortedUserConcerns.append( (concernName, distressScore) )
        return unsortedUserConcerns

    def _sortConcernsByDistressScore(self, unsortedUserConcerns):
        return sorted(unsortedUserConcerns, key=operator.itemgetter(1), reverse=True)

    # def reply(self, message):
    #     return "hello"
        # initialized: concern set to most distressful
        #
        # if all concerns have been discussed, then finalize user session,
        # by asking the user to terminate conversation, user can at
        # this point only ask for a specific topic or agree to
        # ending conversation
        #
        # loop body:
        # set topic in interpreter
        # forward preprocessed message to interpreter
        # get reply and return reply
        # interpreter can ask permission to change topic
        # in which case mark current topic as discussed
        #
        # when is discussion saved? discussion must be saved one level
        # above in order to have access to unprocessed user input

    def moveToNextConcern(self):
        pass

    def concernHasBeenAddressed(self, concernName):
        userConcerns = concerns.UserConcernsFactory.getUserConcerns(self.userid)
        concern = userConcerns[concernName]

        return (concern is not None) and concern.hasBeenAddressed()

    def _markAddressed(self, concernName):
        concern = self._getUserConcern(concernName)
        concern.setAddressed()

    def _getUserConcern(self, concernName):
        userConcerns = concerns.UserConcernsFactory.getUserConcerns(self.userid)
        concern = userConcerns[concernName]

        if concern is None:
            raise KeyError("No concern about '{}' for userid '{}'"\
                            .format(concernName, self.userid))
        else: return concern
