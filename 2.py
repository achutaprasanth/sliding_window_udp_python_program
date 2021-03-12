import socket
import sys
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1',10045)
print("Connection Established...")
window_size = int(input("Enter the size of buffer window " ))
n=1
while(n <= window_size):
    print("Enter the data ",n," : " )
    data = input()
    sent = sock.sendto(data.encode('ASCII'),server_address)
    print("Data sent to server...")
    data,server = sock.recvfrom(4096)
    result=data.decode('ASCII')
    print("From Server : " , result)
    n = n+1
print("Window size Exceeded...")    
sock.close()
