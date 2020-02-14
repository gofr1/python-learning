import some_module

# __name__ shows if some script/file is loaded as module
# or is executed as scenario

# in REPL it is import
# The name is: some_module

# from terminal it is scenario
# python3 some_module.py 
# The name is: __main__

# if module is imported "if __name__=='__main__':..."" will not be executed