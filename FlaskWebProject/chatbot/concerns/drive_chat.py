'''Module to drive the chatbot brain through the highlighted topics'''
import operator
import topics
import concerns.concern_factory
import concerns.concern

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
        userConcerns = concerns.concern_factory.UserConcernsFactory.getUserConcerns(self.userid)
        userConcerns[concernName] = concerns.concern.Concern(concernScore)

    def _sortUserConcerns(self):
        unsortedUserConcerns = self._getUserConcernsAsCoupleOfNameAndScore(self.userid)
        sortedUserConcerns = self._sortConcernsByDistressScore(unsortedUserConcerns)

        sortedUserConcernNames = []
        for concern in sortedUserConcerns:
            sortedUserConcernNames.append(concern[0])

        return sortedUserConcernNames

    @staticmethod
    def _getUserConcernsAsCoupleOfNameAndScore(userid):
        userConcerns = \
            concerns.concern_factory.UserConcernsFactory.getUserConcerns(userid)
        unsortedUserConcerns = []

        for concernName in topics.ALL_TOPICS:
            concern = userConcerns[concernName]
            if concern is not None:
                distressScore = concern.getDistressScore()
                unsortedUserConcerns.append( (concernName, distressScore) )
        return unsortedUserConcerns

    def _sortConcernsByDistressScore(self, unsortedUserConcerns):
        return sorted(unsortedUserConcerns, key=operator.itemgetter(1), reverse=True)

    def getNextConcern(self):
        userConcerns = concerns.concern_factory.UserConcernsFactory.getUserConcerns(self.userid)

        for concernName in self.sortedUserConcernNames:
            concern = userConcerns[concernName]
            if not concern.hasBeenAddressed():
                return concernName

        return None

    def concernHasBeenAddressed(self, concernName):
        userConcerns = concerns.concern_factory.UserConcernsFactory.getUserConcerns(self.userid)
        concern = userConcerns[concernName]

        return (concern is not None) and concern.hasBeenAddressed()

    def _markAddressed(self, concernName):
        concern = self._getUserConcern(concernName)
        concern.setAddressed()

    def _getUserConcern(self, concernName):
        userConcerns = concerns.concern_factory.UserConcernsFactory.getUserConcerns(self.userid)
        concern = userConcerns[concernName]

        if concern is None:
            raise KeyError("No concern about '{}' for userid '{}'"\
                            .format(concernName, self.userid))
        else: return concern
