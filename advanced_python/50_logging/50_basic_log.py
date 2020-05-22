#!/usr/bin/env python3

import logging

def main():

    logging.basicConfig(level=logging.DEBUG, filemode="w", filename="output.log")

    logging.debug("This is a debug-level log message")
    logging.info("This is an info-level log message")
    logging.warning("This is a warning-level message")
    logging.error("This is an error-level message")
    logging.critical("This is a critical-level message")

    # output formatted string to the log
    logging.info("Here's a {} variable and an int: {}".format("string", 10))


if __name__ == "__main__":
    main()