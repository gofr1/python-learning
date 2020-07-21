class TestClass:
    @classmethod
    def setup_class(cls):
        print("\nSetup TestClass!")
    
    @classmethod
    def teardown_class(cls):
        print("\nTeardown TestClass!")
    
    def setup_method(self, method):
        if method == self.test1:
            print('\nSetting up test1')
        elif method == self.test2:
            print('\nSetting up test2')
        else:
            print('\nSetting up unknown test')
    
    def teardown_method(self, method):
        if method == self.test1:
            print('\nTeardown test1')
        elif method == self.test2:
            print('\nTeardown test2')
        else:
            print('\nTeardown unknown test')
    
    def test1(self):
        print('Executing test1!')
        assert True
    
    def test2(self):
        print('Executing test2!')
        assert True

# unit_tests/test_xunit_style_class.py::TestClass::test1 
# Setup TestClass!

# Setting up test1
# Executing test1!
# PASSED
# Teardown test1

# unit_tests/test_xunit_style_class.py::TestClass::test2 
# Setting up test2
# Executing test2!
# PASSED
# Teardown test2

# Teardown TestClass!