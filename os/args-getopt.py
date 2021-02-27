#!/usr/bin/env python3

# getopt
# allow grouping argumnets and options
# Can use both UNIX style (-s) and long GNU style (--summary)

import getopt # Is considered outdated
import sys


args, files = getopt.getopt(sys.argv[1:], 'sdvf:', ['summary', 'desc', 'version', 'first-name ='])
print(args)
print(files)

__version__ = 'beta'

for opt, arg in args:
    if opt in ['-s', '--summary']:
        print('Summary')
    if opt in ['-d', '--desc']:
        print('Description')
    if opt in ['-v', '--version']:
        print(f'Version: {__version__}')

# python3 os/args-getopt.py -v 
#* [('-v', '')]
#* []
#* Version: beta

# python3 os/args-getopt.py -v --first-name=Jack
#* [('-v', ''), ('--first-name ', 'Jack')]
#* []
#* Version: beta

# python3 os/args-getopt.py -s arg1 arg2
#* [('-s', '')]
#* ['arg1', 'arg2']
#* Summary
