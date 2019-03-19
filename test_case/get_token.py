# coding:utf-8
import requests
import json
import unittest
import readconfig

rt=readconfig.ReadConfig()
API=rt.get_api()
Prefix=rt.get_prefix()
account=rt.get_account()
password=rt.get_pw()

class GetToken(unittest.TestCase):

    def test_token(self):
        """读取配置文件中的帐号后登录"""
        url='%s%s/users/login'%(API,Prefix)
        header = {
    'content-type': "application/json",
    'x-platform': "web",
    }
        data = {"account":"%s"%account,"password":"%s"%password} #正确的登录帐号
        #将data序列化为json格式数据，传递给data参数
        r = requests.post(url, data=json.dumps(data), headers=header)
        token=r.headers["authorization"]
        print(token)
        return token


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()

