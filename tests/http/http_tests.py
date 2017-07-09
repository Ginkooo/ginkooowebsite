from src.http.http_request import HttpRequest
from unittest import TestCase


class HttpRequestTests(TestCase):

    def check_if_can_encaplulate_http_request(self):
        request = HttpRequest(b'GET /favicon.ico HTTP/1.1\r\n' +
                              b'User-Agent: Mozilla 5.0\r\n\r\n')
        self.assertEqual(request.params['user-agent'], b'Mozilla 5.0')
