import os
from datetime import datetime

# The name of the operating system dependent module imported. 
print(os.name)

some_file = "somefile.txt"

# check for existance and type
print("Item exists:", os.path.exists(some_file))
print("Item is file:", os.path.isfile(some_file))
print("Item is directory:", os.path.isdir(some_file))

# work with file paths
print("Item path:", os.path.realpath(some_file))
print("Item path and name:", os.path.split(os.path.realpath(some_file)))

# get modification time
item_mod_time = datetime.fromtimestamp(os.path.getmtime(some_file))
print("Item modification time is:", item_mod_time)

# calculate how long ago the item was modified
td = datetime.now() - item_mod_time
print("It has being {} since the file was modified\nOr, {} seconds".format(td, td.total_seconds()))