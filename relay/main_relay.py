"""
Relays API request to an OpenComputer instance.
"""

import socketserver
import threading
from threading import Thread
from typing import List

TCP_IP = ''
TCP_PORT = 5002
BUFFER_SIZE = 1024

buffer: List[str] = []


class Handler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        if len(buffer) > 0:
            self.request.send(buffer.pop(0).encode('utf-8'))
        else:

            self.request.send("\0\1\0\1\0\n".encode('utf-8'))


class Relay:
    sock: socketserver

    def send(self, msg: str):
        if not msg.endswith('\n'):
            msg += '\n'
        buffer.append(msg)

    def __init__(self):
        self.sock = socketserver.TCPServer(("127.0.0.1", 5002), Handler)
        server_thread: Thread = threading.Thread(target=self.sock.serve_forever, daemon=True)
        server_thread.start()



