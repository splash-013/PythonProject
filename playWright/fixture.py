# Fixture is a reusable function which can be executed before a TC
import pytest

@pytest.fixture #this is used to define a fixture
def setup():
    print('This is setup')

def test_example1(setup):
    print('First statement')
def test_example2(setup):
    print('Second statement')



