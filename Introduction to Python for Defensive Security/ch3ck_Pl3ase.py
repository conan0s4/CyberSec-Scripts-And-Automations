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

def is_malicious(verify):


    new_api_key = input("input_virus_total_api_key:")

    # Open and load the JSON file
    with open('VT_apiKey.json', 'r') as file:
        config = json.load(file)

    my_key = config.get("api_key")


    url = f"https://www.virustotal.com/api/v3/files/{verify}"
    headers = {
        "x-apikey": api_key
    }
    response = requests.get(url, headers=headers)
    print(response.json())


def hash(filename,verify):
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
def main():
    parser = argparse.ArgumentParser(prog='ch3ckPl3ase')
    parser.add_argument("--filename", help='verify file')
    args = parser.parse_args()
    filename = args.filename
    hash(filename)

if __name__=="__main__":
    main()