#!/usr/bin/env python3

import tempfile

def main():
    # create
    tempFile = tempfile.TemporaryFile()

    # write
    tempFile.write(b"Save this special number for me: 5678309")
    tempFile.seek(0)

    # read
    print(tempFile.read())

    # close
    tempFile.close()

if __name__ == '__main__':
    main()