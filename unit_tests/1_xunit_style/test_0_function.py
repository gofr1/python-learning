
def setup_module(module):
    print("\nSetup module!")

def teardown_module(module):
    print("\nTeardown module!")

def setup_function(function):
    if function == test1:
        print('\nSetting up test1')
    elif function == test2:
        print('\nSetting up test2')
    else:
        print('\nSetting up unknown test')

def teardown_function(function):
    if function == test1:
        print('\nTeardown test1')
    elif function == test2:
        print('\nTeardown test2')
    else:
        print('\nTeardown unknown test')

def test1():
    print('Executing test1!')
    assert True

def test2():
    print('Executing test2!')
    assert True

# Setup module!

# Setting up test1
# Executing test1!
# PASSED
# Teardown test1

# unit_tests/test_xunit_style.py::test2 
# Setting up test2
# Executing test2!
# PASSED
# Teardown test2

# Teardown module!