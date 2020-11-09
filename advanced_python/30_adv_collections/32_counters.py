#!/usr/bin/env python3

# Counter allows us to count the occurrences of a particular item.
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
    #* 2

    # how many students are in class 1
    print(sum(c1.values()), "student in class 1")
    #* 12 student in class 1

    # combine the two classes
    c1.update(class2)
    print(sum(c1.values()), "student in class 1&2")
    #* 24 student in class 1&2

    # what's the most common name in classes
    print(c1.most_common(3))
    #* [('James', 3), ('Frank', 2), ('Bob', 1)]

    # separate the classes again
    c1.subtract(class2)
    print(c1.most_common(3))
    #* [('James', 2), ('Bob', 1), ('Becky', 1)]

    # what's common between the two classes
    print(c1 & c2)
    #* Counter({'Frank': 1, 'James': 1})

    # count the number of individual favourite colours
    colours = (
        ('John', 'Yellow'),
        ('Jack', 'Blue'),
        ('Jack', 'Green'),
        ('Silvia', 'Black'),
        ('John', 'Red'),
        ('Jane', 'Silver'),
    )

    favs = Counter(name for name, colour in colours)
    print(favs)
    #* Counter({'John': 2, 'Jack': 2, 'Silvia': 1, 'Jane': 1}

if __name__ == '__main__':
    main()