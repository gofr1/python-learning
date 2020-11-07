#!/usr/bin/env python3

from collections import defaultdict
import json

def main():
    # define a list of items we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']
    
    fruitCounter = {}
    
    for fruit in fruits:
        fruitCounter.setdefault(fruit, 0)
        fruitCounter[fruit] +=1
    
    print(fruitCounter)

    # with defaultdict

    fruitCounter = defaultdict(int)

    for fruit in fruits:
        fruitCounter[fruit] +=1
       
    print(fruitCounter)

    # but if you call a key-value that is not in dictionary
    # it will return with default value
    print(fruitCounter['tomato']) # 0

    # and it will be added to default dictionary
    print(fruitCounter)

    some_dict = {}
    some_dict['colours']['favourite'] = "yellow"
    
    # Unlike dict, with defaultdict you do not need to check whether a key is present or not
    tree = lambda: defaultdict(tree)
    some_dict = tree()
    some_dict['colours']['favourite'] = "yellow"
    print(json.dumps(some_dict))

if __name__ == '__main__':
    main()