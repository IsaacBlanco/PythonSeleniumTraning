import pytest


@pytest.mark.usefixtures("setup")
class TestClassLevelExample:

    def test_fixtureInClass0(self):
        print("execute steps in fixture using class level fixture 0")

    def test_fixtureInClass1(self):
        print("execute steps in fixture using class level fixture 1")

    def test_fixtureInClass2(self):
        print("execute steps in fixture using class level fixture 2")

    def test_fixtureInClass3(self):
        print("execute steps in fixture using class level fixture 3")

    def test_fixtureInClass4(self):
        print("execute steps in fixture using class level fixture 4")

    def test_fixtureInClass5(self):
        print("execute steps in fixture using class level fixture 5")
