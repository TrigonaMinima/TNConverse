# Import socket module
import socket               

# Create a socket object
s = socket.socket()         

# Define the port on which you want to connect
port = 12345                

# connect to the server on local computer
s.connect(('127.0.0.1', port))
while True:
    # receive data from the server
    print "Server sent :%s" % s.recv(1024)
    x = raw_input('enter ur msg :')
    #sending message to the server
    s.send(x)
    if x == 'end':
        break
# close the connection
s.close()