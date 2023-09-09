#!/usr/bin/python3
import cgi
import subprocess
import uuid

print("content-type: text/html")
print()

form = cgi.FieldStorage();
cmd = form.getvalue("c");
print(cmd)

def launch_container_with_unique_name(image_name):
    unique_id = uuid.uuid4()
    container_name = f"container-{unique_id}"


if "date" in cmd:
    output=subprocess.getoutput("date")
    print(output)

elif "cal" in cmd:
    output=subprocess.getoutput("cal")
    print("<pre>")
    print(output)
    print("</pre>")

elif "docker container" in cmd:
    output=subprocess.getoutput("sudo docker ps ")
    print("<pre>")
    print(output)
    print("</pre>")

elif "docker images" in cmd:
    output=subprocess.getoutput("sudo docker images")
    print("<pre>")
    print(output)
    print("</pre>")

elif "new container" in cmd:
    container_name = form["container_name"].value
    # Launch the Docker container using subprocess
    try:
        subprocess.run(["docker", "run", "--name", container_name, "-d", "centos:7"])
        print("<h2>Success! Docker container '{}' has been launched.</h2>".format(container_name))
    except Exception as e:
        print("<h2>Error launching Docker container: {}</h2>".format(e))

elif "pwd" in cmd:
    output=subprocess.getoutput("pwd")
    print("<pre>")
    print(output)
    print("</pre>")

elif "ip" in cmd:
    output=subprocess.getoutput("ifconfig")
    print("<pre>")
    print(output)
    print("</pre>")

elif "df" in cmd:
    output=subprocess.getoutput("df")
    print("<pre>")
    print(output)
    print("</pre>")

elif "xdotool" in cmd:
    output = subprocess.getoutput("xdotool getmouselocation");
    print("<pre>")
    print(output);
    print("</pre>")
    

elif "dpkg" in cmd:
    output = subprocess.getoutput("dpkg -l");
    print("<pre>")
    print(output);
    print("</pre>")

elif "uptime" in cmd:
    output = subprocess.getoutput("uptime");
    print(output);

elif "ping" in cmd:
    host = "www.google.com"
    output = subprocess.getoutput(f"ping -c 4 {host}");
    print(output);

elif "ps" in cmd:
    output = subprocess.getoutput("uname -a");
    print(output);

elif "free" in cmd:
    output = subprocess.getoutput("free -h");
    print(output);
elif "env" in cmd:
    output = subprocess.getoutput("env");
    print(output);
elif "openss" in cmd:
    output = subprocess.getoutput("openssl rand -base64 12");
    print(output);

elif "history" in cmd:
    output = subprocess.getoutput("history");
    print(output)
else:
    print("well try.....")