#!/usr/bin/env python3

def main():
    x = kitten()
    print(x)

def kitten():
    return 'Meow!'

# __name__ will return the name of current module
# so if this file had been included in another
# execution unit by the import statement then this
# would be running as a module and this __name__ 
# would have the name of the module here,
# but currently it is not imported and it is running as 
# __main__ unit
# Basically: if __name__ == __main__ it is running as 
# main unit and will be execited as is.
# If it is imported it would not be executed
if __name__ == '__main__': 
    main() 
    
