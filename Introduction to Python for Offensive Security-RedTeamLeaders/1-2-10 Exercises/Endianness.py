

''''
Endianness
Write a function int_to_little_endian(n, length)
that converts any positive integer to a little-endian byte sequence of fixed length.

'''

n = 2565
length = 8

def int_to_little_endian(n, length):
    return n.to_bytes(length, byteorder='little')

res = int_to_little_endian(n, length)
print(res)

#source:
#https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview