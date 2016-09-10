import postprocess.keyword_extractor_single

REPLYSMOKING = "You can find more information here: {{ 'smoking' }}"
SIMPLETEMPLATE = "Oh look {{'interesting'}}"
ANOTHERTEMPLATE = "Let me tell you a {{'story'}} ... And they lived happily ever after"

MANYTEMPLATES = "There are three templates here: {{'more'}} {{'than'}} {{'can be handled'}}"
MANYKEYWORDS = "How many keywords are in here? {{ 'one' 'two' 'three' }}"
MANYTEMPLATESANDKEYWORDS = "Oh no! {{ 'this' 'means' }} {{ 'trouble' }}"

NOTEMPLATES = "Forgot to add templates"
NOKEYWORDS = "Here is an empty template: {{ }}"

keywordExtractor = postprocess.keyword_extractor_single.SingleKeywordExtractor()

def test_init():
    assert hasattr(keywordExtractor, "parseSearchParameter")

def test_parseSearchParameter_smoking():
    actual = keywordExtractor.parseSearchParameter(REPLYSMOKING)
    expected = "smoking"

    assert expected == actual

def test_parseSearchParameter_simple():
    actual = keywordExtractor.parseSearchParameter(SIMPLETEMPLATE)
    expected = "interesting"

    assert expected == actual

def test_parseSearchParameters_story():
    actual = keywordExtractor.parseSearchParameter(ANOTHERTEMPLATE)
    expected = "story"

    assert expected == actual

def test_parseSearchParameter_many_templates():
    actual = keywordExtractor.parseSearchParameter(MANYTEMPLATES)
    expected = "more"

    assert expected == actual

def test_parseKeywordContainer_many_templates():
    actual = keywordExtractor._parseKeywordContainer(MANYTEMPLATES)
    expected = "'more'"

    assert expected == actual

def test_parseSearchParameter_many_keywords():
    actual = keywordExtractor.parseSearchParameter(MANYKEYWORDS)
    expected = "one"

    assert expected == actual

def test_parseSearchParameter_many_many():
    actual = keywordExtractor.parseSearchParameter(MANYTEMPLATESANDKEYWORDS)
    expected = "this"

    assert expected == actual

def test_parseSearchParameters_no_templates():
    actual = keywordExtractor.parseSearchParameter(NOTEMPLATES)
    expected = ""

    assert expected == actual

def test_parseSearchParameters_no_keywords():
    actual = keywordExtractor.parseSearchParameter(NOKEYWORDS)
    expected = ""

    assert expected == actual

def test_parseSearchParameters_empty():
    actual = keywordExtractor.parseSearchParameter("")
    expected = ""

    assert expected == actual

def test_parseSearchParameters_none():
    actual = keywordExtractor.parseSearchParameter(None)
    expected = ""

    assert "" == actual
