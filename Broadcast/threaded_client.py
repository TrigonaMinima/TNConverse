import socket
from datetime import datetime
s = socket.socket()
host = socket.gethostname()
port = 12345

# Connecting to server.
s.connect((host, port))
print "New client added to the broadcast list at" + str(datetime.now())

para = s.recv(1024)

print "Received:"+para
