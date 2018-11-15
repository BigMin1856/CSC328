import os , socket , threading , sys

IPBind = "10.500.5.3"
PortBind = 9000

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind((IPBind, PortBind))
server.listen(10)

print("Listening on " ,IPBind , ":", PortBind)

def client_handle(client_sock):
    reqst = client_sock.recv(10)
    client_sock.send('HELLO')
    client_sock.close()





#server.close()