import socket
import sys
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host='127.0.0.1' 
port=10045 
server_address = (host,port)
sock.bind(server_address)
while True:
     data,addr = sock.recvfrom(4096) 
     if not data:
          break
     print("\nDecoding the received data...")
     x = data.decode('ASCII')
     print("Data Received is : " ,x )
     sent = sock.sendto("ACHU".encode('ASCII'), addr)
     print("ACHU send to client...")
