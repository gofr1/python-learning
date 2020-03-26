#!/usr/bin/env python3

def main():
    infile = open('berlin.jpg', 'rb')
    outfile = open('berlin_copy.jpg', 'wb')

    while True:
        buf = infile.read(10240) # read 10KB in a loop
        # it is a good practice to read file ib some slices
        # because the file could be very big and maybe
        # there is not enough memory to read it at once
        if buf:
            outfile.write(buf)
            print('.',end='', flush=True)
        else: break # this will break while True statement
    infile.close()
    outfile.close()
    print('\ndone')

if __name__ == '__main__':
    main()

