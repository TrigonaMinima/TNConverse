from socket_class import mysocket
import time

# create an INET, STREAMing socket
s = mysocket()

port = 1234
s.connect("localhost", port)

print("Connected to the server...\n")

while 1:
    print("Server (" + time.ctime(time.time()) + ") : 0. Send a message")
    print("1. Recieve a message\n2. Break the connection\n\nChoice (0/1/2)?")
    sender = "Me (" + time.ctime(time.time()) + ") : "
    mode = input(sender)
    msg = ''
    s.mysend(mode)
    if mode == '2':
        msg = s.myreceive()
        sender = "Server (" + time.ctime(time.time()) + ") : "
        print(sender + msg)
        s.closing()
        break
    elif mode == '1':
        sender = "Server (" + time.ctime(time.time()) + ") : "
        msg = s.myreceive()
        print(sender + msg)
    elif mode == '0':
        sender = "Me (" + time.ctime(time.time()) + ") : "
        msg = input(sender)
        s.mysend(msg)
    else:
        sender = "Server (" + time.ctime(time.time()) + ") : "
        print(sender + "Sorry, wrong choice!!")


# while 1:

#     msg = s.myreceive()
#     print("Server sent : ", msg)

#     x = input('enter ur msg : ')
#     s.mysend(x.encode('utf-8'))

#     if x == 'end':
#         break
