import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_thirdTest():
    assert 2 == 1, "no queal"

def test_fourthTestRegression():
    a = 4
    b = 6
    assert a + 2 == b, "no queal"