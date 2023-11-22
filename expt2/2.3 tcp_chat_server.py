from socket import *

s = socket(AF_INET,SOCK_STREAM)

s.bind(("",8000))

s.listen(5)

c,a = s.accept()

while True:

    data=c.recv(100).decode()

    if data.lower()=='bye':
        print('bye')
        break
    else:
        print("Recieved data from client:",data)

    newmessage=input("Enter message:")

    print("Sending data to client...")

    c.send(newmessage.encode('utf-8'))
    
    if(newmessage.lower()=='bye'):
        break

c.close()
