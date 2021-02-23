#!/usr/bin/env python3
#! Assert
#! - Great for testing and debugging
#! - Not for business logic

can_access = False

try:
    assert can_access
except AssertionError:
    print('No access!')

# In python there is an optimizied mode
# This mode do some tweaks and one of this tweaks is getting rid of assortion
# In terminal: python3 -O simple-assortion.py
#! No exception will be thrown!

#? How to fix this?
# Good old if statement

if can_access is False:
    print('No access!')

# onxe again run: python3 -O simple-assortion.py
#* No access!