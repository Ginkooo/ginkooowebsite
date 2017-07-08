class HttpRequest:
    def __init__(self, data: bytes):
        length = len(data)
        first_nl_idx = data.find(b'\r\n')
        header = data[:first_nl_idx + 1]
        method, url, version = header.split(b' ')
        double_nl_idx = data.find(b'\r\n\r\n')

        params = data[first_nl_idx + 2:double_nl_idx + 1]

        print(method, url, version)
        print(params)

        self.method = method
        self.url = url
        self.version = version
