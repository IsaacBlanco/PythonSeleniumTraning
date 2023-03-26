# Any pytest fiel must start with "test_" or end with "test_"
# pytest  method names must start with "test"
# any code must be wrapped in the method only
# Metod name shpuld have sense
# -V verbose -S pint in logs output
# -k stands for methods name execution, run all test which has that value in method name
# run all test py.test , inside the test directory
# sun specific file test py.test "file_name"
# mark /tag /group with @pytest.mark.<<name>>
        # -m satanf for mark, to run tcs marked with specific keyword
# to skip TC you cna mark it as skip@pytest.mark.skip
# @pytest.mark.xfail run the test but skip the report ( in case tc is need for something else, but is failig)
# fixtures are used to setup and teardown methods or TCs - conftest.py file to generalize fixture and make it available for all TCs
# data driven an parameterization can be given in iteable object and return statement
# scope Class in fixture, to run one per class


import pytest


@pytest.mark.smoke
@pytest.mark.xfail
def test_firstTest(setup):
    print("Hello")

def test_secondTestRegression(setup):
    print("Automations WOW!!!")
