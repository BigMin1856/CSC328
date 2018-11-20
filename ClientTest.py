#******************************************************************
#
# Author: Leo Atkinson
# Major: Computer Science - Software Development
# Course: Csc328 - Network Programming
# Professor: Dr. Frye
# Date: November 19th, 2018
# Language: Python 2.7.12
# Filename: client.py
# Purpose: Provides client-side interface for a download server.
#			Takes cmd line input.
# Execution command: python client.py <IP Address> <port no.>
#
#****************************************************************

import sys
import socket
import random

#default port number
port_number = 2048
max_size = 8192

def main(port_number):

	if len(sys.argv) == 2:
		hostIP = sys.argv[1]
	elif len(sys.argv) == 3:
		hostIP = sys.argv[1]
		port_number = int(sys.argv[2])
	else:
		print("USAGE ERROR: Improper number of arguments.")
		print("Proper Usage: python client.py <IP Address> <port no. (optional)>")
		exit(-1)

	#logging to console information
	print("Connecting to: \nHost IP: {0} \nPort #: {1}".format(hostIP, port_number))
	
	#creating socket
	tcp_sockfd =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	#checking for failure 
	if tcp_sockfd == -1:
	   print("Socket call failed.")
	   exit(-1)

	try:
		#establish connection
		tcp_sockfd.connect((hostIP,port_number))
	except socket.error as error:
		print(error)
		exit(-1)

	try:
		#get message from server
		msg = tcp_sockfd.recv(max_size)
	except socket.error as error:
		print(error)
		exit(-1)

	msg = msg.decode("utf-8").strip()

	if msg == "HELLO":
		print("Connected to: \nHost IP: {0} \nPort #: {1}".format(hostIP, port_number))

	first = True

	while(True):
		
		print("Welcome to our Client/Server Download App")
		print("\nEnter a command listed below:")
		print("PWD - Print Working Directory (not implemented)")
		print("DIR - Print Content of Current Directory (not implemented)")
		print("CD - Change Directory (not implemented)")
		print("DOWNLOAD - Download specified file (not implemented)")
		print("EXIT - Close Connection and Exit")

		user_cmd = input("\nEnter command >>>")

		user_cmd = user_cmd.strip().upper()

		if (user_cmd == "MENU"):
			print("Welcome to our Client/Server Download App")
			print("\nEnter a command listed below:")
			print("PWD - Print Working Directory (not implemented)")
			print("DIR - Print Content of Current Directory (not implemented)")
			print("CD - Change Directory (not implemented)")
			print("DOWNLOAD - Download specified file (not implemented)")
			print("EXIT - Close Connection and Exit")
			first = False
		#add extra commands
		elif (user_cmd == "EXIT"):
			tcp_sockfd.send('BYE'.encode(encoding='utf-8'))
			tcp_sockfd.close()
			exit(0)



#begin main block
if __name__ == "__main__":

	main(port_number)
