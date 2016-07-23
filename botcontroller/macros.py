'''Module defining the python objects to be called inside '.rive' files '''
from botcontroller import concerns as model
from botcontroller.equivalence import EquivalenceClasses
from operator import itemgetter

'''List representing all issues that can be selected'''
ALL_ISSUES = ["respiratory","urinary","constipation","diarrhoea","eating","indigestion",
"mouth","nausea-vomit","sleeping","fatigue","swelling","fever",
"walking","tingling","pain","hot-flushes","skin","wound-care",
"weight","memory-concentration","sensory","speaking","appearance","sexuality",
"caring-responsibilities","work-education","finance-housing","travel","transport","communication-NHS",
"chores","washing-dressing","preparing-meal",
"partner","children","relative-friend",
"planning","interests-activities","expressing-feelings","anger-frustration","guilt","hopelessness",
"loneliness","depression","worry-fear-anxiety",
"lost-faith-spiritual","lost-meaning-purpose","regret"]

'''map of microtopics to macrotopics'''
CLASSES = {
    ("partner","children","relative-friend"): "family",
    ("planning","interests-activities","expressing-feelings",
    "anger-frustration","guilt","hopelessness") : "emotional_1",
}

micro_to_macro = EquivalenceClasses.from_dict(CLASSES)

def format_issue_list(issue_list):
    '''Formats a list of tuples for output through the chatbot interface'''
    output = ""

    for issue_tuple in issue_list:
        issue = issue_tuple[0]
        score = issue_tuple[1]
        output += "{}: {}\n".format(issue, score)
    return output

def get_all_issues(userid):
    '''Returns all the issues highlighted so far for the userid, sorted in
    descending order by level of distress (most distressful first)'''
    issue_list = []

    for issue in ALL_ISSUES:
        score = get_issue(userid, issue)
        if score is not None:
            issue_list.append( ( issue, score) )

    return sorted(issue_list, key=itemgetter(1), reverse=True)

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
        raise ValueError(" macro called without arguments. Needs "
                        "exactly {}.".format(num))
    else:
        return True

def dummy_f():
    '''Dummy function used to test calling from rive file'''
    return 0
