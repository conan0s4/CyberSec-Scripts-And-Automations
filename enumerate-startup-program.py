import subprocess


Res = subprocess.run(["net" , "user"])
print(Res)

#startup for all users
res = subprocess.run(["dir" , r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"] ,shell=True) #if built in terminal not exe
print(res)

#all user startup registry
#seperate args in "" ,
#r raw string for file paths or double \\
r3s = subprocess.run(["reg" ,"query" ,r"HKLM\Software\Microsoft\Windows\CurrentVersion\Run"])
print(r3s)
