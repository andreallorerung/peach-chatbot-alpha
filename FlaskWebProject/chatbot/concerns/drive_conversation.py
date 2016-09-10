'''Module to drive the chatbot brain through the highlighted topics'''
import operator
import topics
import drive_conversation_abstract
import concern


class DistressConversationDriver(drive_conversation_abstract.ConversationDriver):
    '''Class to drive the conversation through the questionnaire topics'''
    def __init__(self, userid):
        self.userid = userid
        self.userConcerns = dict()
        self.sortedUserConcernNames = []

    def setInitialUserConcerns(self, concerns):
        '''To set the initial user concerns extracted independently of the
        chatbot system'''
        self.userConcerns = self._createConcernObjectsDict(concerns)
        self.sortedUserConcernNames = self._sortUserConcerns()

    @staticmethod
    def _createConcernObjectsDict(initialConcerns):
        '''To extract a dictionary of Concern objects from a dictionary of
        concernName -> concernDistressScore'''
        concernsDict = dict()
        for key, value in initialConcerns.iteritems():
            concernsDict[key] = concern.Concern(value)

        return concernsDict

    def _sortUserConcerns(self):
        '''To return a linear data structure of sorted concerns'''
        unsortedUserConcerns = self._getUserConcernsAsCoupleOfNameAndScore()
        sortedUserConcerns = self._sortConcernsByDistressScore(unsortedUserConcerns)

        sortedUserConcernNames = []
        for concern in sortedUserConcerns:
            sortedUserConcernNames.append(concern[0])

        return sortedUserConcernNames

    def _getUserConcernsAsCoupleOfNameAndScore(self):
        '''To return a list of couples of concern name and score'''
        unsortedUserConcerns = []

        for concernName in topics.ALL_TOPICS:
            try:
                concern = self.userConcerns[concernName]
                distressScore = concern.getDistressScore()
                unsortedUserConcerns.append( (concernName, distressScore) )
            except KeyError: #key error occurs when the topic is not in the map
                continue
        return unsortedUserConcerns

    def _sortConcernsByDistressScore(self, unsortedUserConcerns):
        '''To sort a list of couples of concern name and score in descending
        order'''
        return sorted(unsortedUserConcerns, key=operator.itemgetter(1), reverse=True)

    def getNextConcernName(self):
        '''To return the name of the next unaddressed user concern on the list,
        or None when there are no concerns, or no unaddressed concerns'''
        for concernName in self.sortedUserConcernNames:
            concern = self.userConcerns[concernName]
            if not concern.hasBeenAddressed():
                return concernName

        return None

    def concernHasBeenAddressed(self, concernName):
        '''To decide whether a concern has been addressed'''
        concern = self.userConcerns[concernName]

        return (concern is not None) and concern.hasBeenAddressed()

    def getConcernScore(self, concernName):
        '''To get the score for a concern'''
        try:
            concern = self.userConcerns[concernName]
        except KeyError:
            raise KeyError("No concern '{}' stored for user {}".format(concernName, self.userid))

        return concern.getDistressScore()

    def _markAddressed(self, concernName):
        '''To mark a concern as addressed'''
        concern = self.userConcerns[concernName]
        concern.setAddressed()
