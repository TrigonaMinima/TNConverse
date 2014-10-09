# first of all import the socket library
import socket               

# create a socket object
s = socket.socket()         
print "Socket successfully created"

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345                

# Next bind to the port
s.bind(('', port))        
print "socket binded to %s" %(port)

# put the socket into listening mode
s.listen(5)     
print "socket is listening" 

# Establish connection with client.
c, addr = s.accept()     
print 'Got connection from', addr

# a forever loop until we interrupt it or 
while True:
    # Establish connection with client.
    x = raw_input('enter ur msg :')
    # send a message to the client. 
    c.send(x)
    # print the received msg from client side
    y = c.recv(1024)
    print "Client sent :%s" % y 
    if y == 'end':
        break
# Close the connection with the client  
c.close()