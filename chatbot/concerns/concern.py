'''Module to define the internal representation of individual user concerns'''


class Concern(object):
    '''Class to define an individual user concern'''
    def __init__(self, distressScore):
        '''To create a new concern representation'''
        self.distressScore = distressScore
        self.addressed = False

    def getDistressScore(self):
        '''To return the distress score of the concern'''
        return self.distressScore

    def hasBeenAddressed(self):
        '''To decide whether the concern has been addressed'''
        return self.addressed

    def setAddressed(self):
        '''To mark the concern as addressed'''
        self.addressed = True
