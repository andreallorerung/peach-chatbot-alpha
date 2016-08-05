from synonym.rivescript_array import RivescriptArray

def test_formatarray():
    expected = "! array faith = belief|church|holy"
    actual = RivescriptArray.formatArray("faith", ["belief","church","holy"])

    assert expected == actual

def test_str():
    rivescriptarray = RivescriptArray("faith", ["belief","church","holy"])

    expected = "! array faith = belief|church|holy"
    actual = str(rivescriptarray)

    assert expected == actual
