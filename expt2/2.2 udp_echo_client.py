import socket

client_socket =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

message = 'test'

addr = ("127.0.0.1", 12000)

client_socket.sendto(message.encode('utf-8'), addr)

data, server =client_socket.recvfrom(1024)
response = data.decode('utf-8')
print(response)
