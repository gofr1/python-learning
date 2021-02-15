#!/usr/bin/env python3
# Loading config with importlib
from importlib.machinery import SourceFileLoader

def load_config(path):
    return SourceFileLoader('config', path).load_module()

# now in ipython (or python)

# In [3]: %run importlib_sample.py                                                                              
# In [4]: config = load_config('server_config.py')                                                              
# In [5]: config                                                                                                
# Out[5]: <module 'config' from 'server_config.py'>
# In [6]: config.port                                                                                           
# Out[6]: 8888


