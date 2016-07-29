from preprocess.stopwords_remover import *

nltkstopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']

sentences = ["I do not believe in myself",
            "Why you do this?",
            "why are you doing this?",
            "I do not think negations should be removed!",
            "My wife says she does not love me she has been distant",
            "My wife says she doesn't love me anymore, she has been distant",
            "they did not want me there",
            "I have been sick"]

def test_nltkstopwordremover():
    stopwordremover = StopwordRemoverNLTK()

    # nltkstopwordremover seems to eliminate too much
    without_stopwords = ["believe",
                       "this?",
                       "this?",
                       "think negations removed!",
                       "wife says love distant",
                       "wife says doesn't love anymore, distant",
                       "want",
                       "sick"]

    for expected, actual in \
    zip(without_stopwords, \
    [stopwordremover.removeStopwords(sentence) for sentence in sentences]):
        assert expected == actual
