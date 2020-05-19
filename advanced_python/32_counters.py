#!/usr/bin/env python3

from collections import Counter

def main():
    # list of students in class 1
    class1 = ['Bob', 'Becky', 'Chad', 'Darcy', 'Frank', 'Hannah', 'Kevin',
              'James', 'James', 'Melanie', 'Penny', 'Steve']
    
    # list of students in class 2
    class2 = ['Bill', 'Barry', 'Cindy', 'Debbie', 'Frank', 'Gabby', 'Kelly',
              'James', 'Joe', 'Sam', 'Tara', 'Ziggy']
    
    # create a counter for class1 and class2
    c1 = Counter(class1)
    c2 = Counter(class2)

    # how many students in class 1 named James?
    print(c1['James'])

    # how many students are in class 1
    print(sum(c1.values()), "student in class 1")

    # combine the two classes
    c1.update(class2)
    print(sum(c1.values()), "student in class 1&2")
    
    # what's the most common name in classes
    print(c1.most_common(3))

    # separate the classes again
    c1.subtract(class2)
    print(c1.most_common(3))

    # what's common between the two classes
    print(c1 & c2)

if __name__ == '__main__':
    main()