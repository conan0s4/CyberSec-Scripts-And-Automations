''''
Task: Build a Python script that:

Accepts a file or folder as input.
Calculates MD5, SHA1, and SHA256 for each file.
Checks SHA256 hash in VirusTotal (via API).
Outputs a formatted report in JSON or CSV.
Includes status: {"known_malware": True, "detections": 32}

note: 
1.)
ask user first hand for their api key 
save api key in json file then encrypt it "AES-256"
2.)
save response report to json
'''''
import argparse
import hashlib
import requests
import json
import os

def is_malicious(verify):
    if not os.path.exists("vtKey.json"):
        new_api_key = input("input_virus_total_api_key:")
        data = {"api_key": new_api_key}
        with open("vtKey.json", "w") as outfile:
            json.dump(data, outfile)
    with open('vtKey.json', 'r') as file:
        config = json.load(file)
    my_key = config["api_key"]
    url = f"https://www.virustotal.com/api/v3/files/{verify}"
    headers = {
        "x-apikey": my_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code==200:
        print(response.json())
    else:
        print("error!")

def hash(filename):
    MD5 = hashlib.md5()
    SHA1 = hashlib.sha1()
    SHA256 = hashlib.sha256()
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            print("file hashes:")
            print(f"md5: {MD5.hexdigest()}")
            print(f"sha1: {SHA1.hexdigest()}")
            verify = SHA256.hexdigest()
            print(f"sha256: {verify}")
    is_malicious(verify)

def main():
    parser = argparse.ArgumentParser(prog='ch3ckPl3ase')
    parser.add_argument("--filename", help='verify file')
    args = parser.parse_args()
    filename = args.filename
    hash(filename)
if __name__=="__main__":
    main()