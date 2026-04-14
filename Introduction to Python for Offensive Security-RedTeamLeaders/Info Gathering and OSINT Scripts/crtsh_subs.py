'''''''''
Passive-Only Recon Write crtsh_subs.py that queries 
https://crt.sh/?q=%.example.com&output=json and dumps unique sub-domains.
references:
https://www.python-httpx.org/
https://hackdb.com/item/crtsh
wildcard search query
Find All Subdomains: %.target.com (e.g., %.google.com) returns all subdomains, excluding the apex domain itself.
'''''''''''

import httpx
import ssl
import socket
# note: implement banner_grab() must use both domains we got from enum and probe
# enum-->probe-->banner grab
def main():
    web_target = input("web target: ")
    recon = input("enum/probe?:")
    if recon == "enum":
        dns_enumerate(web_target)
    elif recon == "probe":
        dns_probe(web_target)

def dns_enumerate(web_target):
    crt_web = "https://crt.sh/"
    query = {'q': f"%.{web_target}", "output": "json"}
    with httpx.Client() as client:
        r = httpx.get(crt_web, params=query, timeout=10.0)
        data = r.json()
    domains = []
    d = []
    for item in data:
        domain = item.get("name_value")
        if domain not in domains:
            domains.append(domain)
            d.append(domain)
            print(domain)

def dns_probe(web_target):
    hostname =  web_target
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
    print(cert["subject"])
    print(cert["subjectAltName"])

if __name__ == "__main__":
    main()




