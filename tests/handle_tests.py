import unittest
from src import handler


class HandleTests(unittest.TestCase):

    def check_handle_returns_dupa(self):
        print('Testing handler')
        response = handler.handle(b'GET /favicon.ico HTTP/1.1\r\n' +
                                  b'User-Agent: Mozilla 5.0\r\n\r\n')
        self.assertEqual(response, b'dupa')
