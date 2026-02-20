import re



# get auth logs
#get all users that logged using regex

#location :  /var/log/auth.log

with open("file.txt") as f:
    x = re.findall(  r"[<ip>\s* (\d*.\d*.\d*.\d*)]", f.read())
    print(x)


