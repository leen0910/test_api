# coding:utf-8
import requests
import unittest
# from readconfig import ReadConfig
import readconfig

class get_request(unittest.TestCase):

    def setUp(self):
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        self.get_url = '%s'%API

    def test_url_01(self):
        url=self.get_url
        r = requests.get(url)
        print(r.text)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()