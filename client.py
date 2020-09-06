import socket

s = socket.socket()

ip = 'localhost'
port = 8000

s.connect((ip,port))
print ('Connected ! ')

while True:
    print(s.recv(1024).decode())
    msg = input (">>>")
    s.send(msg.encode())
