# coding:utf-8
import requests
import json
from common import readconfig

rt=readconfig.ReadConfig()
API=rt.get_api()
Prefix=rt.get_prefix()
account=rt.get_account()
password=rt.get_pw()

class GetToken:

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
        return token

    def test_userid(self):
        """读取配置文件中的帐号后登录"""
        url='%s%s/users/login'%(API,Prefix)
        header = {
    'content-type': "application/json",
    'x-platform': "web",
    }
        data = {"account":"%s"%account,"password":"%s"%password} #正确的登录帐号
        #将data序列化为json格式数据，传递给data参数
        r = requests.post(url, data=json.dumps(data), headers=header)
        loginuser_id=r.json()['data'][0]['id']
        return loginuser_id


    def tearDown(self):
        pass

if __name__ == "__main__":
    test=GetToken()
    print(test.test_token())
    print(test.test_userid())

