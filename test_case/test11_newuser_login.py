# coding:utf-8
import requests
import json
import unittest
from common import readconfig
from common import writeconfig
from test_case import test02_user
from test_case import test01_login
import configparser

class post_request(unittest.TestCase):
    """初始密码用户重置，是一个测试流程，具体接口之间的调用逻辑"""
    def test01_create_newusre(self):
        """先添加新用户，密码为初始密码"""
        t=test02_user.post_request()
        print('先添加一个管理员/激活的新用户。')
        t.setUp()
        r=t.common_add_users()
        newuser=r.json()['data'][0]['account']
        newuserid=r.json()['data'][0]['id']
        obj=writeconfig.rwconfig()
        path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\test_api\\info.txt'
        obj.modifyconfig(path,'info','ini_user',str(newuser))
        obj.modifyconfig(path,'info','ini_user_id',str(newuserid))
        print('初始用户：%s 返回config文件'%newuser)


    def test02_nweuser_login(self):
        """用上一步建立的新用户进行登录，获取token值"""
        cf=configparser.ConfigParser()
        cf.read('C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\test_api\\info.txt')
        account=cf.get('info', 'ini_user')
        rt=test01_login.post_request()
        rt.setUp()
        rt.common_login(account,'123456')
        print('初始帐号：%s登录成功,并返回token值。'%account)

    def test03_nweuser_reset(self):
        """初始用户密码重置"""
        cf=configparser.ConfigParser()
        cf.read('C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\test_api\\info.txt')
        name=cf.get('info', 'comm_user')
        token=cf.get('info', 'comm_user_token')
        rt=readconfig.ReadConfig()
        API=rt.get_api()
        Prefix=rt.get_prefix()
        url = '%s%s/users/pwd/reset'%(API,Prefix)  #rest接口
        header= {
            'content-type': "application/json",
            'Authorization':token
        }
        data= {
            "account": '%s'%name,
            "password": "666666"
        }
        r = requests.post(url,data=json.dumps(data),headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)
        print('初始密码重置成功!')
        obj=writeconfig.rwconfig()
        path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\test_api\\info.txt'
        obj.modifyconfig(path,'info','comm_user_pw',"666666")
        print('更新config文件：ini_user_id')


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()