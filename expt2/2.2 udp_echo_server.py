import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_socket.bind(('', 12000))

while True:

    data, address =server_socket.recvfrom(1024)
    message = data.decode('utf-8')

    server_socket.sendto(message.encode('utf-8'),address)
    print(data)
