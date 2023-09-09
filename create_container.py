#!/usr/bin/python3
print("Content-type: text/html")
print()
import subprocess
import cgi
import cgitb
cgitb.enable()

form=cgi.FieldStorage()
name=form.getvalue("name")
os_name=form.getvalue("os")

command = f"sudo docker run -dit --name {name} {os_name}"
output=subprocess.getoutput(command)
print(f"Docker Container named '{name}' Launched")