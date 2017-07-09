from src.http.http_request import HttpRequest
from src.http.http_response import HttpResponse
import os
from config import settings


def dispatch(http_request: HttpRequest) -> HttpResponse:
    return HttpResponse(http_request,
                        open(os.path.join(settings.PUBLIC_DIR,
                                          'index.html'), 'rb').read())
