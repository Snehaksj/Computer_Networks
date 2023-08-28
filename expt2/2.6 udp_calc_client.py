import socket

client_socket =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


num1=input("Enter number 1:")
num2=input("Enter number 2:")
op=input("Enter operator:")
l=num1+num2+op
print("Sending data to server...")

addr = ("127.0.0.1", 12000)

client_socket.sendto(l.encode('utf-8'), addr)

data, server =client_socket.recvfrom(1024)
response = data.decode('utf-8')
print("Receieved message from server:",response)
