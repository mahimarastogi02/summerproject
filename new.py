#!/usr/bin/python3
print("content-type: text/html")
print()

import cgi
import subprocess
form = cgi.FieldStorage()
cmd = form.getvalue("c")

if "date" in cmd:
    output = subprocess.getoutput("date")
    print(output)
elif "cal" in cmd:
    output = subprocess.getoutput("cal")
    print(output)
elif "df" in cmd:
    output = subprocess.getoutput("sudo df")
    print(output)
elif "ifconfig" in cmd:
    output=subprocess.getoutput("ifconfig")
    print(output)
elif "ls" in cmd:
    output=subprocess.getoutput("ls")
    print(output)
elif "whoami" in cmd:
    output=subprocess.getoutput("whoami")
    print(output)
elif "pwd" in cmd:
    output=subprocess.getoutput("pwd")
    print(output)
elif "dd" in cmd:
    output=subprocess.getoutput("dd")
    print(output)
elif "tail" in cmd:
    output=subprocess.getoutput("tail new.py")
    print(output)
elif "env" in cmd:
    output=subprocess.getoutput("env")
    print(output)

elif "netstat" in cmd:
    output=subprocess.getoutput("netstat")
    print(output)

elif "head new.py" in cmd:
    output=subprocess.getoutput("head new.py")
    print(output)

elif "grep" in cmd:
    output=subprocess.getoutput("grep")
    print(output)
elif "all containers" in cmd:
    output = subprocess.getoutput("sudo docker ps -a")
    print(output)
elif "container" in cmd:
    output=subprocess.getoutput("sudo docker ps")
    print(output)
elif "docker images" in cmd:
    output=subprocess.getoutput("sudo docker images")
    print(output)
elif "launch centos 5.11" in cmd:
    output=subprocess.getoutput("sudo docker pull centos:5.11")
    print(output)
elif "launch centos 6.6" in cmd:
    output=subprocess.getoutput("sudo docker pull centos:6.6")
    print(output)
elif "launch ubantu" in cmd:
    output=subprocess.getoutput("sudo docker pull boystar/ubantu")
    print(output)
else:
    print("command not found")
