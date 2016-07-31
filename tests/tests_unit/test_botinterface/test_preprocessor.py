from botinterface.preprocessor import MessagePreprocessor

def test_init():
    preprocessor = MessagePreprocessor()

    assert preprocessor is not None

def test_runstemmer():
    preprocessor = MessagePreprocessor()

    message = "I do not believe in fairies"
    expected = "i do not believ in fairy"

    actual = preprocessor._stem(message)

    assert expected == actual
