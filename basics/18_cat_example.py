#!/usr/bin/env python3

r"""Simple implementation of ``cat`` unix command
Only supported parameter is ``number``
This example demonstrates file structure
and useful hints of python""" # documentation

# We will take parameters/arguments from user input like:
# ./18_cat_example.py --help # will show help
# ./18_cat_example.py filename # will show data stored in file like cat
# Use argumnets as input for a script
import argparse
import logging
import sys

__version__ = '0.0.1' # metadata

logging.basicConfig(level=logging.DEBUG)

class Catter(object):
    """Class for file concatenation
    in standart output"""

    def __init__(self, files, show_numbers=False):
        self.files = files
        self.show_numbers = show_numbers

    def run(self, fout):
        # use 6 spaces with right align
        fmt = '{0:>6} {1}'
        for fin in self.files:
            logging.debug('catting {0}'.format(fin))
            for count, line in enumerate(fin, 1):
                if self.show_numbers:
                    fout.write(fmt.format(count, line))
                else:
                    fout.write(line)

def main(args):
    """cat logic w/ arguments"""
    parser = argparse.ArgumentParser(
        description='Concatenate FILE(s), or '
        'standart input, to standard output')
    parser.add_argument('--version',
        action='version', version=__version__)
    parser.add_argument('files', nargs='*',
        type=argparse.FileType('r'),
        default=[sys.stdin], metavar='FILE')
    parser.add_argument('-n','--number',
        action='store_true',
        help='number all output lines')
    parser.add_argument('--run-tests',
        action='store_true',
        help='run module tests')
    args = parser.parse_args(args)
    
    if args.run_tests:
        import doctest
        doctest.testmod()
    else:
        cat = Catter(args.files, args.number)
        cat.run(sys.stdout)
        logging.debug('done catting')
    
if __name__=='__main__':
    main(sys.argv[1:])
