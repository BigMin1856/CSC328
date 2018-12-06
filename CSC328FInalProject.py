import sys , socket , os

# /************************************************************/
# /* Author: Marc Minnick                                     */
# /* Major: Information Technology                            */
# /* Creation Date: November 10th, 2018                       */
# /* Due Date: November 20th, 2018                            */
# /* Course: CSC328 020                                       */
# /* Professor Name: Dr. Frye                                 */
# /* Assignment: Final Project                                */
# /* Filename: FinaleProject328.py                            */
# /* Purpose: This program will establish a server for clients*/
#             connect and download files                      */
# /************************************************************/


port_num = 2048 # Establish Default Port Number
bind_ip = "0.0.0.0" # Establish IP Address

def crtSock():  
    server = socket.socket(family=socket.AF_INET , type=socket.SOCK_STREAM)  # Creating socket to server

    server.bind((bind_ip,port_num)) # Binds IP and Port number

    server.listen(5) #Establishes the queue length for the server

    print("Listening on {}".format(bind_ip))

    client_sock, address = server.accept() # Waits for incoming connection
    print("Connected to: {} : {}".format(address[0],address[1]))

    rtrnlst = [client_sock , address , server]

    return rtrnlst

def clientHandler(rtrnlist):
    client_sock = rtrnlist[0]
    address = rtrnlist[1]
    server = rtrnlist[2]
    first = True
    while True:
        if first == True:
            try:
                client_sock.send("HELLO".encode(encoding='utf-8'))
                first = False
            except:
                print("Error Connecting")

        
        data = client_sock.recv(10) #Recieves the commands from the client
        message = data.decode() # Decoding the message from the client

        if message == "DIR":
            ListDir(client_sock)

        if message == "PWD":
            pwd(client_sock)

        if message == "CD":
            cd(client_sock , message)

        if message == "DOWNLOAD":
            print("DOWNLOAD CMD RCVD")
            download(client_sock)

        if message == "BYE":
            server.close()
            print("Connection to: {} : {} has been terminated".format(address[0],address[1]))
            break

    return client_sock

def pwd(client_sock):
    try:
        drct = os.getcwd()
        client_sock.send(drct.encode(encoding='utf-8'))

    except socket.error as error:
        print("Could Not Fetch Working Directory\n")
        print("Error: " , error)

def ListDir(client_sock):
    print("DIR COMMAND RECEIVED")
    try:
        dirlist = os.listdir()

        client_sock.send(str(dirlist).encode(encoding='utf-8'))

    except socket.error as error:
        print("Could Not Fetch Directory Listing")
        print("Error: " , error)

    
def cd(client_sock , message):
    path = client_sock.recv(1024)
    
    try:
        ndrct = os.chdir(path)
        cwd = os.getcwd()
        client_sock.send(cwd.encode(encoding='utf-8'))

    except socket.error as error :
        msg = "ERROR: {}".format(error)
        data = msg.encode(encoding='utf-8')
        client_sock.send(data)



def download(client_sock):
    filename = client_sock.recv(30) #getting filename from client
    filename = filename.decode() #decoding name
    f = open(filename, 'rb')
    
    while True:
        l = f.read(1024)
        client_sock.send(l)
        print("Sent {}".format(repr(l)))
        if len(l) == 0:
            break
        #l = f.read(1024)
    f.close()

    print("Done Sending")

rtrnlist = crtSock()
client_sock = clientHandler(rtrnlist)
pwd(client_sock)
