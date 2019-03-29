import socket
import time

def Main():
	print("====================================================")
	print("=            TCP CLIENT is turned ON               =")
	print("====================================================")
	print(" ")

	# Port and Host initialization
	client 	   = socket.socket(socket.AF_INET,socket.SOCK_STREAM)		# creates a TCP socket.
	host 	   = 'Dlab99'  	# Standard loopback interface address (localhost)
	port	   = 13000			# Port to listen on (non-privileged ports are > 1023)
	bufferSize =  1024
	ExitCmnd   = "exit"
	address	   = (host,port)
	
	try:
		client.connect(address) # test connection 
	except:
		print("X			Failled to connect to the Server		")
		time.sleep(3)
		return
	
	print("             Connected to the Server				")
	print(" ")
	
	while True:
		message = input(str(" Type message to send: "))
		print("->-> CLIENT: ",message)
		message  = message.encode()
		client.sendall(message)
		if (message.decode()).lower() == ExitCmnd:
			client.close()
			print("XXXXXXX    Connection Terminated     XXXXXX")
			time.sleep(3)
			break
		response = client.recv(bufferSize)
		print("<-<- SERVER: ", response.decode())
		print("->-> ")
	
	client.close()


if __name__ == '__main__':
		Main()
