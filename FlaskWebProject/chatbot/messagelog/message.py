'''Module to define a message data model'''


class Message(object):
    '''Class to define a message'''
    def __init__(self, userid, content):
        self.userid = userid
        self.content = content

    def getUserid(self):
        '''To return the user ID associated with this message'''
        return self.userid

    def getContent(self):
        return self.content
