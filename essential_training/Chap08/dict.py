#!/usr/bin/env python3

def main():
    # animals = {'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr', 
    # 'giraffe': 'I am a giraffe!', 'dragon': 'rawr'} # associative arrays
    animals = dict(kitten = 'meow', puppy = 'ruff!', lion = 'grrr', 
    giraffe = 'I am a giraffe!', dragon = 'rawr')

    print(animals['lion'])
    animals['lion'] = 'GRRR!' # change

    animals['monkey'] = 'haha' # add
    
    # chaeck if key is in dictionary
    print('lion' in animals)

    # get a value
    print(animals.get('godzilla')) # None
    print(animals.get('monkey')) # haha

    for k, v in animals.items(): # keys, values to iterate through items
        print(f'{k} = {v}')

    print_dict(animals)    

def print_dict(o):
    for x in o:
        print(f'{x}: {o[x]}')

if __name__ == '__main__':
    main()