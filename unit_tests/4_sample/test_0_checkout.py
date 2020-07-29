# Cab create instance of Checkout class
# Can add item price
# Can add an item
# Can calculate the current total
# Can add multiple items and get correct total
# Can add discount rules
# Can apply discount rules to the total
# Exception is thrown for item added w/o a price

import pytest
from checkout import Checkout

# as we are instanciating Checkout class in every test
# let's create a fixture
@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice('a', 1)
    checkout.addItem('a')
    return checkout
# instaed of this test
# def test_CanInstanciateCheckout():
#     co = Checkout()

# as both this tests are implemented in 
# the test_CanCalculateTotal we can delete them
#
# def test_CanAddItemPrice(checkout):
#     checkout.addItemPrice('a', 1)
#
# def test_CanAddItem(checkout):
#     checkout.addItem('a')

def test_CanCalculateTotal(checkout):
    assert checkout.calculateTotal() == 1

def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItemPrice('b', 2)
    checkout.addItem('b')
    assert checkout.calculateTotal() == 3

def test_CanAddDiscountRile(checkout):
    checkout.addDiscount('a', 3, 2)

# @pytest.mark.skip # to skip test
def test_CanApplyDiscountRule(checkout):
    checkout.addDiscount('a', 3, 2)
    checkout.addItem('a')
    checkout.addItem('a')
    assert checkout.calculateTotal() == 2

def test_ExceptionWithBadItemPrice(checkout):
    with pytest.raises(Exception):
        checkout.addItem('c')