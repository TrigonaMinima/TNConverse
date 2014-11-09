from socket_class import mysocket
import time

bcast_addr = '255.255.255.255'
bcast_port = 54554

# Create a broadcast socket object
sock = mysocket()
sock.set_socket(bcast_addr, bcast_port)
sock.binding(bcast_addr, bcast_port)
print("Made a broadcast socket...\n")


start = time.clock()

while True:
    sender = "Programmer (" + time.ctime(time.time()) + ") : "
    sender = sender + "0. Broadcast your message?\n"
    sender = sender + "1. Recieve some broadcast?\nChoice? (0/1) : "
    mode = input(sender)
    # Broadcasting mode
    if mode == '0':
        sock.mysendto(mode, bcast_addr, bcast_port)
        sender = "Broadcast message (" + time.ctime(time.time()) + ") : "
        msg = input(sender)
        sock.mysendto(msg, bcast_addr, bcast_port)
    # Receiving mode
    elif mode == '1':
        sock.mysendto(mode, bcast_addr, bcast_port)

        msg, addr = sock.myrecvfrom()
        while True:
            msg, addr = sock.myrecvfrom()
            # if msg == '':
            #     break
            sender = "Broadcast by " + \
                str(addr) + " (" + time.ctime(time.time()) + ") : "
            print(sender + msg)
            # msg = ''
            break
    # Bad input handling
    else:
        sender = "Programmer (" + time.ctime(time.time()) + ") : "
        print(sender + "Wrong choice!!")

    # Close the server after some time
    if (time.clock() - start) > 0.3:
        print("\nIt's time for the server to sleep. Bye bye.")
        sock.close()
        break
