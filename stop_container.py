#!/usr/bin/python3
print("Content-type: text/html")
print()
import subprocess
import cgi

form=cgi.FieldStorage()
name=form.getvalue("name")

command = f"sudo docker stop {name}"
output=subprocess.getoutput(command)
print(output)
print(f"Docker Container named '{name}' Stopped")