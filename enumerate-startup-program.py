import subprocess

#startup for all users
res = subprocess.run(["dir" , r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"] ,shell=True) #if built in terminal not exe
print(res)

#all user startup registry
#if exe seperate args
#r raw string for file paths or double \\
r3s = subprocess.run(["reg" ,"query" ,r"HKLM\Software\Microsoft\Windows\CurrentVersion\Run"])
print(r3s)
