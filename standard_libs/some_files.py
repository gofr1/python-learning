#!/usr/bin/env python3

def main():
    myFile = open("scores.txt", "w")

    # Show attributes of a file
    print(f"Name: {myFile.name}")
    print(f"Mode: {myFile.mode}")
    
    # Write to file
    myFile.write("GBJ : 100\n")
    myFile.write("NHD : 99\n")
    myFile.write("BBB : 89\n")
    myFile.close()
    
    # Read from file
    myFile = open("scores.txt", "r")
    print("Reading...")
    print(myFile.read()) # we can pass number of characters to read()
    # next read statement will read next characters
    myFile.close()

if __name__ == '__main__':
    main()