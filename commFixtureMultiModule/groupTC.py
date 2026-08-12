# grouping by smoke, regression, smoke+regression
# for user defined decorators create a pytest.ini file and define the UD groups(smoke, regression) to avoid warnings
# to run specific group of decorator, terminal -> pytest commFixtureMultiModule/groupTC.py -s -v -m 'smoke'
# run test for both smoke and regression, terminal -> pytest commFixtureMultiModule/groupTC.py -s -v -m 'smoke and regression', use and operator
import pytest


@pytest.mark.skip  # decorator to skip the TC
def test_login01():
    print('Login 01')

@pytest.mark.smoke
@pytest.mark.regression
def test_login02(setup):
    print('Login 02')

@pytest.mark.smoke
def test_login03():
    print('Login 03')
    assert 1 == 1

@pytest.mark.regression
def test_login04(setup):
    print('Login 04')

@pytest.mark.skip
def test_login05():
    print('Login 05')

@pytest.mark.smoke
@pytest.mark.regression
def test_login06():
    print('Login 06')


def test_login07():
    print('Login 07')
