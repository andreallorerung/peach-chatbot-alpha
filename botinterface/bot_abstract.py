

class BotInterface(object):
    
    def __init__(self):
        raise NotImplementedError("BotInterface is an interface")

    def reply(self):
        raise NotImplementedError("BotInterface is an interface")
