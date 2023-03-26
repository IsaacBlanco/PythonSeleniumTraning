import pytest

from pytestDemo.BaseClass import BaseClass


#when fixture return data and you need it in a TC then you need to add that fixture as an argument
@pytest.mark.usefixtures("dataLoad")
class TestFixtureData(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(type(dataLoad))
        log.info(dataLoad)

        assert dataLoad[2] == "shiro", "strings doesnt now match"
        log.info(dataLoad[2])
        #print(type(dataLoad))
        #print(dataLoad)
        #print(dataLoad[2])

    def test_crossBrowser(self, crossBrowser):
        log = self.getLogger()
        log.info(crossBrowser)
        print(crossBrowser)

    def test_crossBrowserMultiple(self, crossBrowserMultiple):
        log = self.getLogger()
        log.info(crossBrowserMultiple)
        print(crossBrowserMultiple)
        print(crossBrowserMultiple[0])
        print(crossBrowserMultiple[1])
        print(crossBrowserMultiple[2])