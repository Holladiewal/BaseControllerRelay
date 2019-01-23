"""
Presents a webUI
"""


import cherrypy
from relay.main_relay import Relay


class WebUI:

    def __init__(self):
        self.relay = Relay()
        pass

    @cherrypy.expose
    def index(self):
        return open("./html/index.html")

    @cherrypy.expose
    def send(self, msg: str = None):
        if msg:
            self.relay.send(msg)
        return "sent: " + msg

    @cherrypy.expose
    def send_form(self):
        return open("./html/send_message.html")


# if __name__ == '__main__':
cherrypy.quickstart(WebUI())

