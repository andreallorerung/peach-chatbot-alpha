from botinterface.postprocessor_example import MessagePostprocessorExample

postprocessor = MessagePostprocessorExample()

def test_init():

    assert postprocessor is not None

def test_parse():

    output = "You can find more information here: {{ query.keyword='cats' }}"

    actual = postprocessor._parse(output)
    expected = "query.keyword='cats'"

    assert expected == actual

def test_query():

    keyword = "dogs"

    actual = postprocessor._query(keyword)
    expected = "http://dogs.com"

    assert expected == actual

def test_readkeyword():
    command = "query.keyword='cats'"

    expected = "cats"
    actual = postprocessor._readKeyword(command)

    assert expected == actual

def test_postprocess():

    output = "You can find more information here: {{ query.keyword='cats' }}"

    expected = "http://cats.com"
    actual = postprocessor.process(output)

    assert expected == actual
