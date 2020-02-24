import pyodbc, configparser

section_name = 'mssql_local'
config = configparser.ConfigParser()
c = config.read("./.env/db.conf")
db_opts = config.options(section_name)
details = dict()

for db_opt in db_opts:
    details[db_opt] = config.get(section_name, db_opt)

connect_string = 'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'.format(**details)

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
    connection.close()
