# Fixture is a reusable function which can be executed before a TC
import pytest

@pytest.fixture #this is used to define a fixture, this contains steps to launch and exit browser
def setup(): #setup/launch browser
    print('Setup browser')
    yield #close/exit the browser after executing test functions
    print('Close browser')

def test_example1(setup):
    print('First statement execution')
def test_example2(setup):
    print('Second statement execution')



