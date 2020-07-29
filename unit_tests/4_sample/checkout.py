class Checkout:
    
    class Discount:
        def __init__(self, numberOfItems, price):
            self.numberOfItems = numberOfItems
            self.price = price
        
    def __init__(self):
        self.prices = {}
        self.items = {}
        self.discounts = {}

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.prices:
            raise Exception('Item has no price')

        if item in self.items:
            self.items[item] += 1
        else:
         self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.calculateItemTotal(item, cnt)
        return total
    
    def addDiscount(self, item, numberOfItems, price):
        discount = self.Discount(numberOfItems, price)
        self.discounts[item] = discount
    
    def calculateItemTotal(self, item, cnt):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.numberOfItems:
                total += self.calculateItemDiscountedTotal(item, cnt, discount)
            else:
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt
        return total
    
    def calculateItemDiscountedTotal(self, item, cnt, discount):
        total = 0
        numberOfItems = cnt/discount.numberOfItems
        total += numberOfItems * discount.price
        remaining = cnt%discount.numberOfItems
        total += remaining * self.prices[item]
        return total