# coding:utf-8
import requests
import unittest
from common import readconfig

class get_request(unittest.TestCase):

    def setUp(self):
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        self.get_url = '%s'%API

    def test01_url_home(self):
        """get页面:首页"""
        url=self.get_url+'/#/main/(router-main:home)'
        r = requests.get(url)
        self.assertEqual(r.status_code,200)
        print('成功get页面:首页')

    def test02_url_procuct(self):
        """get页面:产品页"""
        url=self.get_url+'/#/main/(router-main:product)'
        r = requests.get(url)
        self.assertEqual(r.status_code,200)
        print('成功get页面:产品页')

    def test03_url_software(self):
        """get页面:下载页"""
        url=self.get_url+'/#/main/(router-main:software)'
        r = requests.get(url)
        self.assertEqual(r.status_code,200)
        print('成功get页面:下载页')

    def test04_url_talent(self):
        """get页面:招贤纳士页"""
        url=self.get_url+'/#/main/(router-main:talent)'
        r = requests.get(url)
        self.assertEqual(r.status_code,200)
        print('成功get页面:招贤纳士页')

    def test05_url_login(self):
        """get页面:云平台页"""
        url=self.get_url+'/#/login'
        r = requests.get(url)
        self.assertEqual(r.status_code,200)
        print('成功get页面:云平台页')




    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()