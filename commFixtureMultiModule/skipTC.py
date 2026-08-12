import pytest

@pytest.mark.skip #decorator to skip the TC
def test_login01():
    print('Login 01')


def test_login02(setup):
    print('Login 02')

@pytest.mark.skip
def test_login03():
    print('Login 03')


def test_login04(setup):
    print('Login 04')


def test_login05():
    print('Login 05')

@pytest.mark.skip
def test_login06():
    print('Login 06')


def test_login07():
    print('Login 07')
