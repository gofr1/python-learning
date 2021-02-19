import yaml # is slower than json and other formats

with open('config.yml', 'r') as fp:
    config = yaml.safe_load(fp)

print(config)
#* {'api_host': 'app.example.com',
#*   'auth_server': 
#*     {'host': 'api_host', 'port': 8787}, 
#*   'db_server': 
#*     {'host': 'db.example.com', 'port': 9898, 'user': 'dbu', 'passwrd': 's3cr3t'}, 
#*   'log_server': 
#*   {'host': 'app.example.com', 'port': 9797, 'endpoint': '/log'}}

print(yaml.safe_dump(config))
#* api_host: app.example.com
#* auth_server:
#*   host: api_host
#*   port: 8787
#* db_server:
#*   host: db.example.com
#*   passwrd: s3cr3t
#*   port: 9898
#*   user: dbu
#* log_server:
#*   endpoint: /log
#*   host: app.example.com
#*   port: 9797

with open('config2.yml', 'w') as out:
    yaml.safe_dump(config, out)