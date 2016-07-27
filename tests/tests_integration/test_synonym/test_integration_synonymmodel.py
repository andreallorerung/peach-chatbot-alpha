import pytest
from gensim.models.word2vec import Word2Vec
from synonym.synonym_model import *

WORDS_TO_GET_SYNONYMS_FOR = ["dad",
                            "hopeless",
                            "education",
                            "pain",
                            "faith",
                            "friend",
                            "interests",
                            "finance",
                            "sleeping",
                            "meaning"]

EXPECTED_SYNONYMS = {
    "dad":["Dad","father","grandpa","daddy","mom","stepdad","son","granddad",
            "uncle","brother"]
    ,"hopeless":["utterly_hopeless","forlorn","hopelessly","miserable",
                "pathetic","pitiful","helpless","seemingly_hopeless","bleak",
                "futile"]
    ,"education":["eduction","eduation","LISA_MICHALS_covers",
                    "Matt_Krupnick_covers","educational","educa_tion",
                    "edu_cation","educations","professionals_CEC_SmartBrief",
                    "curriculum"]
    ,"pain":["discomfort","chronic_pain","excruciating_pain","ache",
                "arthritic_pain","agony","soreness","throbbing_pain",
                "dull_ache","numbness"]
    ,"faith":["belief","Godly_principles","foundational_truths",
                "Biblical_principles","devoutness","religion",
                "congregational_polity","beliefs","religious_beliefs",
                "Jehovah_God"]
    ,"friend":["pal","friends","buddy","dear_friend","acquaintance","cousin",
                "girlfriend","colleague","uncle","roommate"]
    ,"interests":["detriment","vested_interests",
                    "wormholes_hypothetical_scientific","Getzschman_insisted",
                    "desires","intersts","interets","judiciary_Rehmat",
                    "agendas","intrests"]
    ,"finance":["Finance","financing","fi_nance","reporter_Sue_Lannin",
                "Ellen_Roseman_writes","professionals_ELFA_SmartBrief",
                "director_Karim_Naffah","initiatives_PFIs","Agha_Jan_Mohtasim",
                "fin_ance"]
    ,"sleeping":["slept","sleep","asleep","sleeping_soundly","Sleeping",
                    "snoozing","falling_asleep","sleeps","bed","dozing"]
    ,"meaning":["meanings","means","Designated_hitter_Joe_Mauer","denotations",
                "denote","mean","connotation","phrase","denotative",
                "grammatical_constructions"]
}

def test_synonyms_based_on_google_trained_word2vecmodel():
    model = Word2VecSynonymModel(word2vecmodel=Word2Vec.load_word2vec_format(
                './synonym/.trainedWord2Vec/GoogleNews-vectors-negative300.bin',
                binary=True))

    for word in WORDS_TO_GET_SYNONYMS_FOR:
        list_of_couples = model.get_synonyms(word)

        for synonym, couple in zip(EXPECTED_SYNONYMS[word], list_of_couples):
            first_element_of_couple = couple[0]
            assert synonym == first_element_of_couple
