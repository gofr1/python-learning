#!/usr/bin/env python3

def main():
    list1 = [1, 2, 3, 0, 5, 6]
    list2 = [1, 2, 3, 4, 5, 6]
    
    # any - will return true if any of the sequence values are true
    print(any(list1))

    # all - will evaluate true only if all values are true
    print(all(list1))
    print(all(list2))
    
    # min, max and sum
    print(min(list1))
    print(max(list1))
    print(sum(list1))

    # for strings
    str_list = ['abc', 'bcd', 'zxy', 'acb', 'zyx' ,'efg']

    print(min(str_list))
    print(max(str_list))

if __name__ == '__main__':
    main()