import concerns.drive_conversation_abstract

def mockForUserWithConcern(userid, concern):
    mock = MockConversationDriver(userid)
    mock.concern = concern

    return mock

class MockConversationDriver(concerns.drive_conversation_abstract.ConversationDriver):
    def __init__(self, userid):
        self.concern = None

    def getNextConcernName(self):
        return self.concern

    def getConcernScore(self, concernName):
        if concernName == "some distressful concern":
            return 10

        elif concernName == "not a distressful concern":
            return 1

        else:
            return 5
