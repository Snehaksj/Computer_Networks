from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.connect(("127.0.0.1",8000)) # Connect

op='hai'

print("Sending data to server...")

s.send(op.encode('utf-8')) # Send request

data = s.recv(100).decode()# Get response

print("Received data from server:",data)

s.close()
