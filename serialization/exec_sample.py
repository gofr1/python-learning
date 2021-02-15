#!/usr/bin/env python3
# Loading config with exec
from types import SimpleNamespace

def load_config(path):
    with open(path) as fp:
        data = fp.read()
    
    ns = {}
    exec(data, {}, ns)
    return(SimpleNamespace(**ns))

# now in ipython (or python)

# In [1]: %run exec_sample.py                                                                                     
# In [2]: config = load_config('server_config.py') 
# In [3]: config                                                                                                
# Out[3]: namespace(api_key=None, log_level=20, num_workers=100, port=8888)
