import requests
import json
import unittest
from common import readconfig
from common import get_token
from common import random_char
from common import get_list_id
from common import search_list

class post_request(unittest.TestCase):

    def setUp(self):
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        self.post_url = '%s%s/downloads'%(API,Prefix)  #Request Download Terminal Software接口
        self.t=get_token.GetToken()
        token=self.t.test_token()
        self.header= {
        'content-type': "application/json",
        'authorization':token,
        'x-platform':"web",
        'x-module-id': "c64d9830c7688cb1366a954b97ff87e7"
        }

    def test01_post_request(self):
        """上传下载请求"""
        url=self.post_url
        header = self.header
        self.random=random_char.RandomChar()
        name=self.random.random_char([],4,2)   # 生成4位长度混合字符串
        email=self.random.random_char([],8,0)  # 生成6位长度的纯数字字符串
        data={
            "name": "Test-%s"%name,
            "email": "%s@qq.com"%email,
            "phone": "138%s"%email
        }
        #将data序列化为json格式数据，传递给data参数
        r = requests.post(url, data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,201)
        print('成功上传一个下载请求：\n%s'%r.text)

    def test02_get_list(self):
        """获取下载请求列表"""
        url=self.post_url
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        print('获取下载请求列表：\n%s'%r.text)

    def test03_get_one(self):
        """获取某个id下载请求"""
        print('先get list,并返回第一个下载请求的id')
        url1=self.post_url
        header = self.header
        rt=get_list_id.GetListID()
        t=rt.test_getoneid(url1,header)
        """传入id参数，调用下一个接口"""
        url=self.post_url+'/%s'%t
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        print('获取指定id：%s的下载请求：\n%s'%(t,r.text))

    def test04_create_new(self):
        """测试排序需求，新上传10个下载请求"""
        for i in range(0,10):
            self.test01_post_request()


    def test05_sort_name(self):
        """下载申请列表name：姓名 列升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"name"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('下载申请列表按“姓名”升序排序：\n%s'%r.text)

    def test06_sort_name(self):
        """下载申请列表name：姓名 列降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-name"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('下载申请列表按“姓名”降序排序：\n%s'%r.text)

    def test06_sort_create_at(self):
        """下载申请列表create_at：日期 列升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"create_at"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('下载申请列表按“日期”升序排序：\n%s'%r.text)

    def test07_sort_create_at(self):
        """下载申请列表create_at：日期 列降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-create_at"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('下载申请列表按“日期”降序排序：\n%s'%r.text)


    def test08_sort_status(self):
        """下载申请列表status：状态 列升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"status"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('下载申请列表按“状态”升序排序：\n%s'%r.text)

    def test09_sort_status(self):
        """下载申请列表status：状态 列降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-status"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('下载申请列表按“状态”降序排序：\n%s'%r.text)

    def test091_search_list(self):
        """下载申请列表搜索功能测试"""
        print("下载申请列表搜索key：")
        url=self.post_url
        header = self.header
        key="test"
        r=search_list.SearchList()
        r.search(url,header,key)


    def test10_post_settings(self):
        """配置下载申请列表订阅邮件列表"""
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        url = '%s%s/settings'%(API,Prefix)  #settings接口
        self.t=get_token.GetToken()
        token=self.t.test_token()
        header= {
        'content-type': "application/json",
        'authorization':token,
        'x-platform':"web",
        'x-module-id': "c64d9830c7688cb1366a954b97ff87e7"
        }
        data={
            "content": [
            "16955414@qq.com",
            "leen0910@sina.com"
            ]
        }
        r = requests.post(url,data=json.dumps(data),headers=header)
        self.assertEqual(r.status_code,201)
        print('上传2个邮箱订阅成功：\n%s'%r.text)

    def test11_get_settings(self):
        """获取下载申请列表订阅邮件列表"""
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        url = '%s%s/settings'%(API,Prefix)  #settings接口
        self.t=get_token.GetToken()
        token=self.t.test_token()
        header= {
        'content-type': "application/json",
        'authorization':token,
        'x-platform':"web",
        'x-module-id': "c64d9830c7688cb1366a954b97ff87e7"
        }
        r = requests.get(url,headers=header)
        self.assertEqual(r.status_code,200)
        print('下载申请的邮箱订阅列表：\n%s'%r.json()['data'][0]['content'])

    def test12_download_process(self):
        """处理软件下载请求(发送邮件)"""
        print('先get list,并返回第一个下载请求的id')
        url1=self.post_url
        header = self.header
        rt=get_list_id.GetListID()
        t=rt.test_getoneid(url1,header)
        """传入id参数，调用下一个接口"""
        url=self.post_url+'/process'+'/%s'%t
        header = self.header
        data={
            "name": "test",
            "email": "leen0910@sina.com",
            "url": "http://182.254.245.83:99/download/windows/terminal-1.1.2.exe",
            "sha256": "df912c0250f2caf1c801396315e944428878401dbed229fa5c8b0449ba0f5b55",
            "subscribers": [
                "leen0910@sina.com",
                "16955414@qq.com"
            ]
        }
        r = requests.post(url, data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,200)
        print('已处理下载申请：\n%s'%r.text)

    def test13_clear_settings(self):
        """清空下载申请列表订阅邮件列表"""
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        url = '%s%s/settings'%(API,Prefix)  #settings接口
        self.t=get_token.GetToken()
        token=self.t.test_token()
        header= {
        'content-type': "application/json",
        'authorization':token,
        'x-platform':"web",
        'x-module-id': "c64d9830c7688cb1366a954b97ff87e7"
        }
        data={
            "content": [

            ]
        }
        r = requests.post(url,data=json.dumps(data),headers=header)
        self.assertEqual(r.status_code,201)
        if r.json()['data'][0]['content']==[]:
            print('已清空下载申请的邮箱订阅。')
        else:
            print('下载申请的邮箱订阅未清空：%s'%r.json()['data'][0]['content'])


    def test14_download_clearall(self):
        """清空下载请求列表"""
        print('先get list,并返回所有下载请求的id')
        url1=self.post_url
        header = self.header
        rt=get_list_id.GetListID()
        t_list=rt.test_getallid(url1,header)
        """传入id参数，调用下一个接口"""
        print('清除所有下载申请：')
        for t in t_list:
            url=self.post_url+'/%s'%t
            header = self.header
            r = requests.delete(url, headers=header)
            self.assertEqual(r.status_code,204)
            print(t)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
    # t=post_request()
    # t.setUp()
    # t.test14_download_clearall()