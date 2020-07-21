from pytest import raises

def raiseValueException():
    raise ValueError

def test_exception():
    with raises(ValueError):
        raiseValueException()