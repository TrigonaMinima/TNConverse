import socket

MSGLEN = 1024


class mysocket:

    """
    A simple multicasting socket class to handle the receiving and sending
    of data stream.
    """

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        else:
            self.sock = sock

    def set_socket(self, b_addr, b_port):
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def binding(self, b_addr, b_port):
        self.sock.bind((b_addr, b_port))

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysendto(self, msg, b_addr, b_port):
        totalsent = 0
        size = str(len(msg)).zfill(4)
        self.sock.sendto(bytes(size, 'utf8'), (b_addr, b_port))
        while totalsent < len(msg):
            sent = self.sock.sendto(
                bytes(msg[totalsent: totalsent + MSGLEN], 'utf8'), (b_addr, b_port))
            totalsent = totalsent + sent

    def closing(self):
        self.sock.close()

    def myrecvfrom(self):
        size, addr = self.sock.recvfrom(4)
        size = int(size.decode('utf8'))
        msg = ''
        while size > 0:
            chunk, addr = self.sock.recvfrom(MSGLEN)
            msg = msg + chunk.decode("utf8")
            size -= MSGLEN
        return msg, addr
