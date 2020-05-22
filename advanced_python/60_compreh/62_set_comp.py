#!/usr/bin/env python3

def main():
    # define a list of temperature data points
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

    # build a list of unique Farenheit temperatures
    ftemps1 = [(t*9/5)+32 for t in ctemps]
    print(ftemps1)
    
    # build a set of unique Farenheit temperatures
    ftemps2 = {(t*9/5)+32 for t in ctemps}
    print(ftemps2)

    # built a set from an input source 
    sTemp = 'The quick brown fox jumped over the lazy dog'
    chars = {c.upper() for c in sTemp if not c.isspace()}
    print(chars)

if __name__ == '__main__':
    main()