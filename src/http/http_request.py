class HttpRequest:
    def __init__(self, data: bytes):
        first_nl_idx = data.find(b'\r\n')
        header = data[:first_nl_idx]
        method, url, version = header.split(b' ')
        double_nl_idx = data.find(b'\r\n\r\n')

        params = data[first_nl_idx + 2:double_nl_idx]


        self.method = method
        self.url = url
        self.version = version

        for param in params.splitlines():
            key, value = param.split(b':', 1)
