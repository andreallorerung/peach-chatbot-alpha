import pytest
import botinterface.postprocessor
import postprocess.keyword_extractor_single
import postprocess.message_decorator_single
import mock_search_integration

REPLYSMOKING = "You can find more information here: {{ 'smoking' }}"
SIMPLETEMPLATE = "Oh look {{'interesting'}}"
ANOTHERTEMPLATE = "Let me tell you a {{'story'}} ... And they lived happily ever after"

MANYTEMPLATES = "There are three templates here: {{'more'}} {{'than'}} {{'can be handled'}}"
MANYKEYWORDS = "How many keywords are in here? {{ 'one' 'two' 'three' }}"
MANYTEMPLATESANDKEYWORDS = "Oh no! {{ 'this' 'means' }} {{ 'trouble' }}"

NOTEMPLATES = "Forgot to add templates"
NOKEYWORDS = "Here is an empty template: {{ }}"

postprocessor = botinterface.postprocessor.\
    MessagePostprocessor(keywordExtractor=postprocess.keyword_extractor_single.SingleKeywordExtractor(),
                        searchAdapter=mock_search_integration.MockSearch(),
                        messageDecorator=postprocess.message_decorator_single.MessageDecoratorSingle())

def test_process_smoking():
    systemReply = REPLYSMOKING
    processedReply = postprocessor.process(systemReply)

    expectedResult = "http://www.smoking.com"
    assert processedReply is not None
    assert expectedResult != processedReply
    assert expectedResult in processedReply
    assert "You can find more information here: http://www.smoking.com" == processedReply

def test_process_simple():
    systemReply = SIMPLETEMPLATE
    processedReply = postprocessor.process(systemReply)
    expected = "Oh look http://www.interesting.com"

    assert expected == processedReply

def test_process_anothersimple():
    systemReply = ANOTHERTEMPLATE
    processedReply = postprocessor.process(systemReply)
    expected = "Let me tell you a http://www.story.com ... And they lived happily ever after"

    assert expected == processedReply

def test_process_many_templates():
    systemReply = MANYTEMPLATES
    processedReply = postprocessor.process(systemReply)
    expected = "There are three templates here: http://www.more.com {{'than'}} {{'can be handled'}}"

    assert expected == processedReply

def test_process_many_keywords():
    systemReply = MANYKEYWORDS
    processedReply = postprocessor.process(systemReply)
    expected = "How many keywords are in here? http://www.one.com"

    assert expected == processedReply

def test_process_many_templates_and_keywords():
    systemReply = MANYTEMPLATESANDKEYWORDS
    processedReply = postprocessor.process(systemReply)
    expected = "Oh no! http://www.this.com {{ 'trouble' }}"

    assert expected == processedReply

def test_process_notemplates():
    systemReply = NOTEMPLATES
    processedReply = postprocessor.process(systemReply)
    expected = "Forgot to add templates"

    assert expected == processedReply

def test_process_nokeywords():
    systemReply = NOKEYWORDS
    processedReply = postprocessor.process(systemReply)
    expected = "Here is an empty template: None"

    assert expected == processedReply

def test_search_empty():
    searchResult = postprocessor._search("")

    assert searchResult is None

def test_process_null():
    systemReply = None
    with pytest.raises(TypeError):
        processedReply = postprocessor.process(systemReply)

def test_process_empty():
    systemReply = ""
    processedReply = postprocessor.process(systemReply)

    assert "" == processedReply
