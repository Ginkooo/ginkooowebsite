import socketserver
import handler
import settings


class RequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.read(2048).strip()
        response = handler.handle(self.data)
        self.request.sendall(response)


def start():
    """starts serverloop"""
    server = socketserver.TCPServer((settings.HOST, settings.PORT), RequestHandler)
    server.allow_reuse_address = settings.DEBUG
    server.serve_forever()
