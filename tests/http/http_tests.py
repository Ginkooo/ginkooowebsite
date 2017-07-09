from src.http.http_request import HttpRequest
from src.http.http_response import HttpResponse
from unittest import TestCase
from unittest.mock import MagicMock


class HttpRequestTests(TestCase):

    def check_if_can_encaplulate_GET_http_request(self):
        request = HttpRequest(b'GET /favicon.ico HTTP/1.1\r\n' +
                              b'User-Agent: Mozilla 5.0\r\n\r\n')
        self.assertEqual(request.params['user-agent'], b'Mozilla 5.0')

    def check_if_can_encaplulate_POST_http_request_with_body(self):
        request = HttpRequest(b'POST /favicon.ico HTTP/1.1\r\n' +
                              b'content-length: 28\r\n' +
                              b'User-Agent: Mozilla 5.0\r\n\r\n' +
                              b'username=Ginko&password=asdf')
        self.assertEqual(request.post[b'username'], b'Ginko')


class HttpResponseTests(TestCase):

    def prep(self):
        self.request = MagicMock()
        self.request.version = b'HTTP/1.1'
        self.request.params = {}
        body_len = str(len(b'example body')).encode('ascii')
        self.request.params['content-length'] = body_len

    def check_if_can_make_response_object(self):
        response = HttpResponse(self.request, b'example body')
        self.assertEqual(b'example body', response.body)

    def check_can_get_response_as_bytes(self):
        response = HttpResponse(self.request, b'example body')
        expected = self.request.version +\
            b' 200 OK\r\n' + b'content-length: ' +\
            self.request.params['content-length'] + b'\r\n\r\n' +\
            b'example body'
        self.assertEqual(expected, response.get_as_bytes())
