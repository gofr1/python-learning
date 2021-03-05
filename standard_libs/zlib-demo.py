import zlib
import binascii

# Here the argument data contains the bytes to be compressed, 
# and level is an integer value that can take the values -1 or 0 to 9. 

# Level 9 is the slowest, yet it yields the highest level of compression. 

data = b'Hello world'

compressed_data = zlib.compress(data, 2)

print('Original data: ', data)
print('Original data length: ', len(data))
#* Original data:  b'Hello world'
#* Original data length:  11

print('Compressed data: ', compressed_data)
print('Compressed data length: ',len(compressed_data))
#* Compressed data:  b'x^\xf3H\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00\x18\xab\x04='
#* Compressed data length:  19

print('Compressed data: ', binascii.hexlify(compressed_data))
print('Compressed data: ', len(binascii.hexlify(compressed_data)))
#* Compressed data:  b'785ef348cdc9c95728cf2fca49010018ab043d'
#* Compressed data:  38
