import socket
import ssl

'''''''''''
reference:
https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.getpeercert

'''''''''''
hostname = input("input target: ")
context = ssl.create_default_context()


with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        cert = ssock.getpeercert()
        print(ssock.version())

for item in cert:
    print(f"[+]{item}:")
    print(cert[item])

