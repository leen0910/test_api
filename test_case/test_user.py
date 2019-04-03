# coding:utf-8
import requests
import json
import unittest
from common import readconfig
from common import get_token
from common import random_char



class post_request(unittest.TestCase):

    def setUp(self):
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        self.post_url = '%s%s/users'%(API,Prefix)  #create users接口
        self.t=get_token.GetToken()
        token=self.t.test_token()
        self.header= {
        'content-type': "application/json",
        'authorization':token,
        'x-platform':"web",
        'x-module-id': "7d94de1cdba7512a76fd42d71f537bfd"
        }
    #
    def test01_add_users(self):
        """添加新用户：管理员帐号/激活"""
        url=self.post_url
        header = self.header
        self.random=random_char.RandomChar()
        n=self.random.random_char([],4,2)   # 生成4位长度混合字符串
        n1=self.random.random_char([],6,0)  # 生成6位长度的纯数字字符串
        n2=self.random.random_char([],2,0)  # 生成2位长度的纯数字字符串
        data={
            "account": "admin_%s"%n,
            "nickname": "nick_%s"%n,
            "password": "666666",
            "avatar": "",
            "role": 0,
            "activated": bool(1),
            "name": "zz",
            "sex": 1,
            "phone": "13825%s"%n1,
            "email": "1695%s@qq.com"%n1,
            "company": {
                "name": "qx",
                "job_num": "%s"%n2,
                "job": "server developer",
                "address": {
                    "province": "浙江",
                    "city": "杭州市",
                    "district": "西湖区",
                    "remark": "公司地址测试：%s"%n
                }
            },
            "address": {
                "province": "北京",
                "city": "北京市",
                "district": "朝阳区",
                "remark": "个人地址测试_%s"%n
            }
        }
        #正确的子程序数据
        #将data序列化为json格式数据，传递给data参数
        r = requests.post(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,201)

    def test02_add_users(self):
        """添加新用户：管理员帐号/不激活"""
        url=self.post_url
        header = self.header
        self.random=random_char.RandomChar()
        n=self.random.random_char([],4,2)   # 生成4位长度混合字符串
        n1=self.random.random_char([],6,0)  # 生成6位长度的纯数字字符串
        n2=self.random.random_char([],2,0)  # 生成2位长度的纯数字字符串
        data={
            "account": "admin_%s"%n,
            "nickname": "nick_%s"%n,
            "password": "666666",
            "avatar": "",
            "role": 0,
            "activated": bool(0),
            "name": "zz",
            "sex": 1,
            "phone": "13825%s"%n1,
            "email": "1695%s@qq.com"%n1,
            "company": {
                "name": "qx",
                "job_num": "%s"%n2,
                "job": "server developer",
                "address": {
                    "province": "浙江",
                    "city": "杭州市",
                    "district": "西湖区",
                    "remark": "公司地址测试：%s"%n
                }
            },
            "address": {
                "province": "北京",
                "city": "北京市",
                "district": "朝阳区",
                "remark": "个人地址测试_%s"%n
            }
        }
        #正确的子程序数据
        #将data序列化为json格式数据，传递给data参数
        r = requests.post(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,201)


    def test03_add_users(self):
        """添加新用户：普通帐号/激活"""
        url=self.post_url
        header = self.header
        self.random=random_char.RandomChar()
        n=self.random.random_char([],4,2)   # 生成4位长度混合字符串
        n1=self.random.random_char([],6,0)  # 生成6位长度的纯数字字符串
        n2=self.random.random_char([],2,0)  # 生成2位长度的纯数字字符串
        data={
            "account": "general_%s"%n,
            "nickname": "nick_%s"%n,
            "password": "666666",
            "avatar": "",
            "role": 1,
            "activated": bool(1),
            "name": "zz",
            "sex": 1,
            "phone": "13825%s"%n1,
            "email": "1695%s@qq.com"%n1,
            "company": {
                "name": "qx",
                "job_num": "%s"%n2,
                "job": "server developer",
                "address": {
                    "province": "浙江",
                    "city": "杭州市",
                    "district": "西湖区",
                    "remark": "公司地址测试：%s"%n
                }
            },
            "address": {
                "province": "北京",
                "city": "北京市",
                "district": "朝阳区",
                "remark": "个人地址测试_%s"%n
            }
        }
        #正确的子程序数据
        #将data序列化为json格式数据，传递给data参数
        r = requests.post(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,201)

    def test04_add_users(self):
        """添加新用户：普通帐号/非激活"""
        url=self.post_url
        header = self.header
        self.random=random_char.RandomChar()
        n=self.random.random_char([],4,2)   # 生成4位长度混合字符串
        n1=self.random.random_char([],6,0)  # 生成6位长度的纯数字字符串
        n2=self.random.random_char([],2,0)  # 生成2位长度的纯数字字符串
        data={
            "account": "general_%s"%n,
            "nickname": "nick_%s"%n,
            "password": "666666",
            "avatar": "",
            "role": 1,
            "activated": bool(0),
            "name": "zz",
            "sex": 1,
            "phone": "13825%s"%n1,
            "email": "1695%s@qq.com"%n1,
            "company": {
                "name": "qx",
                "job_num": "%s"%n2,
                "job": "server developer",
                "address": {
                    "province": "浙江",
                    "city": "杭州市",
                    "district": "西湖区",
                    "remark": "公司地址测试：%s"%n
                }
            },
            "address": {
                "province": "北京",
                "city": "北京市",
                "district": "朝阳区",
                "remark": "个人地址测试_%s"%n
            }
        }
        #正确的子程序数据
        #将data序列化为json格式数据，传递给data参数
        r = requests.post(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,201)

    def test05_add_users(self):
        """添加新用户：用户帐号/激活"""
        url=self.post_url
        header = self.header
        self.random=random_char.RandomChar()
        n=self.random.random_char([],4,2)   # 生成4位长度混合字符串
        n1=self.random.random_char([],6,0)  # 生成6位长度的纯数字字符串
        n2=self.random.random_char([],2,0)  # 生成2位长度的纯数字字符串
        data={
            "account": "user_%s"%n,
            "nickname": "nick_%s"%n,
            "password": "666666",
            "avatar": "",
            "role": 2,
            "activated": bool(1),
            "name": "zz",
            "sex": 1,
            "phone": "13825%s"%n1,
            "email": "1695%s@qq.com"%n1,
            "company": {
                "name": "qx",
                "job_num": "%s"%n2,
                "job": "server developer",
                "address": {
                    "province": "浙江",
                    "city": "杭州市",
                    "district": "西湖区",
                    "remark": "公司地址测试：%s"%n
                }
            },
            "address": {
                "province": "北京",
                "city": "北京市",
                "district": "朝阳区",
                "remark": "个人地址测试_%s"%n
            }
        }
        #正确的子程序数据
        #将data序列化为json格式数据，传递给data参数
        r = requests.post(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,201)

    def test06_add_users(self):
        """添加新用户：用户帐号/非激活"""
        url=self.post_url
        header = self.header
        self.random=random_char.RandomChar()
        n=self.random.random_char([],4,2)   # 生成4位长度混合字符串
        n1=self.random.random_char([],6,0)  # 生成6位长度的纯数字字符串
        n2=self.random.random_char([],2,0)  # 生成2位长度的纯数字字符串
        data={
            "account": "user_%s"%n,
            "nickname": "nick_%s"%n,
            "password": "666666",
            "avatar": "",
            "role": 2,
            "activated": bool(0),
            "name": "zz",
            "sex": 1,
            "phone": "13825%s"%n1,
            "email": "1695%s@qq.com"%n1,
            "company": {
                "name": "qx",
                "job_num": "%s"%n2,
                "job": "server developer",
                "address": {
                    "province": "浙江",
                    "city": "杭州市",
                    "district": "西湖区",
                    "remark": "公司地址测试：%s"%n
                }
            },
            "address": {
                "province": "北京",
                "city": "北京市",
                "district": "朝阳区",
                "remark": "个人地址测试_%s"%n
            }
        }
        #正确的子程序数据
        #将data序列化为json格式数据，传递给data参数
        r = requests.post(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,201)


if __name__ == "__main__":
    unittest.main()