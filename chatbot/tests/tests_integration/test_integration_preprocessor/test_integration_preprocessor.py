from preprocess.preprocessor import MessagePreprocessor
import preprocess.tokenizer_simple
import preprocess.stopwords_remover_lenient
import preprocess.stemming_lancaster

preprocessor = MessagePreprocessor(tokenizer=preprocess.tokenizer_simple.SimpleTokenizerProxy(),
                                    stopwordRemover=preprocess.stopwords_remover_lenient.StopwordRemoverLenient(),
                                    stemmer=preprocess.stemming_lancaster.Lancaster())

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

def test_removestopwords():

    tokens = ["the", "message", "is", "so", "very", "full", "of", "stopwords",
    "in", "so","and","such","ways"]

    result = preprocessor._removeStopwords(tokens)

    assert len(result) < len(tokens)

def test_process():
    message = "The message is so very full of stopwords in so and such ways"

    expected = "mess is ful stopword way"
    actual = preprocessor.process(message)

    assert expected == actual
