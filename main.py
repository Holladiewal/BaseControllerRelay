"""
Presents a webUI
"""


import cherrypy
from relay.main_relay import Relay
import relay.main_relay


class WebUI:

    def __init__(self):
        self.relay = Relay()

    @cherrypy.expose
    def index(self):
        return open("./html/index.html")

    @cherrypy.expose
    def send(self, msg: str = None):
        if msg:
            self.relay.send(msg)
        return "sent: " + msg

    @cherrypy.expose
    def send_form(self, list_devices="generic"):
        relay.main_relay.ls_response["generic"] = [("/send_form?list_devices=ae", "AE controller"),
                                                   ("/send_form?list_devices=power", "Power Controller")]
        relay.main_relay.ls_response["power"] = [("/send?msg=power\0\1 shutdown mains", "Power main"), ("", "Quarry Power")]
        if list_devices not in relay.main_relay.ls_response.keys():
            relay.main_relay.ls_response[list_devices] = []
        html: str = ''.join(open("./html/send_message.html").readlines())

        html_list_part: str = "<li> <a href={k}>{v}</a> </li>"
        html_list: str = ""
        for k, v in relay.main_relay.ls_response[list_devices]:
            html_list += html_list_part.format(k=k, v=v)

        return html.format(html_list)

    def generate_list(self) -> str:
        pass


if __name__ == '__main__':
    cherrypy.quickstart(WebUI())

