import sys , socket , random

port_num = 2048
bind_ip = "0.0.0.0"

server = socket.socket(family=socket.AF_INET , type=socket.SOCK_STREAM)
server.bind((bind_ip , port_num))
server.listen(5)

print("Listening on {} : {}".format(bind_ip , port_num))

def clnt_handler(client_sock):
    client_sock.send("HELLO".encode(encoding='utf-8'))

while True:
    client_sock, address = server.accept()
    print("Connected from: {} : {}".format(address[0],address[1]))
    clnt_handler(client_sock)
    data = client_sock.recv(10)
    message = data.decode()
    if message == "BYE":
        client_sock.close()
        print("Connection to {} has been terminated".format(address[0]))
        break
