from botinterface.preprocessor import MessagePreprocessor

preprocessor = MessagePreprocessor()

def test_init():

    assert preprocessor is not None

def test_runstemmer():

    message = ["I","do","not","believe","in","fairies"]
    expected = ["i","do","not","believ","in","fairy"]

    actual = preprocessor._stem(message)

    assert expected == actual

def test_tokenize():

    message = "I do not believe in fairies"
    expected = ["I","do","not","believe","in","fairies"]

    actual = preprocessor._tokenize(message)

    assert expected == actual

def test_join():
    tokens = ["I","do","not","believe","in","fairies"]
    expected = "I do not believe in fairies"

    actual = preprocessor._join(tokens)

    assert expected == actual
