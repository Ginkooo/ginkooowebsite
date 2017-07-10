import socketserver
from . import handler
from config import settings


class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(2048).strip()
        response = handler.handle(self.data)
        self.request.sendall(response)


def start():
    socketserver.TCPServer.allow_reuse_address = settings.DEBUG
    server = socketserver.TCPServer((settings.HOST, settings.PORT),
                                    RequestHandler)
    server.serve_forever()
