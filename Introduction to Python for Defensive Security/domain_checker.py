import argparse
import subprocess
import re

def ping(domain):
    res = subprocess.run(["ping", domain])
def whois(domain):
    res = subprocess.run(["powershell" , "whois" , domain])
def Main():
    parser = argparse.ArgumentParser(prog='checker')
    parser.add_argument("--domain", help='target domain')
    args = parser.parse_args()
    domain_pattern = r"^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$"
    if not args.domain:
        parser.print_help()
        print("install: Install-Module -Name Get-WHOIS -RequiredVersion 1.0.1")
    elif not re.fullmatch(domain_pattern , args.domain):
        print("invalid format")
        parser.print_help()
        print("install: Install-Module -Name Get-WHOIS -RequiredVersion 1.0.1")
    else:
        live = ping(args.domain)
        who = whois(args.domain)
        print(live)
        print(who)
if __name__=="__main__":
    Main()


