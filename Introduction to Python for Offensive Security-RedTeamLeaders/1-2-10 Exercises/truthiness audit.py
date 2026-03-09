''''''''''
Truthiness Audit
Write a class OpenPort with attributes port and status, 
and define __bool__ so that the instance is truthy only when status == "open".
'''''''''''

class OpenPort:

    def __init__(self , port , status):
        self.port = port
        self.status = status

    def __bool__(self):
        if self.status == "open":
            return True
        elif self.status == "close":
            return  False


#https://www.pythontutorial.net/python-oop/python-__bool__/

p0rts = [OpenPort(22,"open"),OpenPort(80,"close")]

for i in range(len(p0rts)):
    print(bool(p0rts[i]))
