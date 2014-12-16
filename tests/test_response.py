import unittest

from diablo3api import Diablo3API
from diablo3api.resources import Diablo3APIError


class Diablo3APIResponseTestCase(unittest.TestCase):

    def setUp(self):
        self.api = Diablo3API()

    def test_request_headers(self):
        r = self.api.profile.response('testuser-1234')
        self.assertTrue('User-Agent' in r.request.headers)
        self.assertEqual(r.request.headers['User-Agent'], 'Diablo 3 Python API Wrapper')

    def test_404_item_response(self):
        r = self.api.item.response('bad-item-id')
        self.assertEqual(r.status_code, 404)

    def test_404_raises_APIError(self):
        self.assertRaises(Diablo3APIError, lambda: self.api.item.get('bad-item-id'))
