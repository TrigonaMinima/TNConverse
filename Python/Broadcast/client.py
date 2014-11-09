from socket_class import mysocket
import time

bcast_addr = '255.255.255.255'
bcast_port = 54554

# Create a broadcast socket object
sock = mysocket()
sock.set_socket(bcast_addr, bcast_port)
sock.binding(bcast_addr, bcast_port)
print("New client added to the broadcast list...")


while True:
    mode, addr = sock.myrecvfrom()
    if mode == '0':
        print("*Receiving mode*")
        msg, addr = sock.myrecvfrom()
        sender = "Broadcast by " + \
            str(addr) + " (" + time.ctime(time.time()) + ") : "
        print(sender + msg)
    elif mode == '1':
        print("*Announcing mode*")
        sender = "Server (" + time.ctime(time.time()) + ") : "
        sender = sender + "0. Broadcast your message?\n"
        sender = sender + "1. Recieve some broadcast?\nChoice? (0/1) : "
        inner_mode = input(sender)
        if inner_mode == '0':
            print("*Receiving mode*")
            msg, addr = sock.myrecvfrom()
            sender = "Broadcast by " + \
                str(addr) + " (" + time.ctime(time.time()) + ") : "
            print(sender + msg)
        elif inner_mode == '1':
            print("*Announcing mode*")
            sender = "Broadcast message (" + time.ctime(time.time()) + ") : "
            msg = input(sender)
            sock.mysendto(msg, bcast_addr, bcast_port)
