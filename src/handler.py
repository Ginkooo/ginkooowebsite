from .http.http_request import HttpRequest


def handle(data: bytes) -> bytes:
    """handle
    Handles data recieved from client and returns a response

    :param data: HTTP protocol compatible message
    :type data: bytes

    :rtype: bytes - bytes to send back to client
    """
    http_request = HttpRequest(data)
    return b'dupa'
