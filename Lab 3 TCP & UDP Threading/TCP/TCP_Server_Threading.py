import socket
import time
from threading import Thread

def handleConnection(connection,client_addr):
    bufferSize = 1024
    ExitCmnd   = "exit"
    print("<-> ",client_addr, " has connected to the Server")
    print("_____________________________________________________")
    #read the data from the connection into a size 1024 bytes buffer
    while True:
        data = connection.recv(bufferSize)
        #Determine when to close the Socket:
        message = data.decode()
        if message.lower() == ExitCmnd:
            #connection.sendall(("-> Connection Terminated").encode())
            connection.close()
            print("->X    Connection closed for : ", client_addr)
            print("=====================================================")
            time.sleep(1)
            break 								# break from the loop if the exit command is recieved
        else:
            #Process and Present the Data:
            print("->-> Data Received: ",message)
            #Server respond back to the Client(Echo the message back to the Client)
            message = (message.upper()).encode()
            connection.sendall(message)
            print("<-<- Sent back to client") 				 
            print("_____________________________________________________")
        #end Else if
    #End while
	

def Main():
	print("====================================================")
	print("=             TCP SERVER is ONLINE                 =")
	print("====================================================")
	print(" ")

	# Port and Host initialization
	server 	   = socket.socket(socket.AF_INET,socket.SOCK_STREAM)		# creates a TCP socket.
	host 	   = 'Dlab99'  	# Standard loopback interface address (localhost)
	port	   = 13000		# Port to listen on (non-privileged ports are > 1023)
	numConnections = 5
	address	   = (host,port)
	
	
	server.bind(address)	# Attaches the socket with the IP adress and port number
	
	print("-> The name of the Host is: ", host)
	print("-> Waiting for connections")
	
	# Persistent connection
	while True: 
		server.listen(numConnections)				# Listens for an incoming TCP connection request from the client
		connection, client_addr = server.accept()	#  request received ,creates a new socket for
													#  the connection with that particular client
		try:
			clientThread = Thread(target=handleConnection, args=(connection, client_addr))
			clientThread.start()
			clientThread.join()
		except Exception:
			print("Error while creating a thread")		
		#End_Try
	#End while	
	
	#connection.close() #close the Socket
	print("Server is OFF")
	time.sleep(2)
	print(" ")

if __name__ == '__main__':
		Main()
