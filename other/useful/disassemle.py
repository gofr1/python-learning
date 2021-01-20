#!/usr/bin/env python3
import dis

def test(number):
    return (str(number)+str(number))

def newFunc(string):
    print("Hello", string)

# This will display the disassembly of test():
dis.dis(test)

#*  2           0 LOAD_GLOBAL              0 (str)
#*              2 LOAD_FAST                0 (number)
#*              4 CALL_FUNCTION            1
#*              6 LOAD_GLOBAL              0 (str)
#*              8 LOAD_FAST                0 (number)
#*             10 CALL_FUNCTION            1
#*             12 BINARY_ADD
#*             14 RETURN_VALUE

# This will display the disassembly of newFunc()
dis.dis(newFunc)
#*  2           0 LOAD_GLOBAL              0 (print)
#*              2 LOAD_CONST               1 ('Hello')
#*              4 LOAD_FAST                0 (string)
#*              6 CALL_FUNCTION            2
#*              8 POP_TOP
#*             10 LOAD_CONST               0 (None)
#*             12 RETURN_VALUE