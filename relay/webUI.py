"""
Presents a webUI
"""

import cherrypy
from relay.main_relay import Relay


class webUI(object):
    _relay = Relay()

    @cherrypy.expose
    def index(self):
        return open("../html/index.html")

    @cherrypy.expose
    def send(self, msg: str = None):
        if msg:
            self._relay.send(msg)


cherrypy.quickstart(webUI())
