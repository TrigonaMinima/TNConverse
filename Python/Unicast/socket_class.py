import socket

MSGLEN = 1024


class mysocket:

    """
    A simple socket class to handle the receiving and sending of data stream.
    """

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        size = str(len(msg)).zfill(4)
        self.sock.send(size.encode('utf8'))
        while totalsent < len(msg):
            sent = self.sock.send(
                (msg[totalsent: totalsent + MSGLEN]).encode('utf8'))
            totalsent = totalsent + sent

    def closing(self):
        self.sock.close()

    def myreceive(self):
        size = int((self.sock.recv(4)).decode('utf8'))
        msg = ''
        while size > 0:
            chunk = self.sock.recv(MSGLEN)
            msg = msg + chunk.decode("utf8")
            size -= MSGLEN
        return msg
