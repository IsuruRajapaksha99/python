import socket 
port = 1234
address="127.0.01"

#creating a socket object name "server"

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((address,port))
server.listen(5)
print("Listening")
while True:
    con.addr=server.accept()
    print("connection address is :",addr)
    con.send(bytes("Hello!,welcome to the server!","utf-8"))