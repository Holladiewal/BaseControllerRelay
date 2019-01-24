"""
Relays API request to an OpenComputer instance.
"""

import socketserver
from socket import socket
import threading
from threading import Thread
from typing import List, Dict, Tuple

TCP_IP = '127.0.0.1'
TCP_PORT = 5002

buffer: List[str] = []
ls_response: Dict[str, List[Tuple[str, str]]] = {}


class Handler(socketserver.BaseRequestHandler):

    def handle(self):
        sock: socket = self.request
        data = sock.recv(4096)

        if data:
            message: str = data.decode('utf-8').casefold()
            if message == "getmessage":
                if len(buffer) > 0:
                    self.request.send(buffer.pop(0).encode('utf-8'))
                    return
            elif message.startswith("list"):
                message = message.replace("list ", "", 1)
                parts = message.split('\0\1')
                ls_response[parts[0]] = []
                for part in parts[1].split('\r'):
                    ls_response[parts[0]].append(part)

        self.request.send("\0\1\0\1\0\n".encode('utf-8'))


class Relay:
    sock: socketserver

    def send(self, msg: str):
        if not msg.endswith('\n'):
            msg += '\n'
        buffer.append(msg)

    def __init__(self):
        self.sock = socketserver.TCPServer((TCP_IP, TCP_PORT), Handler)
        server_thread: Thread = threading.Thread(target=self.sock.serve_forever, daemon=True)
        server_thread.start()



