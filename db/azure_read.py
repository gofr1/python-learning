import pyodbc, configparser

section_name = 'azure_main'
config = configparser.ConfigParser()
c = config.read("./.env/db.conf")
db_opts = config.options(section_name)
details = dict()

for db_opt in db_opts:
    details[db_opt] = config.get(section_name, db_opt)

connect_string = 'DRIVER={driver};SERVER={server};PORT={port};DATABASE={database};UID={uid};PWD={pwd}'.format(**details)

try:
    connection = pyodbc.connect(connect_string)
except pyodbc.Error as ex:
    sqlstate = ex.args[1]
    print(sqlstate)
else:
    print(connection)
    cursor = connection.cursor()
    cursor.execute("""select SCHEMA_NAME(schema_id) AS schema_name, name AS table_name from sys.tables""")
    rows = cursor.fetchall()

    for column in cursor.columns():
        print ("%s <%s>" % (column.column_name, column.type_name))

    for row in rows:
        print(f'{row.schema_name}.{row.table_name}')
    connection.close()