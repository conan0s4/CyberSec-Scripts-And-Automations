import httpx
import ssl
import socket
# note: implement banner_grab() must use both domains we got from enum and probe
# enum-->probe-->banner grab
#implementation of argparse
def main():
    web_target = input("web target: ")
    res = input("enum/probe/exit?:")
    Domains = []
    e_domains = []
    p_domains = []
    if res == "enum":
        dns_enumerate(web_target,e_domains)
    elif res == "probe":
        dns_probe(web_target,p_domains)

    Domains = e_domains + p_domains
    print(Domains)

def dns_enumerate(web_target,e_domains):
    crt_web = "https://crt.sh/"
    query = {'q': f"%.{web_target}", "output": "json"}
    with httpx.Client() as client:
        r = httpx.get(crt_web, params=query, timeout=60.0)
        data = r.json()
    for item in data:
        domain = item.get("name_value")
        if domain not in e_domains:
            e_domains.append(domain)
#    for i in range(len(e_domains)):
#        print(e_domains[i])

def dns_probe(web_target,p_domains):
    hostname =  web_target
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
    dom0 = list(cert["subject"][4])
    dom1 = list(cert["subjectAltName"])
    for item in range(len(dom1)):
        p_domains.append(dom1[item][1])
    p_domains.append(dom0[0][1])
#    print(p_domains)

#def banner_grab():


if __name__ == "__main__":
    main()




