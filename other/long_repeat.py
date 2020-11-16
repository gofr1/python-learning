#!/usr/bin/env python3

# find the maximum number of same charecters in a string, that goes one by one

def long_repeat(strng):
    if len(strng) == 1:
        return 1

    d = {}
    n = 1
    
    for i in range(len(strng)-1):
        if strng[i] == strng[i+1]:
            prev = strng[i-1]
            cur = strng[i]

            if cur in d.keys() and prev != cur:
                new_key = cur + str(n)
                d[new_key] = d[cur]
                del d[cur]
                n += 1

            d.setdefault(strng[i], 1)
            d[cur] += 1

    result = max(d.items(), key = lambda x: x[1])
    return result[0][:1], result[1]
            
print(long_repeat('asdffffaasaaa'))
#* ('f', 4)
print(long_repeat('fffasaaalllllaa'))
#* ('l', 5)
print(long_repeat('agggggggggggsdfffggggjjjjjklnmmmmmmgjkgggjjgggggggggg'))
#* ('g', 11)