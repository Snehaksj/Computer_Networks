from socket import *

def calculate(l):
    if l[2]=='+':
        return str(int(l[0])+int(l[1]))
    elif l[2]=='-':
        return str(int(l[0])-int(l[1]))
    elif l[2]=='*':
        return str(int(l[0])*int(l[1]))
    elif l[2]=='/':
        return str(int(l[0])/int(l[1]))
    
s = socket(AF_INET,SOCK_STREAM)

s.bind(("",8000))

s.listen(5)

while True:

    c,a = s.accept()

    print("Received connection from", a)

    data=c.recv(100).decode()

    print("Recieved data from client...")

    newmessage=calculate(data)

    print("Sending data to client...")

    c.send(newmessage.encode('utf-8'))

c.close()
