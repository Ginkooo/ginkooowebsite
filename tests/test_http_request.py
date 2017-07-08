import unittest
from src import handler


class HttpRequest(unittest.TestCase):

    def test_handle_returns_dupa(self):
        print('Testing handler')
        response = handler.handle(b'picza')
        self.assertEqual(response, b'dupa')
