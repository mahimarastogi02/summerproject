#!/usr/bin/python3
print("Content-type: text/html")
print()

import cgi

form=cgi.FieldStorage()
receiver_number=form.getvalue("number")
message=form.getvalue("message")

number="+91"+receiver_number

from twilio.rest import Client
# Your Account Sid and Auth Token from twilio account
account_sid = 'AC58b22aedca9284cb6306111f7afeae5e'
auth_token = '83a4c4f786193fcc599f4cb8c2ffa193'
# instantiating the Client
client = Client(account_sid, auth_token)
messagesent = client.messages.create(body=message, from_='+14326662708', to=number)
print("Message Successfully sent and the message id is",messagesent.sid)