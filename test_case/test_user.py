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

    def test09_get_myinfo(self):
        """获取当前帐号详细信息"""
        self.t=get_token.GetToken()
        id=self.t.test_userid()
        url=self.post_url+'/%s'%id
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        print('当前用户id：%s的详细信息为:\n %s'%(id,r.text))

    def test10_modify_info(self):
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


    def test11_modify_info(self):
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

    def test12_delete_myself(self):
        """删除自已的帐号：不允许"""
        self.t=get_token.GetToken()
        id=self.t.test_userid()
        url=self.post_url+'/%s'%id
        header = self.header
        r = requests.delete(url, headers=header)
        self.assertEqual(r.json()['code'],4008)
        print('返回error信息为: %s'%r.json()['error'])

    def test13_get_userlist(self):
        """分页显示用户列表：显示第一页，每页显示五条记录,并且排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"  "}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test14_search_user(self):
        """搜索用户列表并返回搜索结果"""
        url=self.post_url
        payload = {'search': 'root test'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print('搜索内容为：root test的用户列表：\n%s'%r.text)
        self.assertEqual(r.status_code,200)

    def test15_modify_pwd(self):
        """修改个人帐号密码: 新密码与老密码相同，返回错误。"""
        self.t=get_token.GetToken()
        id=self.t.test_userid()
        url=self.post_url+'/pwd/set/%s'%id
        header = self.header
        data= {
            "old_password": "666666",
            "new_password": "666666"
        }
        r = requests.post(url, data=json.dumps(data),headers=header)
        self.assertEqual(r.json()['code'],4108)
        print('新旧密码一样，返回error信息为: %s'%r.json()['error'])

    def test16_modify_pwd(self):
        """修改个人帐号密码: 老密码输入错误，返回错误。"""
        self.t=get_token.GetToken()
        id=self.t.test_userid()
        url=self.post_url+'/pwd/set/%s'%id
        header = self.header
        data= {
            "old_password": "123456",
            "new_password": "66666"
        }
        r = requests.post(url, data=json.dumps(data),headers=header)
        self.assertEqual(r.json()['code'],4107)
        print('旧密码输入错误，返回error信息为: %s'%r.json()['error'])

    def test17_reset_pwd(self):
        """设置用户初始密码: 不允许reset当前帐号为初始密码，返回错误。"""
        self.t=get_token.GetToken()
        id=self.t.test_userid()
        url=self.post_url+'/pwd/force-reset/%s'%id
        header = self.header
        r = requests.post(url,headers=header)
        self.assertEqual(r.json()['code'],4010)
        print('重置当前帐号密码为初始密码，返回error信息为: %s'%r.json()['error'])

    def get_1stuserid(self):
        """获取用户列表中第一个用户id"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        return r.json()['data'][0]['id']

    def test18_reset_pwd(self):
        """重置用户初始密码。"""
        self.t=get_token.GetToken()
        id1=self.t.test_userid()
        id2=self.get_1stuserid()
        if id1!=id2:
            url=self.post_url+'/pwd/force-reset/%s'%id2
            header = self.header
            r = requests.post(url,headers=header)
            self.assertEqual(r.status_code,200)
            print('重置用户id：%s密码为初始密码123456.'%id2)
        else:
            print('不允许重置当前帐号密码！')

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()