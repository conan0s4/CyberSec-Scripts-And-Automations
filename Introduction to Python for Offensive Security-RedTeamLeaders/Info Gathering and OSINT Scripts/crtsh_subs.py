'''''''''
Passive-Only Recon Write crtsh_subs.py that queries 
https://crt.sh/?q=%.example.com&output=json and dumps unique sub-domains.
references:
https://www.python-httpx.org/
https://hackdb.com/item/crtsh
wildcard search query
Find All Subdomains: %.target.com (e.g., %.google.com) returns all subdomains, excluding the apex domain itself.
'''''''''
import httpx
crt_web = "https://crt.sh/"
web_target = input("input target: ")
query = {'q':f"%.{web_target}","output":"json"}
with httpx.Client() as client:
    r = httpx.get(crt_web, params=query , timeout=60.0)
    data = r.json()
print("""
-----------------------------------------------------------
sub-domains: 
-----------------------------------------------------------
""")
domains = []
d = []
for item in data:
    domain = item.get("common_name")
    if domain not in domains:
        domains.append(domain)
        d.append(domain)
        print(domain)






