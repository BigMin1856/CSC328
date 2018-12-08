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
import os

#default port number
port_number = 2048
max_size = 1024

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
		msg = msg.decode("utf-8")
	except socket.error as error:
		print("ERROR: Failure recieving message.")
		print(error)

	return(msg)


def main(port_number):

	#checking user input
	if len(sys.argv) == 2:
		hostName = sys.argv[1]
	elif len(sys.argv) == 3:
		hostIP = sys.argv[1]
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
		tcp_sockfd.connect((hostIP, port_number))
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
		print("Welcome to our Client/Server Download App")

	user_cmd = "MENU"

	dirlist = os.listdir()
	#begin user input loop
	while(True):

		#Main logic for user input
		if (user_cmd == "MENU"):
			print("\nEnter a command listed below:\n")
			print("MENU - Show List of Valid Commands")
			print("PWD - Print Working Directory")
			print("DIR - Print Content of Current Directory")
			print("CD - Change Directory (will prompt for directory name)")
			print("DOWNLOAD - Download specified file (will prompt for file name)")
			print("EXIT - Close Connection and Exit")
			first = False
		elif (user_cmd == "PWD"):
			sendMsg(tcp_sockfd, user_cmd)
			
			msg = recvMsg(tcp_sockfd)

			print(msg)

		elif (user_cmd == "DIR"):
			sendMsg(tcp_sockfd, user_cmd)
			
			msg = recvMsg(tcp_sockfd)

			if len(msg) == 0:
				print("\nNo files current in directory.")
			else:
				print("\nFiles in current directory:\n")
				msg = msg[1:-2]
				msg = msg.split(',')
				for file in msg:
					print(file)

		elif (user_cmd == "DOWNLOAD"):
			
			sendMsg(tcp_sockfd, user_cmd)
			
			writefile = input("File Name >>> ")

			if writefile in dirlist:

				while (True):
					userResp = input("Are you sure you want to overwrite {0} ? (y/n)>>> ".format(writefile))
					userResp = userResp.upper().strip()

					if((userResp == 'Y') or (userResp == 'N')):
						break
					else:
						print("Enter valid response")
						continue
				
				if (userResp == 'N'):
					print("Overwrite aborted\n")
					user_cmd = 'MENU'
					continue

			sendMsg(tcp_sockfd, writefile)
			try:
				wf = open(writefile, 'w')
				loopT = True
				while(loopT):
					msg = recvMsg(tcp_sockfd)

					if "DONE" in msg:
						msg = msg.replace('DONE', '')
						wf.write(msg)
						wf.close()
						print("{0} has successfully downloaded".format(writeFile))	
						loopT = False
						
					if msg:
						wf.write(msg)				
			except:
				print("ERROR downloading file")

		elif (user_cmd == "CD"):
			sendMsg(tcp_sockfd , user_cmd)

			path = input("Directory Name >>> ")
			tcp_sockfd.send(path.encode('utf-8'))

			msg = recvMsg(tcp_sockfd)
			print(msg)
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
		user_cmd = input("\nEnter command >>> ")

		#Normalizing user input
		user_cmd = user_cmd.strip().upper()



#begin main block
if __name__ == "__main__":

	main(port_number)
