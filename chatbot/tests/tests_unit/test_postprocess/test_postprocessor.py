import pytest
import postprocess.postprocessor
import mock_keywordextractor
import mock_search
import mock_decorator

REPLYSMOKING = "You can find more information here: {{ 'smoking' }}"

postprocessor = botinterface.postprocessor.\
    MessagePostprocessor(keywordExtractor=mock_keywordextractor.MockKeywordextractor(),
                        searchAdapter=mock_search.MockSearch(),
                        messageDecorator=mock_decorator.MockDecorator())

def test_hasadapter():
    assert hasattr(postprocessor, "_searchEngineAdapter")
    assert hasattr(postprocessor._searchEngineAdapter, "search")

def test_process():
    systemReply = REPLYSMOKING
    processedReply = postprocessor.process(systemReply)

    expectedResult = "http://www.smoking.com"
    assert processedReply is not None
    assert expectedResult != processedReply
    assert expectedResult in processedReply
    assert "You can find more information here: http://www.smoking.com" == processedReply

def test_parseSearchParameters():
    systemReply = REPLYSMOKING
    foundParameters = postprocessor._extractKeyword(systemReply)
    print foundParameters
    assert "smoking" == foundParameters

def test_process_null():
    systemReply = None
    with pytest.raises(TypeError):
        processedReply = postprocessor.process(systemReply)

def test_process_empty():
    systemReply = ""
    processedReply = postprocessor.process(systemReply)

    assert "" == processedReply
