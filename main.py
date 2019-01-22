"""
Presents a webUI
"""


import cherrypy
from relay.main_relay import Relay


class webUI(object):
    relay = Relay()

    @cherrypy.expose
    def index(self):
        return open("./html/index.html")

    @cherrypy.expose
    def send(self, msg: str = None):
        if msg:
            if not self.relay.setUp_done:
                self.relay.setUp()
                self.relay.accept()
            self.relay.send(msg)


if __name__ == '__main__':
    cherrypy.quickstart(webUI())

