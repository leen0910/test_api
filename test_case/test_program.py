# coding:utf-8
import requests
import json
import unittest
from common import readconfig
from common import get_token
import random



class post_request(unittest.TestCase):

    def setUp(self):
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        self.post_url = '%s%s/programs'%(API,Prefix)  #create program接口
        self.t=get_token.GetToken()
        token=self.t.test_token()
        self.header= {
        'content-type': "application/json",
        'authorization':token,
        'x-platform':"web",
        'x-module-id': "fecab02aa09d7fdecdee8c1941035ef2"
        }
    #
    def test01_createprogram(self):
        """成功上传程序文件"""
        account=self.rt.get_account()
        url=self.post_url
        header = self.header
        n=random.randint(0,255*255*255)
        data={
          "name": "程序%s"%n,
          "author": "%s"%account,
          "size": 100,
          "data": "{\"type\":\"set\",\"fname\":\"1\",\"fdata\":{\"robot\":{\"label\":\"路点1\",\"name\":\"pos\",\"id\":\"fbd9e511-4174-46bd-8ae5-04ae4d2ce46a\",\"data\":{\"x\":400,\"y\":0,\"z\":0,\"rx\":0,\"coordinate\":\"world\"},\"breakpoint\":false,\"comment\":\"\",\"children\":[],\"isValid\":false},\"ref\":[]}}",
          "version":"1.7.1",
          "types":"四轴-1",
          "machine":"QRST4-05401500"
        }
        #正确的程序数据
        #将data序列化为json格式数据，传递给data参数
        r = requests.post(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,201)
    #
    #
    def test02_getprogram(self):
        """得到程序文件列表"""
        url=self.post_url
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        # print(r.text)
        print("获取程序文件列表")
        if r.json()['total']!=0:
            t=r.json()['data'][0]['id']
            return t
        else:
            t=''

    def modify_program(self):
        """修改第一个程序的主方法"""
        t=self.test02_getprogram()
        # t=r.json()['data'][0]['id']
        if t:
            self.url=self.post_url+'/%s'%t  #传入程序id
            return self.url
        else:
            print('程序列表为空')



    def test03_modifyprogram_name(self):
        """修改程序name字段"""
        print("新增一个程序文件")
        self.test01_createprogram()  #重新上传一个程序
        url=self.modify_program()
        header = self.header
        n=random.randint(0,255*255)
        data = {"name": "修改程序%s"%n}  #随机生成修改后的程序名
        r = requests.patch(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test04_modifyprogram_author(self):
        """修改程序author字段"""
        url=self.modify_program()
        header = self.header
        n=random.randint(0,255)
        data = {"author": "修改作者%s"%n}  #随机生成修改后的名
        r = requests.patch(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test05_modifyprogram_version(self):
        """修改程序version字段"""
        url=self.modify_program()
        header = self.header
        n=random.randint(0,99)
        data = {"version": "V_modify_%s"%n}  #随机生成修改后的名
        r = requests.patch(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test06_modifyprogram_types(self):
        """修改程序types字段"""
        url=self.modify_program()
        header = self.header
        n=random.randint(0,99)
        data = {"types": "类型修改-%s"%n}  #随机生成修改后的名
        r = requests.patch(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    # def test07_modifyprogram_model(self):
    #     """修改程序model字段"""
    #     url=self.modify_program()
    #     header = self.header
    #     n=random.randint(0,99)
    #     data = {"model": "QR-400修改-%s"%n}  #随机生成修改后的名
    #     r = requests.patch(url, data=json.dumps(data), headers=header)
    #     print(r.text)
    #     self.assertEqual(r.status_code,200)

    def test08_modifyprogram_machine(self):
        """修改程序machine字段"""
        url=self.modify_program()
        header = self.header
        n=random.randint(0,99)
        data = {"machine": "QS修改-%s"%n}  #随机生成修改后的名
        r = requests.patch(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)


    def test09_modifyprogram_data(self):
        """修改程序data字段"""
        url=self.modify_program()
        header = self.header
        data = {"data": "{\"type\":\"set\",\"fname\":\"1\",\"fdata\":{\"robot\":{\"label\":\"路点2\",\"name\":\"pos\",\"id\":\"fbd9e511-4174-46bd-8ae5-04ae4d2ce46a\",\"data\":{\"x\":400,\"y\":0,\"z\":0,\"rx\":0,\"coordinate\":\"world\"},\"breakpoint\":false,\"comment\":\"\",\"children\":[],\"isValid\":false},\"ref\":[]}}"}  #修改后的
        r = requests.patch(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test10_view_oneprogram(self):
        """查看某个程序的详细内容"""
        url=self.modify_program()
        header=self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        print(r.text)

    def test11_deleteprogram(self):
        """删除第一个程序"""
        self.test01_createprogram()  #先上传一个程序
        t=self.test02_getprogram()
        if t:
            print("删除程序列中第一个程序")
            url=self.post_url+'/%s'%t  #传入删除程序id
            header = self.header
            r=requests.delete(url,headers=header)
            print(r.text)
            self.assertEqual(r.status_code,204)
        else:
            print('程序列表为空')

    def test12_get_recycleprogram(self):
        """得到程序文件回收站列表"""
        url=self.post_url+'/recycle-bins'
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        t=r.json()['total']
        if t==0:
            print("回收站为空")
        else:
            print(r.text)


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
    # a=post_request()


