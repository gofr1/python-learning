#!/usr/bin/env python3

from datetime import date

def main():

    a = [1,2,3]
    # in this example, the assignment expression helps avoid calling len() twice:
    if (n := len(a)) > 10:
        print(f"List is too long ({n} elements, expected <= 10)")

    # in the following example, parameters a and b are positional-only, 
    # while c or d can be positional or keyword, and e or f are required to be keywords:
    def f(a, b, /, c, d, *, e, f):
        print(a, b, c, d, e, f)
    
    f(10, 20, 30, d=40, e=50, f=60)

    # added an = specifier to f-strings. An f-string such as f'{expr=}' will expand to 
    # the text of the expression, an equal sign, then the representation of
    #  the evaluated expression. For example:
    user = 'eric_idle'
    member_since = date(1975, 7, 31)
    f'{user=} {member_since=}'

if __name__ == '__main__':
    main()