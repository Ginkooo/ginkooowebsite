from src.http.http_request import HttpRequest
from src.http.http_response import HttpResponse
from src import loader
from config import settings
import src.resolver as resolver


def handle(data: bytes) -> bytes:
    """handle
    decides what to do with income http message

    :param data: HTTP protocol compatible message
    :type data: bytes

    :rtype: bytes - bytes to send back to client
    """
    if settings.DEBUG:
        print()
        print('Got request like:')
        print(data)
    http_request = HttpRequest(data)
    url = http_request.url
    if user_wants_resource(url):
        path = resolver.resolve_resource_path_from_url(url)
        data = loader.get_file(path)
        to_send = HttpResponse(http_request, data).get_as_bytes()
        if settings.DEBUG:
            print()
            print('Sending a response like:')
            print(to_send)
        return to_send
    resolved = resolver.resolve_method_and_args_from_url(url)
    if not resolved:
        return HttpResponse(http_request,  # TODO Make some nice 404 page
                            b'Not found',
                            404).get_as_bytes()
    method, args, kwargs = resolved
    response = method(http_request, *args, **kwargs)
    to_send = response.get_as_bytes()
    if settings.DEBUG:
        print()
        print('Sending a response like:')
        print(to_send)
    return to_send


def user_wants_resource(url: bytes) -> bool:
    if url.decode('utf-8').\
            strip().lstrip('/').startswith(settings.RESOURCE_DIR):
        return True
    return False
