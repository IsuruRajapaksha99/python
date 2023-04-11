import socket
port = 1235
address='127.0.01'
BUF_SIZE=1024

#creating socket object name 'con'
con=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con.connect((address,port))

message="Hello"
con.send(bytes(message, "utf-8"))

data=con.recv(BUF_SIZE)
con.close()
print(data.decode("utf_8"))