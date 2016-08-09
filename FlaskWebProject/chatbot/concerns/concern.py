class Concern(object):
    def __init__(self, distressScore):
        self.distressScore = distressScore
        self.addressed = False

    def getDistressScore(self):
        return self.distressScore

    def hasBeenAddressed(self):
        return self.addressed

    def setAddressed(self):
        self.addressed = True
