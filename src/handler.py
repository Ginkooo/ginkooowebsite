from .http.http_response import HttpResponse
from .http.http_request import HttpRequest


def handle(data: bytes) -> HttpResponse:
    http_request = HttpRequest(data)
    return b'hey'
