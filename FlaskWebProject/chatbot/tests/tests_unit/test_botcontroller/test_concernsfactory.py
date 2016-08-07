import pytest
from botcontroller.concerns import UserConcerns
from botcontroller.concerns import UserConcernsFactory

def test_getitem():
    concern_for_id0 = UserConcernsFactory.getUserConcerns("id0")

    assert concern_for_id0 is UserConcernsFactory.getUserConcerns("id0")

def test_getUserConcerns():
    someuserconcenrs = UserConcernsFactory.getUserConcerns("someuserid")
    someDIFFERENTconcerns = UserConcernsFactory.getUserConcerns("someDIFFERENTuserid")

    assert someuserconcenrs is not someDIFFERENTconcerns
    assert someuserconcenrs != someDIFFERENTconcerns

def test_setSomeUserConcernsForOneUserAndSomeForAnother():
    useroneUserConcerns = UserConcernsFactory.getUserConcerns("userone")
    usertwoUserConcerns = UserConcernsFactory.getUserConcerns("usertwo")

    useroneUserConcerns["respiratory"] = 5
    usertwoUserConcerns["family"] = 10

    assert useroneUserConcerns["family"] is None
    assert usertwoUserConcerns["respiratory"] is None
