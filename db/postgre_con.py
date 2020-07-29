import psycopg2, configparser

section_name = 'postgre_local'
config = configparser.ConfigParser()
c = config.read("./.env/db.conf")
db_opts = config.options(section_name)
con_param = dict()

for db_opt in db_opts:
    con_param[db_opt] = config.get(section_name, db_opt)

connect_string = 'dbname={database} user={user} password={password} port={port} host={host}'.format(**con_param)
# connection = psycopg2.connect(user = "user",
#                               password = "password",
#                               host = "127.0.0.1",
#                               port = "5432",
#                               database = "db")

try:
    connection = psycopg2.connect(connect_string)
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
else:
    cursor = connection.cursor()
    print (connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

    # cursor.execute('SELECT * FROM "language";')
    # rows = cursor.fetchall()
    # for row in rows:
    #     print("languageid = ", row[0], end = ';')
    #     print("name = ", row[1], end=';')
    #     print("last_updated = ", row[2])

    connection.close()