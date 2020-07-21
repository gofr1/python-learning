import pytest

# launch this test with:
# pytest -m "mt1 or mt2" unit_tests/

@pytest.mark.mt1
def test1():
    print('Executing test1!')
    assert True

@pytest.mark.mt2
def test2():
    print('Executing test2!')
    assert True

# this will run all test2 tests
# pytest -v -s -k "test2" unit_tests/

