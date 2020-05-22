#!/usr/bin/env python3

import logging

extData = {
    'user': 'userName'
}

def anotherFunc():
    logging.debug("This is an debug-level log message", extra=extData)

def main():
    fmtstr = 'User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s'
    dtstr = '%Y/%m/%d %I:%M:%S %p'

    logging.basicConfig(level=logging.DEBUG, filemode="w", filename="output.log", 
                        format=fmtstr, datefmt=dtstr)

    logging.info("This is an info-level log message", extra=extData)
    logging.warning("This is a warning-level message", extra=extData)

    anotherFunc()

if __name__ == '__main__':
    main()