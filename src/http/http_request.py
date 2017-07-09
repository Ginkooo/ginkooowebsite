class HttpRequest:
    """HttpRequest
    encapsulates HTTP request message"""
    def __init__(self, data: bytes):
        """__init__
        constructor makes a HttpRequest from bytes

        :param data: bytes of HTTP request message
        :type data: bytes
        """
        first_nl_idx = data.find(b'\r\n')
        header = data[:first_nl_idx]
        method, url, version = header.split(b' ')
        double_nl_idx = data.find(b'\r\n\r\n')

        params = data[first_nl_idx + 2:double_nl_idx]
        body = data[double_nl_idx + 4:]

        self.method = method
        self.url = url
        self.version = version
        self.params = {}
        self.body = body

        for param in params.splitlines():
            key, value = param.split(b':', 1)
            key = key.decode('ascii').lower()
            self.params[key] = value.strip()
