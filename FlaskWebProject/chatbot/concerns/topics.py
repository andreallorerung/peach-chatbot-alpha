'''Module representing the issue topics recognized by the chatbot and their
relationship to macro-categories of topics (physical, emotional issues etc)'''
import equivalence

'''List representing all issues that can be selected'''
ALL_TOPICS = ["respiratory","urinary","constipation","diarrhoea","eating","indigestion",
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
    (tuple(ALL_TOPICS[0:5])) : "physical",
    (tuple(ALL_TOPICS[6:11])) : "physical",
    (tuple(ALL_TOPICS[12:17])) : "physical",
    (tuple(ALL_TOPICS[18:23])) : "physical",
    (tuple(ALL_TOPICS[24:29])) : "practical",
    (tuple(ALL_TOPICS[25:27])) : "practical",
    (tuple(ALL_TOPICS[28:30])) : "family",
    (tuple(ALL_TOPICS[31:36])) : "emotional",
    (tuple(ALL_TOPICS[37:39])) : "emotional",
    (tuple(ALL_TOPICS[40:])) : "spiritual"
}

micro_to_macro = equivalence.EquivalenceClasses.from_dict(CLASSES)
