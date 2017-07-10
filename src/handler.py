from src.http.http_request import HttpRequest
from src.http.http_response import HttpResponse
import src.resolver as resolver


def handle(data: bytes) -> bytes:
    """handle
    Resolves correct action to use for requested url and
    executes it

    :param data: HTTP protocol compatible message
    :type data: bytes

    :rtype: bytes - bytes to send back to client
    """
    http_request = HttpRequest(data)
    url = http_request.url
    resolved = resolver.resolve_method_and_args_from_url(url)
    if not resolved:
        return HttpResponse(http_request,  # TODO Make some nice 404 page
                            b'Not found',
                            404).get_as_bytes()
    method, args, kwargs = resolved
    response = method(http_request, *args, **kwargs)
    return response.get_as_bytes()
