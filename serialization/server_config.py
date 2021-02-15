#!/usr/bin/env python3
# Contains an example of server configuration 
# for loading with the help of exec

import logging, sys
from os import environ

api_key = environ.get('API_KEY')
log_level = logging.INFO
port = 8888

if sys.platform == 'win32':
    num_workers = 10
else:
    num_workers = 100

# Clean up namespace
del environ
del logging
del sys