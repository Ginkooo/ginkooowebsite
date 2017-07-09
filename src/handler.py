from .http.http_request import HttpRequest
from src.dispatchers import dispatcher


def handle(data: bytes) -> bytes:
    """handle
    Handles data recieved from client and returns a response

    :param data: HTTP protocol compatible message
    :type data: bytes

    :rtype: bytes - bytes to send back to client
    """
    http_request = HttpRequest(data)
    response = dispatcher.dispatch(http_request)
    return response.get_as_bytes()
