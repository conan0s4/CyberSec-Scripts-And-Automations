'''''
Mutable XOR
Create a function xor_bytes(data: bytearray, key: int) that XORs each byte with a one-byte key in place.

'''''

#exlusive or - comparing individual bits to key


key = 200
data = bytearray([40, 159, 152, 138])


def xor_bytes(data: bytearray, key: int):
    for i in range(len(data)):
        data[i] ^=  key
    return data


print(xor_bytes(data, key))
#https://www.geeksforgeeks.org/python/get-the-logical-xor-of-two-variables-in-python/



