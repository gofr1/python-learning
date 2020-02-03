# in python 3 all strings are stored as unicode
# ASCII uses 7 bits for 128 symbols and control charecters
# it is commonly used with latin alphabet
# in windows they use windows-1252

# so 4 bite codepage would store more than 4 milliards of symbols
# but if you need to work only w latin alphabet - it is 4 times
# incresing space

# the most used is UTF-8 (compatible with ASCII)
# it uses from 1 to 4 bites per symbol

# e.g. grinning face
print('\N{GRINNING FACE}') #name
print('\U0001f600') # code
print(b'\xf0\x9f\x98\x80'.decode('utf8')) # utf8
print('\u263A')

# if you want to know your OS codepage use this
import locale
locale.getpreferredencoding(False)

# UTF-8 stands for Unicode Transformation Format - 8 bit
print('x\u00b2'.encode('utf8'))
print(b'x\xc2\xb2'.decode('utf8'))

# byte string can not be encoded, only decoded
# you can never in what codepage byte string came, so
# you can decode it using wrong codepage and get
# 'mojibake' (Corrupt characters or letters, especially 
# from display or transfer through an inappropriate 
# character set or encoding.)

b'x\xc2\xb2'.decode('cp1026') # Turkey 'ÌB¥'
b'x\xc2\xb2'.decode('cp949') # Korea 'x짼'
b'x\xc2\xb2'.decode('shift_jis_2004') # Japan 'xﾂｲ'

# if there is now such bytes representation in codepage you will get error
b'x\xc2\xb2'.decode('ascii') 
# UnicodeDecodeError: 'ascii' codec can't decode byte 

# you can use error= in decode part, to ignore/replace 
# chars that cannot be decoded. Loss of data is possible
b'x\xc2\xb2'.decode('ascii', errors='ignore') 
# 'x'
b'x\xc2\xb2'.decode('ascii', errors='replace')
# 'x��'

# when writing to file default OS codepage is used *see locale above
with open('/tmp/sq.utf8','w') as fout:
    fout.write('x²\n')
# if you need some other codepage use this
with open('/tmp/sq.cp949','w', encoding='cp949') as fout:
    fout.write('x²\n')

# task1
print('\N{CONFUSED FACE}') # by name
print('\U0001f615') # by code
print(b'\xf0\x9f\x98\x95'.decode('utf8')) # utf8
print('😕') # by glyph

# task2
def turn_str_upsidedown(word):
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxys'
    upsidedown_abc = '∀qϽᗡƎℲƃHIſʞ˥WNOԀὉᴚS⊥∩ΛMXʎZɐqɔpǝɟƃɥıɾʞןɯuodbɹsʇnʌʍxʎs'
    result = ''
    pos = 0
    for letter in word:
        pos = abc.find(letter)
        result += upsidedown_abc[pos:pos+1] if pos >= 0 else letter
    return result

turn_str_upsidedown('Hello word!')

# task3
my_name = turn_str_upsidedown('John')
# cannot encode
my_name.encode('cp949', errors='replace')
my_name.encode('cp1026', errors='replace')
my_name.encode('shift_jis_2004', errors='replace')
# can encode
my_name.encode('utf16')
my_name.encode('utf32')
