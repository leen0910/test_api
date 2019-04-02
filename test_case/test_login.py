# coding:utf-8
import requests
import json
import unittest
from common import readconfig


class post_request(unittest.TestCase):
    def setUp(self):
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        self.post_url = '%s%s/users/login'%(API,Prefix)  #登录接口
        self.header = {
    'content-type': "application/json",
    'x-platform': "web",
    } #根据实际内容

    def test01_login(self):
        """正确用户名密码登录"""
        url=self.post_url
        header = self.header
        data = {"account":"root","password":"root09"} #正确的登录帐号
        #将data序列化为json格式数据，传递给data参数
        r = requests.post(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)
        # token=r.headers["authorization"]
        # print(token)
    def test02_login(self):
        """异常数据：不存在的帐户"""
        url=self.post_url
        header = self.header
        data = {"account":"root1","password":"root09"} #不存在的登录帐号名
        r = requests.post(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.json()["code"],4101)

    def test03_login(self):
        """异常数据：密码错误"""
        url=self.post_url
        header = self.header
        data = {"account":"root","password":"root"} #帐号名正确，密码错误
        r = requests.post(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.json()["code"],4107)

    def test04_login(self):
        """异常数据：空帐户名密码"""
        url=self.post_url
        header = self.header
        data = {"account":"","password":""} #帐号名，密码为空
        r = requests.post(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.json()["code"],4107)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()