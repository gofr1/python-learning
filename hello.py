#print('hello world!')

import pyodbc

details = {
 'server' : 'localhost',
 'database' : 'tempdb',
 'username' : 'SA',
 'password' : "sl1pKN)T"
 }

connect_string = 'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'.format(**details)

try:
    connection = pyodbc.connect(connect_string)
except pyodbc.Error as ex:
    sqlstate = ex.args[1]
    print(sqlstate)
else:
    print(connection)
    cursor = connection.cursor()
    cursor.execute("select @@version as ver")
    rows = cursor.fetchall()
    for row in rows:
        print(row.ver)