#!/usr/bin/env python3
#! International Morse Code

morse = {
'A':'·−',      'H':'····',   'O':'−−−',    'V':'···−',    '3':'···−−',
'B':'−···',    'I':'··',     'P':'·−−·',   'W':'·−−',     '4':'····−',
'C':'−·−·',    'J':'·−−−',   'Q':'−−·−',   'X':'−··−',    '5':'·····',
'D':'−··',     'K':'−·−',    'R':'·−·',    'Y':'−·−−',    '6':'−····',
'E':'·',       'L':'·−··',   'S':'···',    'Z':'−−··',    '7':'−−···',
'F':'··−·',    'M':'−−',     'T':'−',      '1':'·−−−−',   '8':'−−−··',
'G':'−−·',     'N':'−·',     'U':'··−',    '2':'··−−−',   '9':'−−−−·',
'.':'·−·−·−',  ',':'−−··−−', '?':'··−−··', '\'':'·−−−−·', '0':'−−−−−',
'!':'−·−·−−',  '/':'−··−·',  '(':'−·−−·',  ')':'−·−−·−',
'&':'·−···',   ':':'−−−···', ';':'−·−·−·', '=':'−···−',
'+':'·−·−·',   '-':'−····−', '_':'··−−·−', '"':'·−··−·',
'$':'···−··−', '@':'−−·−·',
}

#string = 'The quick brown fox jumps over the lazy dog'
#string = 'sos'
string = 'morse code'


def encode_morse(string):
    simple_space = ' '
    # The space between letters is three units
    letter_space = 3 * simple_space
    # The space between words is seven units 
    words_space = 7 * simple_space

    output = ''
    
    for letter in string.upper():
        if letter == ' ':
            output += words_space
        if letter in morse.keys():
            code = ' '.join(list(morse[letter]))
            output += f'{code}{letter_space}'
    return output

print(encode_morse(string))

