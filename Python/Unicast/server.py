import socket
import time
# from socket_class import mysocket

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("localhost", 1234))
serversocket.listen(5)
print("Server is listening...\n")

MSGLEN = 1024


def mysend(sock, msg):
    totalsent = 0
    size = str(len(msg)).zfill(4)
    sock.send(size.encode('utf8'))
    while totalsent < len(msg):
        sent = sock.send((msg[totalsent: totalsent + MSGLEN]).encode('utf8'))
        totalsent = totalsent + sent


def myreceive(sock):
    size = int((sock.recv(4)).decode('utf8'))
    msg = ''
    while size > 0:
        chunk = sock.recv(MSGLEN)
        msg = msg + chunk.decode("utf8")
        size -= MSGLEN
    return msg

start = time.clock()

while True:
    (clientsocket, address) = serversocket.accept()
    print("Got a connection from %s\n" % str(address))

    # mode has the following values
    # 0 - receive from the client socket
    # 1 - send to the client socket
    # 2 - break the connection
    while 1:
        print("Server (" + time.ctime(time.time()) + ") : 0. Send a message")
        print(
            "1. Recieve a message\n2. Break the connection\n\nChoice (0/1/2)?")
        mode = myreceive(clientsocket)
        msg = ''
        if mode == '2':
            print("*Recieved break connection mode.*")
            mysend(clientsocket, "Ok, bye.")
            print(
                "Server (", time.ctime(time.time()), ") : Ok, bye.\n")
            clientsocket.close()
            break
        elif mode == '1':
            print("*Recieved send message mode.*")
            sender = "Server (" + time.ctime(time.time()) + ") : "
            msg = input(sender)
            mysend(clientsocket, msg)
        elif mode == '0':
            print("*Recieved recieve message mode.")
            msg = myreceive(clientsocket)
            sender = "Client (" + time.ctime(time.time()) + ") : "
            print(sender, msg)
        else:
            sender = "Server (" + time.ctime(time.time()) + ") : "
            print(sender + "Sorry, wrong choice!!")

    if (time.clock() - start) > 0.3:
        print("\nIt's time for the server to sleep. Bye bye.")
        clientsocket.close()
        break

    print("\nServer is FREE now.")


print("Server is shutting down.")
serversocket.close()
