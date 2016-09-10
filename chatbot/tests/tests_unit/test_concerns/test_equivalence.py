import py.test
from concerns.equivalence import EquivalenceClasses

def test_init_and_getitem():
    d = EquivalenceClasses(a=1, b=2)

    assert 1 == d['a']
    assert 2 == d['b']

def test_setgetitem():
    d = EquivalenceClasses()

    d['c', 'd'] = 3
    assert 3 == d['c']
    assert 3 == d['d']

def test_fromdict():
    dictionary = { ('a', 'b'): 1}

    d = EquivalenceClasses.from_dict(dictionary)

    assert 1 == d['a']
    assert 1 == d['b']

    # change 'a'
    d['a'] = 2

    # change affects 'b'
    assert 2 == d['b']
