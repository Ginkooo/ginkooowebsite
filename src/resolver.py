import os
import importlib.util
from config import settings


def get_parts_of_url(url: str) -> tuple:
    """get_parts_of_url
    takes the url and splits it into parts, meaning:
    controller, action, params and query string params

    :param url: url to split into parts
    :type url: str

    :returns: (controller, action, params, query string params)
    :rtype: tuple
    """
    if '?' in url:
        url, query_string = url.split('?', 1)
    url = url.strip('/')
    params = []
    qs_params = {}
    parts = url.split('/')
    if len(parts) > 1:
        controller, action, *params = parts
    else:
        controller = settings.DEFAULT_CONTROLLER if not url else parts[0]
        action = settings.DEFAULT_ACTION
    try:
        query_string
    except NameError:
        return (controller, action, params, qs_params)
    temps = query_string.split('&')
    for t in temps:
        key, value = t.split('=', 1)
        qs_params[key] = value
    return (controller, action, params, qs_params)


def resolve_method_and_args_from_url(url: bytes) -> tuple:
    """resolve_method_and_args_from_url
    gets url and returns function which is supposed to be executed

    :param url: url to resolve
    :type url: bytes

    :returns: function to execute
    :rtype: tuple
    """
    url = url.decode('utf-8')
    if '?' in url:
        url, query_string = url.split('?')
    controller, action, params, qs_params = get_parts_of_url(url)
    controller = controller + '.py'

    path = os.path.join('controllers', controller)
    if not(os.path.exists(path) and os.path.isfile(path)):
        print('There is no controller {}'.format(controller))
        return None

    kwargs = {}
    try:
        query_string
        for key, value in query_string.split('='):
            kwargs[key] = value
    except:
        pass

    filename = os.path.basename(path).split('.')[0]
    spec = importlib.util.spec_from_file_location(filename, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    function = getattr(module, action)
    return (function, params, kwargs)


def resolve_resource_path_from_url(url: bytes) -> str:
    parts = url.decode('utf-8').strip().strip('2%').split('/')
    path = os.path.join('public', *parts)
    print(f'path is {path}')
    return path
