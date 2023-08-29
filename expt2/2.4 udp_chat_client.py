import socket

client_socket =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr = ("127.0.0.1", 12000)

while True:
    string=input("Enter message:")
    
    print("Sending message to server...")

    client_socket.sendto(string.encode('utf-8'), addr)
    if(string=='bye'):
        break
    
    data, server =client_socket.recvfrom(1024)
    response = data.decode('utf-8')
    print("Receieved message from server:",response)
    if response=='bye':
        break
