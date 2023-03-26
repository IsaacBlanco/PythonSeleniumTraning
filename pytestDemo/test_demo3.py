import pytest


@pytest.mark.smoke
def test_fivethTest():
    a = 4
    b = 6
    assert a < b, "no correct"

def test_sixthTestRegression():
    a = 4
    b = 6
    assert  b + a == 10, "no equal"