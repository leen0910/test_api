# coding:utf-8
import requests
import json
import unittest
from common import readconfig
from common import get_token
from common import search_list
import random



class post_request(unittest.TestCase):

    def setUp(self):
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        self.post_url = '%s%s/subprograms'%(API,Prefix)  #create subprogram接口
        self.t=get_token.GetToken()
        token=self.t.test_token()
        self.header= {
        'content-type': "application/json",
        'authorization':token,
        'x-platform':"web",
        'x-module-id': "2468aeb5eb109b45b3e29abcbf01867d"
        }
    #
    def test01_create_subprogram(self):
        """成功上传子程序文件"""
        account=self.rt.get_account()
        url=self.post_url
        header = self.header
        n=random.randint(0,255*255*255)
        data={
          "name": "子程序测试%s"%n,
          "author": "%s"%account,
          "size": 100,
          "data": "{\"type\":\"set\",\"fname\":\"1\",\"fdata\":{\"robot\":{\"label\":\"路点1\",\"name\":\"pos\",\"id\":\"fbd9e511-4174-46bd-8ae5-04ae4d2ce46a\",\"data\":{\"x\":400,\"y\":0,\"z\":0,\"rx\":0,\"coordinate\":\"world\"},\"breakpoint\":false,\"comment\":\"\",\"children\":[],\"isValid\":false},\"ref\":[]}}",
          "version":"1.7.1",
          "types":"四轴-1",
          "machine":"QRST4-05401500"
        }
        #正确的子程序数据
        #将data序列化为json格式数据，传递给data参数
        r = requests.post(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,201)
    #
    #
    def test02_get_subprogram(self):
        """得到子程序文件列表"""
        url=self.post_url
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        # print(r.text)
        if r.json()['total']!=0:
            print("获取子程序文件列表")
            t=r.json()['data'][0]['id']
        else:
            t=''
            print('子程序列表为空')
        return t

    def getsub_name(self):
        """得到第一个程序包中name字段"""
        url=self.post_url
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        print("获取程序文件列表")
        if r.json()['total']!=0:
            t=r.json()['data'][0]['name']
        else:
            t=''
        return t

    def test20_get_subprogram(self):
        """分页显示子程序文件列表：显示第一页，每页显示五条记录,并且排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"  "}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test21_search_subprogram(self):
        """调用common方法：搜索子程序文件列表"""
        print("子程序文件列表搜索key：")
        url=self.post_url
        header = self.header
        key="测试"
        r=search_list.SearchList()
        r.search(url,header,key)

    def modify_subprogram(self):
        """修改第一个子程序的主方法"""
        t=self.test02_get_subprogram()
        # t=r.json()['data'][0]['id']
        if t:
            self.url=self.post_url+'/%s'%t  #传入程序id
        else:
            print('子程序列表为空')
        return self.url


    def test03_modifysub_name(self):
        """修改子程序name字段"""
        print("新增一个子程序文件")
        self.test01_create_subprogram()  #先上传一个程序
        url=self.modify_subprogram()
        header = self.header
        n=random.randint(0,255*255)
        data = {"name": "修改子程序%s"%n}  #随机生成修改后的程序名
        r = requests.patch(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test04_modifysub_author(self):
        """修改子程序author字段"""
        url=self.modify_subprogram()
        header = self.header
        n=random.randint(0,255)
        data = {"author": "修改作者%s"%n}  #随机生成修改后的名
        r = requests.patch(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test05_modifysub_version(self):
        """修改子程序version字段"""
        url=self.modify_subprogram()
        header = self.header
        n=random.randint(0,99)
        data = {"version": "V_modify_%s"%n}  #随机生成修改后的名
        r = requests.patch(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test06_modifysub_types(self):
        """修改子程序types字段"""
        url=self.modify_subprogram()
        header = self.header
        n=random.randint(0,99)
        data = {"types": "类型修改-%s"%n}  #随机生成修改后的名
        r = requests.patch(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    # def test07_modifysub_model(self):
    #     """修改子程序model字段"""
    #     url=self.modify_subprogram()
    #     header = self.header
    #     n=random.randint(0,99)
    #     data = {"model": "QR-400修改-%s"%n}  #随机生成修改后的名
    #     r = requests.patch(url, data=json.dumps(data), headers=header)
    #     print(r.text)
    #     self.assertEqual(r.status_code,200)

    def test08_modifysub_machine(self):
        """修改子程序machine字段"""
        url=self.modify_subprogram()
        header = self.header
        n=random.randint(0,99)
        data = {"machine": "QS修改-%s"%n}  #随机生成修改后的名
        r = requests.patch(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)


    def test09_modifysub_data(self):
        """修改子程序data字段"""
        url=self.modify_subprogram()
        header = self.header
        data = {"data": "{\"type\":\"set\",\"fname\":\"1\",\"fdata\":{\"robot\":{\"label\":\"路点782\",\"name\":\"pos\",\"id\":\"fbd9e511-4174-46bd-8ae5-04ae4d2ce46a\",\"data\":{\"x\":400,\"y\":0,\"z\":0,\"rx\":0,\"coordinate\":\"world\"},\"breakpoint\":false,\"comment\":\"\",\"children\":[],\"isValid\":false},\"ref\":[]}}"}  #修改后的
        r = requests.patch(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def download_subs(self):
        """多个子程序文件下载:获取下载文件包名"""
        oneid=self.test02_get_subprogram()
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        url = '%s%s/download/subprograms'%(API,Prefix)
        header = self.header
        data=[
            '%s'%oneid
        ]
        r = requests.post(url,data=json.dumps(data),headers=header)
        self.assertEqual(r.status_code,200)
        print(r.text)
        oneidname=r.json()['data'][0]['name']
        print('返回第一个子程序文件下载包name: %s'%oneidname)
        return oneidname

    def test0901_download_subs(self):
        """多个子程序文件下载:下载文件"""
        name=self.download_subs()
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        self.t=get_token.GetToken()
        token=self.t.test_token()
        url = '%s%s/download/subprograms/%s'%(API,Prefix,name)
        payload = {'token': token, 'mid': '2468aeb5eb109b45b3e29abcbf01867d','platform':'web'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print("多个子程序文件下载接口调用成功：")
        print(r.text)

    def test0902_download_onepsub(self):
        """仅下载单个程序文件"""
        pid=self.getsub_name()
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        self.t=get_token.GetToken()
        token=self.t.test_token()
        url = '%s%s/download/subprograms/%s.robot'%(API,Prefix,pid)
        payload = {'token': token, 'mid': '2468aeb5eb109b45b3e29abcbf01867d','platform':'web'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print("单个子程序文件下载接口调用成功：")
        print(r.text)


    def test091_sort_addsub(self):
        """测试排序功能，新增子程序文件"""
        print("新添加5个子程序文件")
        for i in range(5):
            self.test01_create_subprogram()

    def test092_sort_subprogram(self):
        """子程序列表name：程序名 列升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"name"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test093_sort_subprogram(self):
        """子程序列表name：程序名 列降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-name"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test094_sort_subprogram(self):
        """子程序列表version：程序名 列升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"version"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test095_sort_subprogram(self):
        """子程序列表version：程序名 列降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"version"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test096_sort_subprogram(self):
        """子程序列表types：类型 列升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"types"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test097_sort_subprogram(self):
        """子程序列表types：类型 列降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-types"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test098_sort_subprogram(self):
        """子程序列表machine：型号 列升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"machine"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test099_sort_subprogram(self):
        """子程序列表machine：型号 列降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-machine"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test0991_sort_subprogram(self):
        """子程序列表create_at：创建日期 列升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"create_at"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test0992_sort_subprogram(self):
        """子程序列表create_at：创建日期 列降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-create_at"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test0993_sort_subprogram(self):
        """子程序列表modify_at：修改日期 列升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"modify_at"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test0994_sort_subprogram(self):
        """子程序列表modify_at：修改日期 列降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-modify_at"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)


    def test10_view_onesub(self):
        """查看某个子程序的详细内容"""
        url=self.modify_subprogram()
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        print(r.text)

    def test11_delete_subprogram(self):
        """删除第一个子程序"""
        self.test01_create_subprogram()  #先上传一个程序
        t=self.test02_get_subprogram()
        if t:
            print("删除子程序列中第一个程序")
            url=self.post_url+'/%s'%t  #传入删除程序id
            header = self.header
            r=requests.delete(url,headers=header)
            print(r.text)
            self.assertEqual(r.status_code,204)
        else:
            print('子程序列表为空')

    def test12_getsub_recyclesub(self):
        """得到子程序文件回收站列表"""
        url=self.post_url+'/recycle-bins'
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        t=r.json()['total']
        if t==0:
            print("回收站为空")
        else:
            print('成功获得子程序回收站列表')
        return r

    def test13_get_recyclesub(self):
        """分页显示子程序文件回收站列表：显示第一页，每页显示五条记录,并且排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"  "}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test14_search_recyclesub(self):
        """调用common方法：搜索子程序回收站文件列表"""
        print("子程序回收站文件列表搜索key：")
        url=self.post_url+'/recycle-bins'
        header = self.header
        key="测试"
        r=search_list.SearchList()
        r.search(url,header,key)

    def test15_getsub_allID(self):
        """得到所有程序文件列表的id"""
        url=self.post_url
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        n=r.json()['total']
        if n!=0:
            t=[]
            for index in range(0,n):
                t.append(r.json()['data'][index]['id'])
        else:
            t=''
            print('子程序列表为空')
        print("get所有子程序文件id:%s "%t)
        return t

    def test16_deletesub_allID(self):
        """删除所有子程序文件"""
        r=self.test02_get_subprogram()
        if r:
            print("删除程序列表中所有子程序：")
            t_list=self.test15_getsub_allID()
            for t in t_list:
                url=self.post_url+'/%s'%t  #传入删除程序id
                header = self.header
                r=requests.delete(url,headers=header)
                self.assertEqual(r.status_code,204)
                print('成功删除程序文件id：%s'%t)
        else:
            print('程序列表已经为空')

    def test17_recycleRecover_1stID(self):
        """回收站程序列表第一个文件还原"""
        r=self.test12_getsub_recyclesub()
        if r.json()['total']!=0:
            t=r.json()['data'][0]['id']
            print("还原回收站中第一个程序：")
            url=self.post_url+'/retrieval/%s'%t  #传入删除程序id
            header = self.header
            r=requests.post(url,headers=header)
            self.assertEqual(r.status_code,201)
            print('还原回收站文件id：%s'%t)
        else:
            print('程序列表已经为空')

    def test18_get_recycleprogram_allID(self):
        """得到回收站所有子程序文件id"""
        url=self.post_url+'/recycle-bins'
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        n=r.json()['total']
        if n!=0:
            t=[]
            for index in range(0,n):
                t.append(r.json()['data'][index]['id'])
        else:
            t=''
            print('回收站子程序列表为空')
        print("get所有回收站子程序文件id:%s "%t)
        return t

    def test181_sort_recyclesub(self):
        """回收站子程序列表name：程序名 列升序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"name"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test182_sort_recyclesub(self):
        """回收站子程序列表name：程序名 列降序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-name"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test183_sort_recyclesub(self):
        """回收站子程序列表version：程序名 列升序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"version"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test184_sort_recyclesub(self):
        """回收站子程序列表version：程序名 列降序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"version"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test185_sort_recyclesub(self):
        """回收站子程序列表types：类型 列升序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"types"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test186_sort_recyclesub(self):
        """回收站子程序列表types：类型 列降序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-types"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test187_sort_recyclesub(self):
        """回收站子程序列表machine：型号 列升序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"machine"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test188_sort_recyclesub(self):
        """回收站子程序列表machine：型号 列降序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-machine"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test189_sort_recyclesub(self):
        """回收站子程序列表create_at：创建日期 列升序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"create_at"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test1891_sort_recyclesub(self):
        """回收站子程序列表create_at：创建日期 列降序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-create_at"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test1892_sort_recyclesub(self):
        """回收站子程序列表modify_at：修改日期 列升序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"modify_at"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test1893_sort_recyclesub(self):
        """回收站子程序列表modify_at：修改日期 列降序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-modify_at"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test19_deleterecycle_allID(self):
        """删除回收站的所有子程序文件"""
        t_list=self.test18_get_recycleprogram_allID()
        if t_list:
            print("删除回收站中所有子程序：")
            for t in t_list:
                url=self.post_url+'/force-delete/%s'%t  #传入删除程序id
                header = self.header
                r=requests.post(url,headers=header)
                self.assertEqual(r.status_code,204)
                print('成功删除回收站子程序文件id：%s'%t)
        else:
            print('子程序列表已经为空')

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
    # a=post_request()
    # a.setUp()
    # a.download_onesub()



