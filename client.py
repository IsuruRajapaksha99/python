import socket
port = 1234
address='127.0.01'
BUF_SIZE=1024

#creating socket object name 'con'
con=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con.connect((address,port))

data=con.recv(BUF_SIZE)
con.close()
print(data.decode("utf_8"))