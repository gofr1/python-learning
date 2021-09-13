#!/usr/local/bin/python3.9

import sys

v = sys.version_info
print('Python version {}.{}.{}'.format(*v))

# Dictionary Merge & Update
# Merge (|) and update (|=) operators
x = {"one": 1, "two": 2}
y = {"three": 3, "four": 4}
z = {"five": 5}

x|y
#* {'one': 1, 'two': 2, 'three': 3, 'four': 4}
y|x
#* {'three': 3, 'four': 4, 'one': 1, 'two': 2}

z |= x
z
#* {'five': 5, 'one': 1, 'two': 2}
z |= y
z
#* {'five': 5, 'one': 1, 'two': 2, 'three': 3, 'four': 4}

# New String Methods to Remove Prefixes and Suffixes
smth = 'SomeThing'

smth.removeprefix('Some')
#* 'Thing'

smth.removesuffix('Thing')
#* 'Some'

# Type Hinting Generics in Standard Collections
def greet_all(names: list[str]) -> None: # we can declare that we need list of string f.e.
    for name in names:
        print("Hello", name)

greet_all(['John', 'Gwen'])

# The zoneinfo module brings support for the IANA time zone database to the standard library.
from zoneinfo import ZoneInfo
from datetime import datetime, timedelta

# Daylight saving time
dt = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
print(dt)
#* 2020-10-31 12:00:00-07:00
dt.tzname()
#* 'PDT'

# Standard time
dt += timedelta(days=7)
print(dt)
#* 2020-11-07 12:00:00-08:00

print(dt.tzname())
#* PST

# HTTP Status Code Registry. HTTP status codes are available in the http standard library
from http import HTTPStatus
HTTPStatus.OK
#* <HTTPStatus.OK: 200>

HTTPStatus.OK.description
#* 'Request fulfilled, document follows'

HTTPStatus(404)
#* <HTTPStatus.NOT_FOUND: 404>

HTTPStatus(404).phrase
#* 'Not Found'
