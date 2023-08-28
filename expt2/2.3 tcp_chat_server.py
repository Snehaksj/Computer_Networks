from socket import *

s = socket(AF_INET,SOCK_STREAM)

s.bind(("",8000))

s.listen(5)

while True:

    c,a = s.accept()

    print("Received connection from", a)

    data=c.recv(100).decode()

    print("Recieved data from client:",data)

    newmessage='bye'

    print("Sending data to client...")

    c.send(newmessage.encode('utf-8'))

c.close()
