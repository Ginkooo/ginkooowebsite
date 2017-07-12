from .http_request import HttpRequest
from . import http_constants


class HttpResponse:
    """HttpResponse
    encapsulates HTTP response message"""
    def __init__(self, http_request: HttpRequest, body: bytes,
                 status: int=200):
        """__init__

        :param http_request: object containing request data
        :type http_request: HttpRequest
        :param body: HTTP response body
        :type body: bytes
        :param status: HTTP status
        :type status: int
        """
        self.body = self.prepare_body(body)
        self.params = {}
        self.version = http_request.version
        self.status = status
        self.status_info = http_constants.status_info[status]
        self.params['content-length'] = str(len(body)).encode('ascii')
        self.body = body

    def get_as_bytes(self) -> bytes:
        """get_as_bytes
        gets http message response in a form prepared to send

        :returns: HTTP response prepared for sending
        :rtype: bytes
        """
        header = self.version + b' ' +\
            str(self.status).encode('ascii') + b' ' +\
            self.status_info + b'\r\n'
        params = b''
        for key, value in self.params.items():
            params += key.encode('ascii') + b': ' + value + b'\r\n'

        blank_line = b'\r\n'
        return header + params + blank_line + self.body

    def prepare_body(self, body: bytes) -> bytes:
        """prepare_body
        prepares body for sending in http message,
        removes extra whitespace etc.

        :param body: HTTP message body
        :type body: bytes

        :returns: HTTP body prepared for sending
        :rtype: bytes
        """
        return bytes  # TODO: Prepare this body to cut extra whitespace etc.
