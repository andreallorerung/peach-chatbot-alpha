class MessageMock(object):
    def __init__(self, userid, content):
        self.userid = userid
        self.content = content

    def getUserid(self):
        return self.userid

    def getContent(self):
        return self.content
