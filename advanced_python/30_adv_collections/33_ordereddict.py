#!/usr/bin/env python3

from collections import OrderedDict

def main():
    # list of sport teams with wins and losses
    sportTeams = [('Royals', (18,12)), ('Rockets', (24,6)),
                  ('Cardinals', (20,10)), ('Dragons', (22,8)),
                  ('Kings', (15,15)), ('Chargers', (20,10)),
                  ('Jets', (16,16)), ('Warriors', (25,5))]
    
    # sort the teams by number of wins
    sortedTeams = sorted(sportTeams, key= lambda t: t[1][0], reverse=True)

    # create an ordered dictionary of the teams
    teams = OrderedDict(sortedTeams)
    print(teams)
    
    # use popitem to remove the top item
    tm, wl = teams.popitem(False)
    print("Top team:", tm, wl)
    
    # what are next the top 4 teams
    for i, team in enumerate(teams, start=1):
        print(i, team)
        if i == 4:
            break
    
    # test for equality
    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "b": 2, "c": 3})
    print("Equality test:", a==b) # True

    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "c": 3, "b": 2})
    print("Equality test:", a==b) # False

    # if you compare to dictionaries with same elements in different order
    # they will be equal
    a = {"a": 1, "b": 2, "c": 3}
    b = {"a": 1, "c": 3, "b": 2}
    print("Equality test (dict):", a==b) # False

    # OrderedDict keeps its entries sorted as they are initially inserted. 
    # Overwriting a value of an existing key doesn’t change the position of that key. 
    # However, deleting and reinserting an entry moves the key to the end of the dictionary.
    colours = OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])
    for key, value in colours.items():
        print(key, value)

    # in the default dictionary the position of keys is not guaranteed:
    colours =  {"Red" : 198, "Green" : 170, "Blue" : 160}
    for key, value in colours.items():
        print(key, value)

if __name__ == '__main__':
    main()