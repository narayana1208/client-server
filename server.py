import socket
server = socket.socket()
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print  "server socket defined"
host = socket.gethostname()
#local host i.e 127.0.0.1 using this to bind it as a server socket
print host
port = 12345
server.bind((host,port))
server.listen(1)
# the following is used to read data from one client or one socket
while True:
    c,addr = server.accept()
    c.send("Thank you ,message received")
    buffer = c.recv(1024)
    c.close()
print buffer
#the following code is used to write the previously received data to another socket
google_socket = socket.socket()
google_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostbyname('www.google.co.in')
port = 80
google_socket.connect((host,port))
google_socket.send(buffer)
while True:
        message = google_socket.recv(1024)
        break
print message
google_socket.close()
