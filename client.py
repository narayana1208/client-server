import socket
client = socket.socket()
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
client.connect((host,port))
client.send("GET / HTTP/1.0\r\n\r\n")
print client.recv(1024)
