import pytest

# launch this test with:
# pytest -m "mt1 or mt2"

@pytest.mark.mt1
def test1():
    print('Executing test1!')
    assert True

@pytest.mark.mt2
def test2():
    print('Executing test2!')
    assert True