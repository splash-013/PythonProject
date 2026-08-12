import pytest
@pytest.fixture()
def setup():
    print('Browser setup')
    yield
    print('Browser close')