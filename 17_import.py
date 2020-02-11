# if you want to use some other module/library/etc
# you can import it in your name space

# this code will create 2 variables that points on sin and pi functions
# from math module
from math import sin, pi # !! this is used to take specific attributes
# from math import (sin, 
# pi)
# from math import sin,\ 
# pi
sin(pi/2)
# math is not in your namespace!
'sin' in dir()
# True

# this will create variable that points on math module
import math # !! this imports ALL attributes
dir(math) # show all attributes
# most of them are functions
math.tan(0) 
# 0.0

# if you have function with same name you can use alias
from math import sin as other_sin
other_sin(0)
# 0.0

# if you got function with name = module name
import math as other_math
other_math.sin(0)
# 0.0

# massive import
# that command loads ALL the content of math module in
# local namespace
# this must be used carefuly
from math import *
asin(0)
# 0.0

# rules of import:
# - import of standart modules
import json
import sys
# - import from third-party modules
import tkinter
import pyodbc
# - import from local modules
import blackjack




# task1
import json
help(json)
my_data = {"name":"John", "age": "45"}
json.dumps(my_data)

# task2
import os

def find_extension (file_name):
    return file_name[file_name.rfind('.')+1:]

def ext_count(dir_to_search):
    files = [fl for fl in os.listdir(dir_to_search) if os.path.isfile(os.path.join(dir_to_search, fl))]
    files_ext = dict()
    
    for fl in files:
        ext = find_extension(fl)
        s = files_ext.setdefault(ext, 1)
        files_ext[ext] += 1
    
    return files_ext

ext_count('/home/gofr1/Downloads/')
ext_count('/tmp')