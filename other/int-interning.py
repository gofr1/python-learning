# CPython keeps an array of integer objects for all integers between -5 and 256, 
# when you create an int in that range you actually just get back a reference to 
# the existing object. This optimization technique is known as integer interning.
# At startup, Python caches a list of integers into the memory to optimize performance and memory usage.

# To understand concept of integer interning, let's check memory address of integers inside and outside of the range -5 to 256.

# Integer inside range -5 to 256:

a=20
b=20

print("Address of a:", id(a))
#* Address of a: 94120979507552
print("Address of b:", id(b))
#* Address of b: 94120979507552
print("a is b:", a is b)
#* a is b: True

# Integer outside range -5 to 256:

a=-6
b=-6
print("Address of a:", id(a))
#* Address of a: 140331834667248
print("Address of b:", id(b))
#* Address of b: 140331834667088
print("a is b:", a is b)
#* a is b: False