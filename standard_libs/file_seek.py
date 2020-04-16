#!/usr/bin/env python3

def main():
    # Read from file
    myFile = open("scores.txt", "r")
    print("Reading...")
    print(myFile.read(10))
    # seek is a pointer that keeps a track of where we are in the file
    myFile.seek(0)
    print("Reading again...")
    print(myFile.read(10))

if __name__ == '__main__':
    main()