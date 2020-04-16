#!/usr/bin/env python3

def main():
    # Read from file
    myFile = open("./scores.txt", "r")
    
    # read one line
    myFile.readline()
    myFile.seek(0)

    # iterate
    for line in myFile:
        print(line)
    
    myFile.close()

if __name__ == '__main__':
    main()