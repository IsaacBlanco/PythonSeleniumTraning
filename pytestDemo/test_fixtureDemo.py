# fixtures are methods that will execute before or after test
# to define a fixture needs @pytest.fixture()
# then the method name
# what is inside fixture method will execute before the test
# add "yield" keyword to add before test methods
# send fixture method as a parameter for the testcase

import pytest


@pytest.mark.smoke
def test_firstTest(setup):
    print("Hello printin from test")


#@pytest.fixture()
#def setup():
#    print("This will execute fisrt beofre test")
#    yield
#    print("this will execute last after test")