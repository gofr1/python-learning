import pytest

# or we can use @pytest.fixture(autouse=True)
# to use fixture for all tests
@pytest.fixture()
def setup():
    print('\nSetup!')

def test1(setup):
    print('\nExecuting test1')
    assert True

@pytest.mark.usefixtures("setup")
def test2():
    print('\nExecuting test2')
    assert True

