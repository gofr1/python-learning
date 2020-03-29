#!/usr/bin/env python3

import sqlite3

def main():
    print('connect')
    db = sqlite3.connect('db_api.db') # will return a database handle
    cur = db.cursor()
    
    print('create')
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("CREATE TABLE test (id integer PRIMARY KEY, string TEXT, number INTEGER)")

    print('insert rows')
    cur.execute("INSERT INTO test (string, number) VALUES ('one', 1)")
    cur.execute("INSERT INTO test (string, number) VALUES ('two', 2)")
    cur.execute("INSERT INTO test (string, number) VALUES ('three', 3)")

    print('commit')
    db.commit()

    print('count')
    cur.execute("SELECT COUNT(*) FROM test")
    count = cur.fetchone()[0]
    print(f'there are {count} rows in the table')

    print('read')
    for row in cur.execute("SELECT * FROM test"):
        print(row)
    
    print('drop')
    cur.execute("DROP TABLE test")

    print('close')
    db.close()

if __name__ == '__main__':
    main()