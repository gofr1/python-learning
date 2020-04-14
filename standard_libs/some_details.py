#!/usr/bin/env python3

def main():
    # when compairing the strings
    # a->z 1->26
    # so 
    print("a" > "b")
    # will be False because 1 is not greater then 2
    print("b" > "a")
    # will result in True 2 > 1
    print("Jenny" > "Jennifer")
    # will result in True because "Jenn" is the same in both words but "y" > "i"
    
    print("a" > "A") # True
    print("z" > "A") # True

    # same goes to min and max
    print(min("Kathryn", "Katie")) # Kathryn as h > i
    print(max("Kathryn", "Katie")) # Katie as h < i

    # sorting 
    children = ["Sue", "jerry", "linda"]
    print(sorted(children)) # ['Sue', 'jerry', 'linda']
    print(sorted(children, key=str.upper)) # ['jerry', 'linda', 'Sue']

    print(sorted("a B c D e F".split())) #['B', 'D', 'F', 'a', 'c', 'e']
    print(sorted("a B c D e F".split(), key=str.upper)) # ['a', 'B', 'c', 'D', 'e', 'F']
    print(sorted("a B c D e F".split(), key=str.lower)) # ['a', 'B', 'c', 'D', 'e', 'F']

    # lambda & sorted
    students = {("alice", "B", 12), ("eliza", "A", 16), ("tae", "C", 15)}
    print(sorted(students, key = lambda student:student[0]))
    print(sorted(students, key = lambda student:student[1]))

if __name__ == '__main__':
    main()