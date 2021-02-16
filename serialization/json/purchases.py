"""Shopping events"""
from datetime import datetime

event = {'purchases': [{
   'name': 'John Doe',
   'purchase date': datetime(2021, 2, 15, 10, 8, 15, 561),
   'items': [{
       'item': 'Beer',
       'amount': 6,
       'price': 2.99
    }, {
       'item': 'Bread',
       'amount': 2,
       'price': 1.95
    }, {
       'item': 'Water',
       'amount': 5,
       'price': 0.54
    }]
    },{
   'name': 'Jack Holmes',
   'purchase date': datetime(2021, 2, 10, 8, 19, 34, 786),
   'items': [{
       'item': 'Snack',
       'amount': 10,
       'price': 1.95
    }, {
       'item': 'Soda',
       'amount': 4,
       'price': 1.37
    }]
    }
]
}