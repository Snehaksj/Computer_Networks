from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.connect(("127.0.0.1",8000)) # Connect

num1=input("Enter number 1:")
num2=input("Enter number 2:")
op=input("Enter operator:")
l=num1+num2+op
print("Sending data to server...")


s.send(l.encode('utf-8')) # Send request

data = s.recv(100).decode()# Get response

print("Received data from server:",data)

s.close()
