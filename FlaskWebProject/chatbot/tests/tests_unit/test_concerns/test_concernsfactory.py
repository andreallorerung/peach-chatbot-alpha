import pytest
from concerns.drive_conversation import DistressConversationDriver
from concerns.concern_factory import UserConcernsFactory

def test_getUserConcerns():
    someuserconcerns = UserConcernsFactory.getUserConcerns("someuserid")
    someDIFFERENTconcerns = UserConcernsFactory.getUserConcerns("someDIFFERENTuserid")

    assert someuserconcerns is not someDIFFERENTconcerns
    assert someuserconcerns != someDIFFERENTconcerns

def test_setSomeUserConcernsForOneUserAndSomeForAnother():
    useroneUserConcerns = UserConcernsFactory.getUserConcerns("userone")
    usertwoUserConcerns = UserConcernsFactory.getUserConcerns("usertwo")

    useroneUserConcerns.setInitialUserConcerns({"respiratory": 5})
    usertwoUserConcerns.setInitialUserConcerns({"family": 10})

    with pytest.raises(KeyError):
        useroneUserConcerns.userConcerns["family"]
    with pytest.raises(KeyError):
        usertwoUserConcerns.userConcerns["respiratory"]
