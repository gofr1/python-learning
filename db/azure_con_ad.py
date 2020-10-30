import pyodbc, configparser

section_name = 'azure_ad'
config = configparser.ConfigParser()
c = config.read("./.env/db.conf")
db_opts = config.options(section_name)
connect_string = ''

for db_opt in db_opts:
    connect_string = connect_string + f'{db_opt}={config.get(section_name, db_opt)};'

try:
    connection = pyodbc.connect(connect_string)
except pyodbc.Error as ex:
    sqlstate = ex.args[1]
    print(sqlstate)
else:
    cursor = connection.cursor()
    cursor.execute("select @@version as ver")
    rows = cursor.fetchall()
    for row in rows:
        print(row.ver)
    connection.close()
