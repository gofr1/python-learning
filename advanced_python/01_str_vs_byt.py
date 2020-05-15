#!/usr/bin/env python3

# strings and bytes are not directly interchangeable
# strings contain unicode, bytes a raw 8-bit values

def main():
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "This is a string"
    print(s)

    # you can not just combine them
    # you should use proper decoding/encoding
    s2 = b.decode('utf8')
    print(s+s2)
    
    b2 = s.encode('utf8')
    print(b+b2)
    
    # lets try utf-32
    b3 = s.encode('utf32')
    print(b3)

    
if __name__ == '__main__':
    main()