#!/usr/bin/env python3

class Employee():
    def __init__(self, fname, lname, level, yrsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrsService
    
    # implement comparison functions by employee level
    def __ge__(self, other):
        if self.level == other.level:
            return self.seniority >= other.seniority
        return self.level >= other.level
    
    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority
        return self.level > other.level

    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority
        return self.level < other.level

    def __le__(self, other):
        if self.level == other.level:
            return self.seniority <= other.seniority
        return self.level <= other.level

    def __eq__(self, other):
        pass


def main():
    # define some employees
    dept = []
    dept.append(Employee('Tim', 'Sims', 5, 9))
    dept.append(Employee('John', 'Doe', 4, 12))
    dept.append(Employee('Jane', 'Smith', 6, 6))
    dept.append(Employee('Rebecca', 'Robinson', 5, 13))
    dept.append(Employee('Tyler', 'Durden', 5, 12))

    # who's more senior?
    print(dept[0] > dept[2])
    print(dept[4] < dept[3])

    # sort the items
    # sorted function will use comparison we defined
    emps = sorted(dept)
    for emp in emps:
        print(emp.lname)

if __name__ == '__main__':
    main()