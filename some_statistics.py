#!/usr/bin/env python3

import statistics

def main():
    # Some random data
    agesData = [10, 13, 14, 12, 11, 10, 11, 10, 15]

    # Statistics Definitions
    # given [2, 2, 3]
    # Mean - average = (2+2+3)/3 = 2.333
    # Median - midpoint = 2
    # Mode - most frequent value = 2
    print(statistics.mean(agesData))
    print(statistics.median(agesData))
    print(statistics.mode(agesData))

    # Advanced Statistics
    # given [2, 2, 3]
    # Variance - the average of squared differences
    # from the mean 
    # ((2-2.333)**2 + (2-2.333)**2 + (3-2.333)**2)/(3-1) = 0.333
    # the greater number shows the greater variance of data
    # Standard Deviation - the square root ogf the variance
    # sqrt(0.333) = .57735
    print(statistics.variance(agesData))
    print(statistics.stdev(agesData))

    # Variance
    s = 0
    for i in agesData:
        s += (i - (sum(agesData)/len(agesData)))**2
    print(s/(len(agesData)-1))

if __name__ == '__main__':
    main()