import socket

s = socket.socket()

ip = 'localhost'
port = 8000

s.bind((ip,port))
s.listen()
print("Wait for client")

c, addr = s.accept()
print ('client added !')
while True:
    msg = input (">>>")
    c.send(msg.encode())
    print (c.recv(1024).decode())
    
    
    


