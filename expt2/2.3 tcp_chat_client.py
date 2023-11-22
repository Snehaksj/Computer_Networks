from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.connect(("127.0.0.1",8000)) # Connect

while True:

    string= input("Enter message:")
    
    print("Sending data to server...")

    s.send(string.encode('utf-8')) # Send request

    if(string.lower()=='bye'):
        break;

    data = s.recv(100).decode()# Get response

    print("Received data from server:",data)
    if(data.lower()=='bye'):
        print("bye")
        break

s.close()
