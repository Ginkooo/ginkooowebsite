from src.http.http_response import HttpResponse
from src.http.http_request import HttpRequest
import src.loader as loader


def index(request: HttpRequest) -> HttpResponse:
    data = loader.get_file('public/home/index.html')
    return HttpResponse(request, data)
