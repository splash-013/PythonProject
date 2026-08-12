# ordering the TC to execute, install pytest-ordering
import pytest

# Approach 1
@pytest.mark.order(3)
def test_login03():
    print('Login 03')
    assert 1 == 1


@pytest.mark.order(2)
def test_login02(setup): #setup fixture
    print('Login 02')


@pytest.mark.order(1)
def test_login01():
    print('Login 01')

# Approach 2
# @pytest.mark.order(before='test_login04')
# def test_login03():
#     print('Login 03')
#     assert 1 == 1
#
#
# @pytest.mark.order(after='test_login01')
# def test_login02(): #setup fixture
#     print('Login 02')
#
#
# @pytest.mark.order(1)
# def test_login01():
#     print('Login 01')
#
# @pytest.mark.order(after='test_login03')
# def test_login04():
#     print('Login 04')