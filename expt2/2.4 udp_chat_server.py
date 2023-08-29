import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_socket.bind(('', 12000))

while True:

    data, address =server_socket.recvfrom(1024)
    message = data.decode('utf-8')
    print("Recieved from client...")
    if message=='bye':
        print('bye')
        break
    else:
        print(message)
    msg= input("Enter message")
    print("sending message to client")
    server_socket.sendto(msg.encode('utf-8'),address)
    if(msg=='bye'):
        break
