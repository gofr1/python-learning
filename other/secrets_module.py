#!/usr/bin/env python3

# Generate cryptographically strong pseudo-random numbers suitable for managing 
# secrets such as account authentication, tokens, and similar.
import secrets

# Return a random integer in the range [0, n)
# () stands for open interval
# [] means closed interval
# {} is used to denote specific elements.
secrets.randbelow(10)

# Return an integer with n random bits
secrets.randbits(6)

# Return a randomly-chosen element from a non-empty sequence
seq = [10, 5, 7, 9]
secrets.choice(seq)

# Return a random byte string containing *nbytes* bytes.
secrets.token_bytes(10)
#* b'\xdc:`\xbd\x9c\xe6\xeaJ\xf4V'

# Return a random text string, in hexadecimal.
# The string has *nbytes* random bytes, each byte converted to two hex digits. 
secrets.token_hex(10)
#* '3e582012364e3ca02fbc'

# Return a random URL-safe text string, in Base64 encoding.
# The string has *nbytes* random bytes. 
secrets.token_urlsafe(5)
#* 'cytvqrA'