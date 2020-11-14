#!/usr/bin/env python3

tr_rows = [(1,),(1,1)]

for i in range(2,8):
    sum = [1, ]
    for j in range(len(tr_rows[i-1])-1):
        sum.append(tr_rows[i-1][j] + tr_rows[i-1][j+1])
    sum.append(1)
    tr_rows.append(tuple(sum))

for r in tr_rows:
    print(' '.join(map(str,r)))