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
        self.request.send(buffer.pop(0))


class Relay(object):
    sock: socketserver

    def send(self, msg: str):
        if not msg.endswith('\n'):
            msg += '\n'
        buffer.append(msg)

    def __init__(self):
        self.sock = socketserver.TCPServer(("whydoyouhate.me", 5002), Handler)
        server_thread: Thread = threading.Thread(target=self.sock.serve_forever, daemon=True)
        server_thread.run()



