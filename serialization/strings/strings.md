What's Unicode?

* Unicode is an encoding schema
* A code point is roughly a character
* A code point is encoded into bytes
* A glyph is a representation of a character

Example:

    Python 3.8.3 (default, May 19 2020, 17:04:53) 
    Type 'copyright', 'credits' or 'license' for more information
    IPython 7.13.0 -- An enhanced Interactive Python. Type '?' for help.
    
    In [1]: s = 'Der Fluß'
    
    In [2]: len(s)
    Out[2]: 8
    
    In [3]: b = s.encode('utf-8')
    
    In [4]: b
    Out[4]: b'Der Flu\xc3\x9f'
    
    In [5]: len(b)
    Out[5]: 9
    
    In [6]: s2 = b.decode('utf-8')
    
    In [7]: s2
    Out[7]: 'Der Fluß'

You will get bytes on the edge of your application, like reading from a socket, a file, accepting http requests etc.

* Input: bytes -> str (decode)
* Output: str -> bytes (encode)

There could be errors while decoding/encoding:

    In [8]: b.decode('ascii')
    ---------------------------------------------------------------------------
    UnicodeDecodeError                        Traceback (most recent call last)
    <ipython-input-9-498050d5a3fb> in <module>
    ----> 1 b.decode('ascii')
    
    UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 7: ordinal not in range(128)
    
    In [9]: b.decode('ascii', errors='ignore')
    Out[9]: 'Der Flu'
