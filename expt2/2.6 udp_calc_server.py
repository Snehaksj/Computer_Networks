import socket

def calculate(l):
    if l[2]=='+':
        return str(int(l[0])+int(l[1]))
    elif l[2]=='-':
        return str(int(l[0])-int(l[1]))
    elif l[2]=='*':
        return str(int(l[0])*int(l[1]))
    elif l[2]=='/':
        return str(int(l[0])/int(l[1]))
    

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_socket.bind(('', 12000))

while True:

    data, address =server_socket.recvfrom(1024)
    message = data.decode('utf-8')
    print("Received message from client...")
    newmessage=calculate(message)
    print("Sending message to client...")
    server_socket.sendto(newmessage.encode('utf-8'),address)
