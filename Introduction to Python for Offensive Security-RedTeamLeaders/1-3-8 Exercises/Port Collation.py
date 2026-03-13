'''''''''
Port Collation
Read a file of ip:port pairs, output a dict mapping each ip to a sorted list of unique ports.

dict


'''''''''

import re
from enum import unique

d = {}

with open("ports.txt","r") as f:
    for line in f :
        ip , port = line.strip().split(":")
        d[ip] = port

print(d)
portval = set()
unique_port = {}

for key, value in d.items():
    if value not in portval:
        unique_port[key] = [value]
        portval.add(value)


print(unique_port)







