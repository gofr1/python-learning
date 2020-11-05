#!/usr/bin/env python3

# By default Python uses a dict to store an object’s instance attributes.
# The dictionary wastes a lot of RAM. 
# Python can’t just allocate a static amount of memory at object creation to store all the attributes. 
# Therefore it sucks a lot of RAM if you create a lot of objects (I am talking in thousands and millions). 
# Still there is a way to circumvent this issue. It involves the usage of __slots__ to tell Python 
# not to use a dictionary, and only allocate space for a fixed set of attributes.

# sudo pip3 install ipython_memory_usage
# sudo pip3 install slots

import ipython_memory_usage.ipython_memory_usage as imu

# With slots
class MyClassWithSlots(object):
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

# Without slots
class MyClassWithoutSlots(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

imu.start_watching_memory()

num = 1024*256
x = [MyClassWithSlots(1,1) for i in range(num)]
#* used 15.2266 MiB RAM in 0.37s, peaked 0.00 MiB above current, total RAM usage 60.02 MiB

y = [MyClassWithoutSlots(1,1) for i in range(num)]
#* used 29.1328 MiB RAM in 0.49s, peaked 0.00 MiB above current, total RAM usage 89.67 MiB

imu.stop_watching_memory()