#!/usr/bin/env python3
# Generating a secret key
import os

secret = os.urandom(64)
print(secret)

with open('secret-key.txt', 'wb') as f:
    f.write(secret)

with open('secret-key.txt', 'rb') as fout:
    print(fout.read())