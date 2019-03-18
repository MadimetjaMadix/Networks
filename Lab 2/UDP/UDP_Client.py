import socket
import time

def Main():
	print("====================================================")
	print("=            UDP CLIENT is turned ON               =")
	print("====================================================")
	print(" ")

	# Port and Host initialization
	client 	   = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)		# creates a UDP socket.
	host 	   = 'Dlab99'  	# Standard loopback interface address (localhost)
	port	   = 13000			# Port to listen on (non-privileged ports are > 1023)
	bufferSize =  1024
	ExitCmnd   = "exit"
	address	   = (host,port)
	
	while True:
		message = input(str(" Type message to send: "))
		print("->-> CLIENT: ",message)
		message  = message.encode()
		if (message.decode()).lower() == ExitCmnd:
			client.close()
			print("XXXXXXX    Connection Terminated     XXXXXX")
			time.sleep(3)
			break
		client.sendto(message,address)
		modifiedMessage, serverAddress = client.recvfrom(bufferSize) 
		print("<-<- SERVER: ", modifiedMessage.decode())
		print("->-> ")
	
	client.close()


if __name__ == '__main__':
		Main()
