'''''''''
in memory malware w/ string obfuscation
basic 


'''''
import base64
import subprocess
# print(Safe Demo)
encoded = "cHJpbnQoJ1NhZmUgZGVtbycp"
decoded = base64.b64decode(encoded).decode()

exec(decoded)
'''''
command = ["powershell", "-Command", "echo 'Hello' "]
result = subprocess.run(command, capture_output=True, text=True, check=True)
print(result.stdout.strip())
'''
enc = "Y29tbWFuZCA9IFsicG93ZXJzaGVsbCIsICItQ29tbWFuZCIsICJlY2hvICdIZWxsbycgIl0KcmVzdWx0ID0gc3VicHJvY2Vzcy5ydW4oY29tbWFuZCwgY2FwdHVyZV9vdXRwdXQ9VHJ1ZSwgdGV4dD1UcnVlLCBjaGVjaz1UcnVlKQpwcmludChyZXN1bHQuc3Rkb3V0LnN0cmlwKCkpCg=="
dec = base64.b64decode(enc).decode()

exec(dec)