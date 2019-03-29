import socket
import time
from threading import Thread

def handleConnection(server, data, clientAddress):
	message = data.decode()
		
	#Process and Present the Data:
	print("->-> Data Received: ",message, "\n From :",clientAddress)

	#Server respond back to the Client(Echo the message back to the Client)
	modifiedData = (message.upper()).encode()
	server.sendto(modifiedData, clientAddress)
	
	print("<-<- Sent back to client :",clientAddress) 				 
	print("_____________________________________________________")
	print("-> Sever ready to recieve ")

def Main():
	print("====================================================")
	print("=             UDP SERVER is ONLINE                 =")
	print("====================================================")
	print(" ")

	# Port and Host initialization
	server 	   = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)		# creates a UDP socket.
	host 	   = 'Dlab99'  	# sever IP (localhost)
	port	   = 13000	    # Port to recive from on (non-privileged ports are > 1023)
	bufferSize = 1024
	ExitCmnd   = "exit"
	address	   = (host,port)
	
	
	server.bind(address)	# Attaches the socket with the IP adress and port number
	
	print("-> The name of the Host is: ", host)
	print("-> Sever ready to recieve ")
	
	# non-Persistent connection
	print("_____________________________________________________")
	#read the data from the connection into a size 1024 bytes buffer
	while True:
		data, clientAddress  = server.recvfrom(bufferSize) 
		try:
			clientThread = Thread(target=handleConnection, args=(server, data, clientAddress))
			clientThread.start()
			clientThread.join()
		except Exception:
			print("Error while creating a thread")		
		#End_Try
		
	#End while


	print("Server is OFFLINE")
	time.sleep(2)
	print(" ")

if __name__ == '__main__':
		Main()
