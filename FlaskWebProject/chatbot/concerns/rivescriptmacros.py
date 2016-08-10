'''Module defining the python objects to be called inside '.rive' files '''
import topics
import concerns
from operator import itemgetter

def validateParametersNumber(args, num=1):
    '''Checks that there are enough arguments being passed into the macro'''
    if not args or len(args) < num:
        raise ValueError(" macro called without arguments. Needs "
        "exactly {}.".format(num))
    else:
        return True

def increase(currentValue):
    '''Increases the number parameter'''
    # values must be passed out to the rivescript macro object as strings
    newValue = str(int(currentValue) + 1)
    return newValue

def getNextConcern(userid):
    userConversationDriver = \
        concerns.concern_factory.UserConcernsFactory.getUserConcerns(userid)

    return userConversationDriver.getNextConcern()
#
# def format_issue_list(issue_list):
#     '''Formats a list of tuples for output through the chatbot interface'''
#     output = ""
#
#     for issue_tuple in issue_list:
#         issue = issue_tuple[0]
#         score = issue_tuple[1]
#         output += "{}: {}\n".format(issue, score)
#     return output
#
# def get_all_issues(userid):
#     '''Returns all the issues highlighted so far for the userid, sorted in
#     descending order by level of distress (most distressful first)'''
#     issue_list = []
#
#     for issue in topics.ALL_ISSUES:
#         score = get_issue(userid, issue)
#         if score is not None:
#             issue_list.append( ( issue, score) )
#
#     return sorted(issue_list, key=itemgetter(1), reverse=True)
#
# def get_issue(userid, issue):
#     '''Returns an issue score from the map of issues for the current user'''
#     concerns = model.UserConcernsFactory.getUserConcerns(userid)
#     return concerns[issue]

def dummy_f():
    '''Dummy function used to test calling from rive file'''
    return 0
