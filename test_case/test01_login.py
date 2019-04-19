# coding:utf-8
import requests
import json
import unittest
from common import readconfig
from common import writeconfig

class post_request(unittest.TestCase):
    """找回密码，邮箱验证流程需要手工验证。"""
    def setUp(self):
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        self.post_url = '%s%s/users/login'%(API,Prefix)  #登录接口
        self.header = {
    'content-type': "application/json",
    'x-platform': "web",
    } #根据实际内容

    def common_login(self,account,pw):
        """通用登录接口调用方法"""
        url=self.post_url
        header = self.header
        data = {"account":account,"password":pw} #正确的登录帐号
        r = requests.post(url, data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,200)
        token=r.headers["authorization"]
        if r.json()['data'][0]['reset']==bool(1):
            print('用户是初始密码登录,返回account,pw,token到config.txt文件。')
            obj=writeconfig.rwconfig()
            path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\test_api\\info.txt'
            obj.modifyconfig(path,'info','comm_user',str(account))
            obj.modifyconfig(path,'info','comm_user_pw',str(pw))
            obj.modifyconfig(path,'info','comm_user_token',str(token))
        else:
            print('用户不是初始密码登录。')
            id=r.json()['data'][0]['id']
            obj=writeconfig.rwconfig()
            obj.writeconfig('info','my_id',str(id))


    def test01_login(self):
        """正确用户名密码登录"""
        url=self.post_url
        header = self.header
        data = {"account":"root","password":"root09"} #正确的登录帐号
        #将data序列化为json格式数据，传递给data参数
        r = requests.post(url, data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,200)
        if r.json()['total']==1:
            print('帐号登录成功！')
        else:
            print("登录帐号异常")
        print(r.text)


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