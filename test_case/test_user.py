# coding:utf-8
import requests
import json
import unittest
from common import readconfig
from common import get_token
from common import random_char



class post_request(unittest.TestCase):
    addusers=[]
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
        if r.json()['total']==1:
            self.addusers.append(r.json()['data'][0]['id'])

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
        if r.json()['total']==1:
            self.addusers.append(r.json()['data'][0]['id'])

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
        if r.json()['total']==1:
            self.addusers.append(r.json()['data'][0]['id'])


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
        if r.json()['total']==1:
            self.addusers.append(r.json()['data'][0]['id'])


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
        if r.json()['total']==1:
            self.addusers.append(r.json()['data'][0]['id'])


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
        if r.json()['total']==1:
            self.addusers.append(r.json()['data'][0]['id'])

    def test07_delete_addusers(self):
        """删除以上用例中添加的测试帐号"""
        for adduser in self.addusers:
            url=self.post_url+'/%s'%adduser
            header = self.header
            r = requests.delete(url, headers=header)
            self.assertEqual(r.status_code,204)
            print('成功删除添加测试帐号: %s'%adduser)

    def test08_logout(self):
        """登录帐号退出"""
        url=self.post_url+'/logout'
        header = self.header
        r = requests.post(url, headers=header)
        self.assertEqual(r.status_code,200)
        rt=readconfig.ReadConfig()
        account=rt.get_account()
        if r.json()['data'][0]['account']=='%s'%account:
            print('%s 帐号成功退出'%account)

    def test09_modify_info(self):
        """修改登录帐户个人信息：邮箱地址"""
        self.t=get_token.GetToken()
        self.random=random_char.RandomChar()
        id=self.t.test_userid()
        url=self.post_url+'/%s'%id
        header = self.header
        n1=self.random.random_char([],11,0)  # 生成11位长度的纯数字字符串
        data={
             "email":"%s@qq.com"%n1
        }
        r = requests.patch(url,data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,202)
        email1=r.json()['data'][0]['email']
        email2="%s@qq.com"%n1
        if email1==email2:
            print('email字段修改成功为：%s'%email1)
        else:
            print('email字段修改失败。')


    def test10_modify_info(self):
        """修改登录帐户个人信息：帐户余额"""
        self.t=get_token.GetToken()
        id=self.t.test_userid()
        url=self.post_url+'/%s'%id
        header = self.header
        self.random=random_char.RandomChar()
        n1=int(self.random.random_char([],4,0))  # 生成4位长度的纯数字字符串
        data={
             "wallet": {
                "balance":n1
            }
}
        r = requests.patch(url,data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,202)
        n=r.json()['data'][0]['wallet']['balance']
        if n==n1:
            print('当前帐户余额更新为：%s'%n)
        else:
            print('帐户余额修改失败')

if __name__ == "__main__":
    unittest.main()