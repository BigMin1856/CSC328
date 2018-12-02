#!/usr/bin/env python3

#******************************************************************
#
# Author: Leo Atkinson
# Partner: Marc Minnick
# Major: Computer Science - Software Development
# Course: Csc328 - Network Programming
# Professor: Dr. Frye
# Date: November 19th, 2018
# Language: Python 3
# Compilation: Not Necessary
# Filename: client.py
# Purpose: Provides client-side interface for a download server.
#			Takes cmd line input.
# Execution command: python3 client.py <IP Address> <port no.>
#
#****************************************************************

import sys
import socket
import random

#default port number
port_number = 2048
max_size = 8192

def sendMsg(tcp_sockfd, msg):
	try:
		tcp_sockfd.send(msg.encode(encoding='utf-8'))
	except socket.error as error:
		print("ERROR: Failure sending to server.")
		print(error)

def recvMsg(tcp_sockfd):
	try:
		#get message from server
		msg = tcp_sockfd.recv(max_size)
		#decoding message
		msg = msg.decode("utf-8").strip()
	except socket.error as error:
		print("ERROR: Failure recieving message.")
		print(error)

	return(msg)


def main(port_number):

	#checking user input
	if len(sys.argv) == 2:
		hostName = sys.argv[1]
	elif len(sys.argv) == 3:
		hostName = sys.argv[1]
		port_number = sys.argv[2]
	else:
		print("USAGE ERROR: Improper number of arguments.")
		print("Proper Usage: python client.py <hostname> <port no. (optional)>")
		exit(-1)

	#get ip by hostname
	hostIP = socket.gethostbyname(hostName)

	#logging to console information
	print("Connecting to {0}: \nHost IP: {1} \nPort #: {2}".format(hostName, hostIP, port_number))
	
	#creating socket
	tcp_sockfd =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	#checking for failure 
	if tcp_sockfd == -1:
	   print("ERROR: Socket call failed.")
	   exit(-1)

	try:
		#establish connection
		tcp_sockfd.connect((iphost, portNo))
	except socket.error as error:
		print("ERROR: Connection to server failed.")
		print(error)
		exit(-1)

	try:
		#get message from server
		msg = tcp_sockfd.recv(max_size)
	except socket.error as error:
		print("ERROR: Failure recieving message.")
		print(error)
		exit(-1)
	#decoding message
	msg = msg.decode("utf-8").strip()

	if msg == "HELLO":
		print("Connected to: \nHost IP: {0} \nPort #: {1}".format(hostIP, port_number))

	user_cmd = "MENU"

	#begin user input loop
	while(True):

		#Main logic for user input
		if (user_cmd == "MENU"):
			print("Welcome to our Client/Server Download App")
			print("\nEnter a command listed below:")
			print("PWD - Print Working Directory (not implemented)")
			print("DIR - Print Content of Current Directory (not implemented)")
			print("CD - Change Directory (not implemented)")
			print("DOWNLOAD - Download specified file (not implemented)")
			print("EXIT - Close Connection and Exit")
			first = False
		elif (user_cmd == "PWD"):
			sendMsg(tcp_sockfd, user_cmd)
			
			msg = recvMsg(tcp_sockfd)

			print(msg)

		elif (user_cmd == "DIR"):
			sendMsg(tcp_sockfd, user_cmd)
			
			msg = recvMsg(tcp_sockfd)

			print(msg)

		elif (user_cmd == "CD"):

		elif (user_cmd == "DOWNLOAD"):

		elif (user_cmd == "EXIT"):
			try:
				tcp_sockfd.send("BYE".encode(encoding='utf-8'))
				tcp_sockfd.close()
			except socket.error as error:
				print("ERROR: Failure recieving message.")
				print(error)
				exit(-1)
			print("\nConnection to {0} closed. Goodbye.".format(hostIP))
			exit(0)
		else:
			print("Invalid Command. Please try your command again.")

		#Asking for and storing user input
		user_cmd = input("\nEnter command >>>")

		#Normalizing user input
		user_cmd = user_cmd.strip().upper()



#begin main block
if __name__ == "__main__":

	main(port_number)
