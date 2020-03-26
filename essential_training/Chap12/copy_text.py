#!/usr/bin/env python3

def main():
    infile = open('lines.txt', 'rt')
    outfile = open('lines_copy.txt', 'wt')

    for line in infile:
        # this will rewrite line endings in the new file with default system line endings
        print(line.rstrip(), file=outfile) 
        # # and this will create the same file
        # outfile.writelines(line)
        print('.',end='', flush=True)
    infile.close()
    outfile.close()
    print('\ndone')

if __name__ == '__main__':
    main()