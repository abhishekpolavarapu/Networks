# Import socket module
from socket import *    

# First create a TCP server socket
#(AF_INET is used for IPv4 protocols)

sSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 7777

# Bind the socket to server address and server port
sSocket.bind(("", serverPort))

# Listen to at most 1 connection at a time
sSocket.listen(1)

# Server should be running and wait for the incoming connections
while True:
	print 'Ready to make a connection'
	
	# Set up a new connection from the client
	connectionSocket, addr = sSocket.accept()
	
	# If an exception occurs during the execution of try clause
	# the rest of the clause is skipped
	# If the exception type matches the word after except
	# the except clause is executed
	try:
		# Receives the request message from the client
		message =  connectionSocket.recv(1024)
		# Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
		filename = message.split()[1]
		# Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character 
		f = open(filename[1:])
		# Store the entire contenet of the requested file in a temporary buffer
		Optdata = f.read()
		# Send the HTTP response header line to the connection socket
		connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")
 
		# Send data of the requested file to the connection socket
		for i in range(0, len(Optdata)):  
			connectionSocket.send(Optdata[i])
		connectionSocket.send("\r\n")
		
		# Close the client's connection
		connectionSocket.close()

	except IOError:
		# if a file is not found send a HTTP message
		connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
		connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
		# Close the client's connection
		connectionSocket.close()

sSocket.close()