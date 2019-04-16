# coding:utf-8
import requests
import json
import unittest
from common import readconfig
from common import get_token

class post_request(unittest.TestCase):
    def setUp(self):
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        self.post_url = '%s%s/smtps'%(API,Prefix)  #smtps接口
        self.t=get_token.GetToken()
        token=self.t.test_token()
        self.header= {
        'content-type': "application/json",
        'authorization':token,
        'x-platform':"web",
        'x-module-id': "04d3e8abbd7e750e778f59bbf5995e40"
        }

    def test01_getlist(self):
        """获取smtps列表"""
        url=self.post_url
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        host=r.json()['data'][0]["host"]
        username=r.json()['data'][0]['username']
        password=r.json()['data'][0]['password']
        ssl=r.json()['data'][0]['ssl']
        print('邮箱配置信息：')
        print('host:%s'%host)
        print('邮箱帐户:%s'%username)
        print('邮箱密码:%s'%password)
        print('ssl:%s'%ssl)
        return r.json()['data'][0]['id']

    def test02_update(self):
        """更新smtps帐号信息"""
        id=self.test01_getlist()
        url=self.post_url+'/%s'%id
        header = self.header
        data ={
            "host": "smtp.139.com",
            "username": "15958189624@139.com",
            "password": "83276015"
        }
        r = requests.patch(url, data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,202)
        print('成功更新smtps信息：\n%s'%r.text)


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()