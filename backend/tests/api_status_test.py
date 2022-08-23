import unittest

from services.api_status import ApiStatus

class TestApiStatus(unittest.TestCase):

    def test_api_request(self):
        self.assertNotEqual(None, ApiStatus.get_market_status())