#!/usr/bin/env python3

import pyodbc
import configparser
import asyncio
from random import randint
# from sys import maxsize

section_name = 'mssql_local'
config = configparser.ConfigParser()
c = config.read("./.env/db.conf")
db_opts = config.options(section_name)
details = dict()

for db_opt in db_opts:
    details[db_opt] = config.get(section_name, db_opt)

details['database'] = 'DEMO'

connect_string = 'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={uid};PWD={pwd}'.format(**details)

async def write_to_db(connect_string, number):
    try:
        connection = pyodbc.connect(connect_string)
    except pyodbc.Error as ex:
        sqlstate = ex.args[1]
        print(sqlstate)
    else:
        cursor = connection.cursor()
        query = f'insert into TestAsync(randomNumber) values (?)'
        #value = randint(0,maxsize)
        for value in range(randint(1, 10)):
            await asyncio.sleep(1)
            value += number
            count = cursor.execute(query, value).rowcount
            connection.commit()
            print(f'Rows inserted: {str(count)}, Value: {value}')
        connection.close()
    


async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        *[write_to_db(connect_string, i) for i in range(10,50,10)]
    )

asyncio.run(main())
#* Rows inserted: 1, Value: 10
#* Rows inserted: 1, Value: 20
#* Rows inserted: 1, Value: 30
#* Rows inserted: 1, Value: 40
#* Rows inserted: 1, Value: 11
#* Rows inserted: 1, Value: 21
#* Rows inserted: 1, Value: 41
#* Rows inserted: 1, Value: 12
#* Rows inserted: 1, Value: 22
#* Rows inserted: 1, Value: 42
#* Rows inserted: 1, Value: 13
#* Rows inserted: 1, Value: 23
#* Rows inserted: 1, Value: 43
#* Rows inserted: 1, Value: 24
#* Rows inserted: 1, Value: 44
#* Rows inserted: 1, Value: 25
#* Rows inserted: 1, Value: 26
#* Rows inserted: 1, Value: 27