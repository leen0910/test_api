# coding:utf-8
import requests
import json
import unittest
from common import readconfig
from common import get_token
from common import random_char
from common import get_list_id

class post_request(unittest.TestCase):
    def setUp(self):
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        self.post_url = '%s%s/versions'%(API,Prefix)  #versions接口
        self.t=get_token.GetToken()
        token=self.t.test_token()
        self.header= {
            'content-type': "application/json",
            'authorization':token,
            'x-platform':"web",
            'x-module-id': "d9283d5be0d01a409fbfd801aa0ff62c"
        }

    def test01_versions_create(self):
        """添加最新版本记录"""
        url=self.post_url
        header = self.header
        self.random=random_char.RandomChar()
        ver=self.random.random_char([],4,2)   # 生成4位长度混合字符串
        version="version.%s"%ver
        md5=self.random.hash(version)
        n=self.random.random_char([],4,0)   # 生成3位长度数字
        t=self.random.localtime()    # 格式化生成当前时间戳
        data={
              "version": "%s"%version,
              "platform": "windows",
              "size": int(n),
              "level": 0,
              "md5": "%s"%md5,
              "url": "http://test.robot-qixing.com:1014",
              "description": "普通升级_%s"%ver,
              "release_at": "%s"%t
        }
        r = requests.post(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,201)
        if r.json()['total']==1:
            print('成功发布版本记录id：%s'%r.json()['data']['id'])
        else:
            print('添加错误数据')

    def test02_versions_add10(self):
        """为测试需求，调用上一接口添加10条记录"""
        print('添加10条新的版本记录：')
        for i in range(10):
            self.test01_versions_create()

    def test03_version_getlist(self):
        """获取当前的版本列表"""
        url=self.post_url
        header = self.header
        r = requests.get(url,headers=header)
        self.assertEqual(r.status_code,200)
        print('获取版本列表：%s'%r.text)

    def test04_sortlist_version(self):
        """终端版本列表version：版本号 升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"version"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('终端版本列表“版本号”升序排序：%s'%r.text)

    def test05_sortlist_version(self):
        """终端版本列表version：版本号 降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-version"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('终端版本列表“版本号”降序排序：%s'%r.text)

    def test06_sortlist_release_at(self):
        """终端版本列表release_at：发布日期 升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"release_at"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('终端版本列表“发布日期”升序排序：%s'%r.text)

    def test07_sortlist_release_at(self):
        """终端版本列表release_at：发布日期 降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-release_at"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('终端版本列表“发布日期”降序排序：%s'%r.text)

    def test08_sortlist_size(self):
        """终端版本列表size：软件大小 升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"size"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('终端版本列表“软件大小”升序排序：%s'%r.text)

    def test09_sortlist_size(self):
        """终端版本列表size：软件大小 降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-size"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('终端版本列表“软件大小”降序排序：%s'%r.text)

    def test10_version_getone(self):
        """查看某一个Id的版本记录"""
        print('先获得某一个版本记录的id.')
        url1=self.post_url
        header = self.header
        rt=get_list_id.GetListID()
        id=rt.test_getoneid(url1,header)
        url=self.post_url+'/%s'%id
        r = requests.get(url,headers=header)
        self.assertEqual(r.status_code,200)
        print('查看id: %s 的版本记录：\n%s'%(id,r.text))

    def test11_update_one(self):
        """查看某一个Id的版本记录"""
        print('先获得某一个版本记录的id.')
        url1=self.post_url
        header = self.header
        rt=get_list_id.GetListID()
        id=rt.test_getoneid(url1,header)
        url=self.post_url+'/%s'%id
        data={
              "version": "修改版本",
              "platform": "windows",
              "size": 256,
              "level": 1,
              "md5": "modify123456",
              "url": "https://baidu.com",
              "description": "修改测试",
              "release_at":"2018-08-08 10:40:13"
        }
        r = requests.patch(url, data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,202)
        print('修改id: %s 的版本记录：\n%s'%(id,r.text))

    def test12_versions_clearall(self):
        """清空终端版本列表"""
        print('先get list,并返回所有用户反馈的id')
        url1=self.post_url
        header = self.header
        rt=get_list_id.GetListID()
        t_list=rt.test_getallid(url1,header)
        """传入id参数，调用下一个接口"""
        print('清除所有终端版本：')
        for t in t_list:
            url=self.post_url+'/%s'%t
            header = self.header
            r = requests.delete(url, headers=header)
            self.assertEqual(r.status_code,204)
            print(t)
        print('建立一条新的终端版本记录，备下次测试数据资源。')
        self.test01_versions_create()


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
    # t=post_request()
    # t.setUp()
    # t.test01_versions_create()