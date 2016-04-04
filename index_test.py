import logging
import unittest

import index

class TestIndex(unittest.TestCase):
    def setUp(self):
        logging.basicConfig()

        self.event = {
            "url": "http://httpbin.org/post",
            "payload": {
                "foo": "bar"
            }
        }
        self.context = {}

    def test_proxies_request(self):
        response = index.proxy_request(self.event, self.context)
        self.assertEqual(self.event["payload"], response["form"])

if __name__ == '__main__':
    unittest.main()
