'''Module defining the python objects to be called inside '.rive' files '''
import topics
import concern_factory
from operator import itemgetter


def validateParametersNumber(args, num=1):
    '''Checks that there are enough arguments being passed into the macro'''
    if not args or len(args) < num:
        raise ValueError(" macro called without arguments. Needs "
        "exactly {}.".format(num))
    else:
        return True

def increase(currentValue):
    '''To increase the value of the argument by 1'''
    # values must be passed out to the rivescript macro object as strings
    newValue = str(int(currentValue) + 1)
    return newValue

def decrease(currentValue):
    '''To decrease the value of the argument by 1'''
    # values must be passed out to the rivescript macro object as strings
    newValue = str(int(currentValue) - 1)
    return newValue

def getNextConcern(userid):
    '''To return the next concern for the user'''
    conversationDriver = \
        concern_factory.UserConcernsFactory.getUserConcerns(userid)

    return conversationDriver.getNextConcernName()

def isDistressSignificantFor(userid, microtopic):
    '''To decide whether distress score is significant for the user and topic'''
    conversationDriver = \
        concern_factory.UserConcernsFactory.getUserConcerns(userid)
    distressScore = conversationDriver.getConcernScore(microtopic)

    if distressScore >= 9:
        return True
    else:
        return False

def dummy_f():
    '''Dummy function used to test calling from rive file'''
    return 0
