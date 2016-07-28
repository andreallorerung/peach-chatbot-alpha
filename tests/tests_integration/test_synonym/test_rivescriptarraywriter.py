from synonym.rivescript_writer import RivescriptArrayWriter
from synonym.rivescript_array import RivescriptArray

FILEPATH = "tests/tests_integration/test_synonym/generated_array.rive"

def test_write():
    # perform
    array = RivescriptArray("faith", ["belief","church","holy"])
    RivescriptArrayWriter.writetofile(FILEPATH, 'w', array)

    # assert file content is as expected
    with open(FILEPATH, 'r') as f:
        line = f.readline()
        assert "! array faith = belief|church|holy\n" == line

def test_write_many():
    # perform
    arrays = [RivescriptArray("faith", ["belief","church","holy"]),
            RivescriptArray("partner", ["wife","husband","lover"]),
            RivescriptArray("nausea", ["queasy","throw up","sick"])]

    RivescriptArrayWriter.writetofile(FILEPATH, 'w', *arrays)

    # assert file content is as expected
    expected = ["! array faith = belief|church|holy\n",
                "! array partner = wife|husband|lover\n",
                "! array nausea = queasy|throw up|sick\n"]

    with open(FILEPATH, 'r') as f:
        lines = f.readlines()

    assert expected == lines
