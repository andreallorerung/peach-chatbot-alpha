from botinterface.preprocessor import MessagePreprocessor
import mock_tokenizer
import mock_stopwordremover
import mock_stemmer

WORDTOREMOVE = "removeme"

preprocessor = MessagePreprocessor(tokenizer=mock_tokenizer.MockTokenizer(),
                                    stopwordRemover=mock_stopwordremover.MockSingleStopwordRemover(WORDTOREMOVE),
                                    stemmer=mock_stemmer.MockStemmer())

def test_init():

    assert preprocessor is not None


def test_runstemmer():

    message = ["I","do","not","believe","in","fairies"]
    expected = ["","d","no","believ","i","fairie"]

    actual = preprocessor._stem(message)

    assert expected == actual

def test_tokenize():

    message = "I do not believe in fairies"
    expected = ["I","do","not","believe","in","fairies"]

    actual = preprocessor._tokenize(message)

    assert expected == actual

def test_removestopwords():

    tokens = [WORDTOREMOVE, "from", "this", "message"]

    result = preprocessor._removeStopwords(tokens)

    assert len(result) == len(tokens) - 1

def test_process():
    message = "The message is so very full of stopwords in so and such ways {}".format(WORDTOREMOVE)

    expected = "Th messag i s ver ful o stopword i s an suc way"
    actual = preprocessor.process(message)

    assert expected == actual

#
# def test_runstemmer():
#
#     message = ["I","do","not","believe","in","fairies"]
#     expected = ["i","do","not","believ","in","fairy"]
#
#     actual = preprocessor._stem(message)
#
#     assert expected == actual
#
# def test_tokenize():
#
#     message = "I do not believe in fairies"
#     expected = ["I","do","not","believe","in","fairies"]
#
#     actual = preprocessor._tokenize(message)
#
#     assert expected == actual
#
# def test_join():
#     tokens = ["I","do","not","believe","in","fairies"]
#     expected = "I do not believe in fairies"
#
#     actual = preprocessor._join(tokens)
#
#     assert expected == actual
#
# def test_removestopwords():
#
#     tokens = ["the", "message", "is", "so", "very", "full", "of", "stopwords",
#     "in", "so","and","such","ways"]
#
#     result = preprocessor._removeStopwords(tokens)
#
#     assert len(result) < len(tokens)
#
# def test_process():
#     message = "The message is so very full of stopwords in so and such ways"
#
#     expected = "mess is ful stopword way"
#     actual = preprocessor.process(message)
#
#     assert expected == actual
