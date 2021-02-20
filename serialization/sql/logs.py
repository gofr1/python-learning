import sqlite3
from random import choice
from datetime import datetime, timedelta

# use :memory: for in memory db, great for testing
db = sqlite3.connect('logs.db')

# create the table
with open('schema.sql', 'r') as fp:
    schema_sql = fp.read()
db.executescript(schema_sql)
db.commit()

# generate some random data ...
cur = db.cursor()
now = datetime.now()
insert_sql = 'INSERT INTO logs (time, level, message) VALUES (?, ?, ?);'
# ... and write it into db
for i in range(10_000):
    time = now - timedelta(seconds=i)
    level = choice(['ERROR', 'WARNING', 'ERROR'])
    message = f'log message #{i}'
    cur.execute(insert_sql, (time, level, message))
db.commit()

# read data from db
db.row_factory = sqlite3.Row # access column by name
cur = db.cursor()
query_sql = 'SELECT time, level, message FROM logs LIMIT 50;'
for row in cur.execute(query_sql):
    print(dict(row))
#* {'time': '2021-02-20 13:56:39.077153', 'level': 'ERROR', 'message': 'log message #0'}
#* {'time': '2021-02-20 13:56:38.077153', 'level': 'WARNING', 'message': 'log message #1'}
#* {'time': '2021-02-20 13:56:37.077153', 'level': 'ERROR', 'message': 'log message #2'}
#* ...
#* {'time': '2021-02-20 13:55:51.077153', 'level': 'ERROR', 'message': 'log message #48'}
#* {'time': '2021-02-20 13:55:50.077153', 'level': 'ERROR', 'message': 'log message #49'}


