from src.http.http_request import HttpRequest
from unittest import TestCase


class HttpRequestTests(TestCase):

    def check_if_can_encaplulate_GET_http_request(self):
        request = HttpRequest(b'GET /favicon.ico HTTP/1.1\r\n' +
                              b'User-Agent: Mozilla 5.0\r\n\r\n')
        self.assertEqual(request.params['user-agent'], b'Mozilla 5.0')

    def check_if_can_encaplulate_POST_http_request_with_body(self):
        request = HttpRequest(b'POST /favicon.ico HTTP/1.1\r\n' +
                              b'User-Agent: Mozilla 5.0\r\n\r\n' +
                              b'content-leght: 28' +
                              b'username=Ginko&password=asdf')
        self.assertEqual(request.post['username'], b'Ginko')
