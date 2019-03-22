# coding:utf-8
import requests
import unittest
from common import readconfig

class get_request(unittest.TestCase):

    def setUp(self):
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        self.get_url = '%s'%API

    def test_url_01(self):
        """打开测试api地址"""
        url=self.get_url
        r = requests.get(url)
        print(r.text)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()