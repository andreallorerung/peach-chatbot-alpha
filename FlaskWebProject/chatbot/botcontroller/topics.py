'''Module representing the issue topics recognized by the chatbot and their
relationship to macro-categories of topics (physical, emotional issues etc)'''
from botcontroller.equivalence import EquivalenceClasses

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
"faith","meaning","regret"]

'''map of microtopics to macrotopics'''
CLASSES = {
    (tuple(ALL_ISSUES[0:5])) : "physical",
    (tuple(ALL_ISSUES[6:11])) : "physical",
    (tuple(ALL_ISSUES[12:17])) : "physical",
    (tuple(ALL_ISSUES[18:23])) : "physical",
    (tuple(ALL_ISSUES[24:29])) : "practical",
    (tuple(ALL_ISSUES[25:27])) : "practical",
    (tuple(ALL_ISSUES[28:30])) : "family",
    (tuple(ALL_ISSUES[31:36])) : "emotional",
    (tuple(ALL_ISSUES[37:39])) : "emotional",
    (tuple(ALL_ISSUES[40:])) : "spiritual"
}

micro_to_macro = EquivalenceClasses.from_dict(CLASSES)
