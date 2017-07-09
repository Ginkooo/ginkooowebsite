import socketserver
from . import handler
from config import settings


class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(2048).strip()
        response = handler.handle(self.data)
        self.request.sendall(response)


def start():
    server = socketserver.TCPServer((settings.HOST, settings.PORT),
                                    RequestHandler)
    server.allow_reuse_address = settings.DEBUG
    server.serve_forever()
