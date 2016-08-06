import pytest
from botcontroller.concerns import Concerns
from botcontroller.concerns import ConcernsFactory

def test_getitem():
    concern_for_id0 = ConcernsFactory.getConcerns("id0")

    assert concern_for_id0 is ConcernsFactory.getConcerns("id0")

def test_getConcerns():
    someuserconcenrs = ConcernsFactory.getConcerns("someuserid")
    someDIFFERENTconcerns = ConcernsFactory.getConcerns("someDIFFERENTuserid")

    assert someuserconcenrs is not someDIFFERENTconcerns
    assert someuserconcenrs != someDIFFERENTconcerns

def test_setSomeConcernsForOneUserAndSomeForAnother():
    useroneConcerns = ConcernsFactory.getConcerns("userone")
    usertwoConcerns = ConcernsFactory.getConcerns("usertwo")

    useroneConcerns["respiratory"] = 5
    usertwoConcerns["family"] = 10

    assert useroneConcerns["family"] is None
    assert usertwoConcerns["respiratory"] is None
