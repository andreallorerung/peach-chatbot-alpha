'''Module to drive the chatbot brain through the highlighted topics'''
import operator
import concerns.topics
import concerns.drive_conversation_abstract
import concerns.concern

class DistressConversationDriver(concerns.drive_conversation_abstract.ConversationDriver):
    '''Class to drive the conversation through the questionnaire topics'''
    def __init__(self, userid):
        self.userid = userid
        self.userConcerns = dict()
        self.sortedUserConcernNames = []

    def setInitialUserConcerns(self, concerns):
        self.userConcerns = self._createConcernObjectsDict(concerns)
        self.sortedUserConcernNames = self._sortUserConcerns()

    @staticmethod
    def _createConcernObjectsDict(initialConcerns):
        concernsDict = dict()
        for key, value in initialConcerns.iteritems():
            concernsDict[key] = concerns.concern.Concern(value)

        return concernsDict

    def _sortUserConcerns(self):
        unsortedUserConcerns = self._getUserConcernsAsCoupleOfNameAndScore()
        sortedUserConcerns = self._sortConcernsByDistressScore(unsortedUserConcerns)

        sortedUserConcernNames = []
        for concern in sortedUserConcerns:
            sortedUserConcernNames.append(concern[0])

        return sortedUserConcernNames

    def _getUserConcernsAsCoupleOfNameAndScore(self):
        unsortedUserConcerns = []

        for concernName in concerns.topics.ALL_TOPICS:
            try:
                concern = self.userConcerns[concernName]
                distressScore = concern.getDistressScore()
                unsortedUserConcerns.append( (concernName, distressScore) )
            except KeyError: #key error occurs when the topic is not in the map
                continue
        return unsortedUserConcerns

    def _sortConcernsByDistressScore(self, unsortedUserConcerns):
        return sorted(unsortedUserConcerns, key=operator.itemgetter(1), reverse=True)

    def getNextConcern(self):
        for concernName in self.sortedUserConcernNames:
            concern = self.userConcerns[concernName]
            if not concern.hasBeenAddressed():
                return concernName

        return None

    def concernHasBeenAddressed(self, concernName):
        concern = self.userConcerns[concernName]

        return (concern is not None) and concern.hasBeenAddressed()

    def _markAddressed(self, concernName):
        concern = self.userConcerns[concernName]
        concern.setAddressed()

    def _getUserConcern(self, concernName):
        userConcerns = \
            concerns.concern_factory.UserConcernsFactory.getUserConcerns(self.userid)
        concern = userConcerns[concernName]

        if concern is None:
            raise KeyError("No concern about '{}' for userid '{}'"\
                            .format(concernName, self.userid))
        else: return concern
