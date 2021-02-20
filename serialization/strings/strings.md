# What's Unicode?

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

# Normalization

The Unicode Standard provides well-defined normalization forms that can be used for this: NFC and NFD.

For loose matching, programs may want to use the normalization forms NFKC and NFKD, which remove compatibility distinctions. These two latter normalization forms, however, do lose information and are thus most appropriate for a restricted domain such as identifiers. 

https://www.unicode.org/faq/normalization.html

    Python 3.8.3 (default, May 19 2020, 17:04:53) 
    Type 'copyright', 'credits' or 'license' for more information
    IPython 7.13.0 -- An enhanced Interactive Python. Type '?' for help.
    
    In [1]: %run city.py
    
    In [2]: city
    Out[2]: 'Köln'
    
    In [3]: query
    Out[3]: 'Köln'
    
    In [4]: city == query
    Out[4]: False
    
    In [5]: len(city)
    Out[5]: 4
    
    In [6]: len(query)
    Out[6]: 5
    
    In [7]: city[1]
    Out[7]: 'ö'
    
    In [8]: query[1]
    Out[8]: 'o'
    
    In [9]: query[2]
    Out[9]: '̈'
    
    In [10]: import unicodedata
    
    In [11]: query2 = unicodedata.normalize('NFKC', query)
    
    In [12]: city == query2
    Out[12]: True

 