Team: 		Marc Minnick & Leo Atkinson
Major: 		Computer Science - Software Development
Course: 	Csc328 - Network Programming
Professor: 	Dr. Frye
Date: 		December 4th, 2018
Language: 	Python 3
Filename: 	readme.txt
Purpose: Provides client-side interface for a download server.
			Takes cmd line input.
Compilation: Not Necessary
Execution command: python3 client.py <hostname> <port no. (optional)>
					python3 server.py <port no. (optional)>

Description:

This is an implementation of an anonymous client/server download application,
which utilizes a concurrent connection-oriented server application and an 
anonymous client application to give users a command interface.

Design Overview:

The client application will take a host name and optional port number to set-up
a TCP connection to a file server. The client application will present a menu
to the user of all possible commands to show the current server directory path 
(PWD); list the files in the current server directory (DIR); change server 
directories to a user specified server directory (CD); download a user specified 
file from the server (DOWNLOAD); and gracefully close a connection to the serve 
and end the client application (BYE).

The server application will take an optional port number and listen for and accept
a request for connection from the client program(s). The server application will
send a confirmation message ("HELLO") upon establishment of connection. The server 
application will listen for user commands sent from the client program, validate 
commands, implement the requested action and return an appropriate response from 
the contense of the file system on the server.

Protocol:

Client command implementations are discussed below. 

MENU - Client side command to print the valid commands and their explaination.

PWD - Server responds with current PATH

DIR - Server respons with a list of the contense of the current directory (files 
		and directories). Server response is parsed and formatted on client side.

CD - Client sends command, server waits for additional input. Client app asks for 
		a directory name and sends to server. Server changes to requested directory,
		if it is valid.

DOWNLOAD - Client sends command, server waits for additional input. Client app asks 
			for a file name, sends to server, and gets ready for a response by opening 
			the a new file of the same name. Server opens specified file and  begins 
			sending file in a loop of specified-sized chunks (same on both client & 
			server side). Client recieves data from server and writes it to the open 
			file until it gets message with "DONE" in it. Server and client both close 
			their open files.

EXIT - Client sends BYE message and closes socket connection. Upon reciept, server 
		closes socket connection.


Known Issues:

Server is iterative.

Not all input is validated. 

Client issues error on download, even though file downloads successfully.
