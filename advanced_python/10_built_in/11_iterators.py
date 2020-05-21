#!/usr/bin/env python3

def main():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    daysFr = ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"]
    
    # iter 
    i = iter(days)
    print(next(i))
    
    # iterate using a function and a sentinel
    with open("testfile.txt", "r") as fi:
        for line in iter(fi.readline, ''):
            print(line)
    
    # use regular iteration
    for day in days:
        print(day)
    
    # or
    for m in range(len(days)):
        print(m+1, days[m])
    
    # or w/enumerate
    for num, val in enumerate(days, start=1):
        print(num, val)
    
    # use zip to combine sequences
    # terminates when smaller sequence is exhausted
    for m in zip(days, daysFr):
        print(m)
    
    for i, m in enumerate(zip(days, daysFr), start=1):
        print(i,m)

if __name__ == '__main__':
    main()