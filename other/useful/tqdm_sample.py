#!/usr/bin/env python3

# sudo pip3 install tqdm
# this library is going to help you when your CLI tool is processing something 
# time-consuming by showing a progress bar to indicate how much has been done.
from tqdm import tnrange, trange
from time import sleep

for _ in trange(100):
    sleep(0.01)

from tqdm import tqdm

for e in tqdm([1,2,3,4,5,6,7,8,9]):
    sleep(0.5)  # Suppose we are doing something with the elements
