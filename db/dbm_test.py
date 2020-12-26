#!/usr/bin/env python3

import dbm

# write to Unix DB file
with dbm.open('test.db', 'c') as db:
    # filename and 'c' for write/read/create
    db['key0'] = 'Value A'
    db['key1'] = 'Value B'

# read from Unix DB file
with dbm.open('test.db', 'r') as db:
    print(db['key0'])
    print(db['key1'])