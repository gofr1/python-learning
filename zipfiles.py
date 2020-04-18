#!/usr/bin/env python3

import zipfile

def main():
    # open
    zip = zipfile.ZipFile('archive.zip', 'r')
    
    # list
    print(zip.namelist())

    # metadata
    for meta in zip.infolist():
        print(meta)
    
    info = zip.getinfo("purchases.txt")
    print(info)

    # access a file in archive
    print(zip.read("wishlist.txt"))

    with zip.open("wishlist.txt") as f:
        print(f.read())
    
    # exctract
    #zip.extract("purchases.txt")
    zip.extractall()

    # close
    zip.close()

if __name__ == '__main__':
    main()