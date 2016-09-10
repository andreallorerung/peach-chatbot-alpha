from preprocess.stopwords_remover import StopwordRemover
from preprocess.stopword_remover_nltk import StopwordRemoverNLTK
from preprocess.stopwords_remover_lenient import StopwordRemoverLenient

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

tokenized_sentences = [
    ["I","do","not","believe","in","myself"],
    ["Why","you","do","this?"],
    ["why","are","you","doing","this?"],
    ["I","do","not","think","negations","should","be","removed!"],
    ["My","wife","says","she","does","not","love","me","she","has","been","distant"],
    ["My","wife","says","she","doesn't","love","me","anymore,","she","has","been","distant"],
    ["they","did","not","want","me","there"],
    ["I","have","been","sick"]]

limit_cases = ["", [11], list(), dict(), [None]]
limit_single_list = [["", 11, list(), dict(), None]]

def test_nltkstopwordremover():
    stopwordremover = StopwordRemoverNLTK()

    # nltkstopwordremover seems to eliminate too much
    without_stopwords = [["believe"],
                           ["this?"],
                           ["this?"],
                           ["think","negations","removed!"],
                           ["wife","says","love","distant"],
                           ["wife","says","doesn't","love","anymore,","distant"],
                           ["want"],
                           ["sick"]]

    for expected, actual in \
    zip(without_stopwords, \
    [stopwordremover.removeStopwords(tokens) for tokens in tokenized_sentences]):
        assert expected == actual

def test_nltkstopwordremover_limitcases():
        stopwordremover = StopwordRemoverNLTK()

        without_stopwords = [[],
                            [11],
                            [],
                            [],
                            [None]]

        for expected, actual in \
        zip(without_stopwords, \
        [stopwordremover.removeStopwords(tokens) for tokens in limit_cases]):
            assert expected == actual

def test_nltkstopwordremover_limitsinglelist():
    stopwordremover = StopwordRemoverNLTK()

    without_stopwords = [["", 11, list(), dict(), None]]

    for expected, actual in \
    zip(without_stopwords, \
    [stopwordremover.removeStopwords(tokens) for tokens in limit_single_list]):
        assert expected == actual

def test_lenientstopwordremover():
    stopwordremover = StopwordRemoverLenient()

    without_stopwords = [["I","not","believe","myself"],
                       ["Why","you","this?"],
                       ["why","are","you","this?"],
                       ["I","not","think","negations","should","be","removed!"],
                       ["My","wife","says","she","not","love","me","she","has","been","distant"],
                       ["My","wife","says","she","doesn't","love","me","anymore,","she","has","been","distant"],
                       ["they","not","want","me","there"],
                       ["I","have","been","sick"]]

    for expected, actual in \
    zip(without_stopwords, \
    [stopwordremover.removeStopwords(tokens) for tokens in tokenized_sentences]):
        assert expected == actual

def test_lenientstopwordremover_limitcases():
        stopwordremover = StopwordRemoverLenient()

        without_stopwords = [[],
                            [11],
                            [],
                            [],
                            [None]]

        for expected, actual in \
        zip(without_stopwords, \
        [stopwordremover.removeStopwords(tokens) for tokens in limit_cases]):
            assert expected == actual

def test_lenientstopwordremover_limitsinglelist():
    stopwordremover = StopwordRemoverLenient()

    without_stopwords = [["", 11, list(), dict(), None]]

    for expected, actual in \
    zip(without_stopwords, \
    [stopwordremover.removeStopwords(tokens) for tokens in limit_single_list]):
        assert expected == actual
