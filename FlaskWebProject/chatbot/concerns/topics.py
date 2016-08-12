'''Module representing the issue topics recognized by the chatbot and their
relationship to macro-categories of topics (physical, emotional issues etc)'''
import equivalence

'''List representing all issues that can be selected'''
PHYSICAL1 = ["respiratory","urinary","constipation","diarrhoea","eating","indigestion"]
PHYSICAL2 = ["mouth","nausea-vomit","sleeping","fatigue","swelling","fever"]
PHYSICAL3 = ["walking","tingling","pain","hot-flushes","skin","wound-care"]
PHYSICAL4 = ["weight","memory-concentration","sensory","speaking","appearance","sexuality"]
PRACTICAL1 = ["caring-responsibilities","work-education","finance-housing","travel","transport","communication-NHS"]
PRACTICAL2 = ["chores","washing-dressing","preparing-meal"]
FAMILY = ["partner","children","relative-friend"]
EMOTIONAL1 = ["planning","interests-activities","expressing-feelings","anger-frustration","guilt","hopelessness"]
EMOTIONAL2 = ["loneliness","depression","worry-fear-anxiety"]
SPIRITUAL = ["faith","meaning","regret"]
'''Aggregation of all topics'''
ALL_TOPICS = PHYSICAL1 +\
             PHYSICAL2 +\
             PHYSICAL3 +\
             PHYSICAL4 +\
             PRACTICAL1 +\
             PRACTICAL2 +\
             FAMILY +\
             EMOTIONAL1 +\
             EMOTIONAL2 +\
             SPIRITUAL

'''mapping of microtopics to macrotopics'''
CLASSES = {
    (tuple(PHYSICAL1))  : "physical",
    (tuple(PHYSICAL2))  : "physical",
    (tuple(PHYSICAL3))  : "physical",
    (tuple(PHYSICAL4))  : "physical",
    (tuple(PRACTICAL1)) : "practical",
    (tuple(PRACTICAL2)) : "practical",
    (tuple(FAMILY))     : "family",
    (tuple(EMOTIONAL1)) : "emotional",
    (tuple(EMOTIONAL2)) : "emotional",
    (tuple(SPIRITUAL))  : "spiritual"
}

'''Equivalence class of micro- to macro- topics'''
macrotopicFor = equivalence.EquivalenceClasses.from_dict(CLASSES)
