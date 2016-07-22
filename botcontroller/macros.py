'''Module defining the python objects to be called inside '.rive' files '''
from botcontroller import concerns as model

def get_issue(userid, issue):
    '''Returns an issue score from the map of issues for the current user'''
    concerns = model.ConcernsFactory.getConcerns(userid)
    return concerns[issue]

def set_issue(userid, issue, score):
    '''Sets an issue score for the current user'''
    concerns = model.ConcernsFactory.getConcerns(userid)
    concerns[issue] = score

def validate_parameters(args, num=1):
    '''Checks that there are enough arguments being passed into the macro'''
    if not args or len(args) < num:
        raise ValueError("get_issues macro called without arguments. Needs "
                        "exactly one.")
    else:
        return True

def dummy_f():
    '''Dummy function used to test calling from rive file'''
    return 0
