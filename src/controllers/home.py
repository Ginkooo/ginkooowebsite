from src.http.http_response import HttpResponse
from src.http.http_request import HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse(request, b'siemaneczko', 200)
