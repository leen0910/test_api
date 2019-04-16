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
        else:
            t=''
        return t

    def getprogram_name(self):
        """得到第一个程序包中name字段"""
        url=self.post_url
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        # print(r.text)
        print("获取程序文件列表")
        if r.json()['total']!=0:
            t=r.json()['data'][0]['name']
        else:
            t=''
        return t

    def test20_get_program(self):
        """分页显示程序列表：显示第一页，每页显示五条记录,并且排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"  "}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test21_search_program(self):
        """搜索程序列表并返回搜索结果"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','search': '12'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        if r.json()['total']!=0:
            print('搜索含有字符“12”的程序列表前五条内容：\n%s'%r.text)
        else:
            print('搜索结果为空')


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

    def download_programs(self):
        """多文件下载:获取下载文件包名"""
        oneid=self.test02_getprogram()
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        url = '%s%s/download/programs'%(API,Prefix)
        header = self.header
        data=[
            '%s'%oneid
        ]
        r = requests.post(url,data=json.dumps(data),headers=header)
        self.assertEqual(r.status_code,200)
        print(r.text)
        oneidname=r.json()['data'][0]["name"]
        print('返回第一个程序文件下载包name: %s'%oneidname)
        return oneidname

    def test0901_download_programs(self):
        """多文件下载:下载文件"""
        name=self.download_programs()
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        self.t=get_token.GetToken()
        token=self.t.test_token()
        url = '%s%s/download/programs/%s'%(API,Prefix,name)
        payload = {'token': token, 'mid': 'fecab02aa09d7fdecdee8c1941035ef2','platform':'web'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print("多个程序文件打包下载接口调用成功：")
        print(r.text)

    def test0902_download_oneprogram(self):
        """仅下载单个程序文件"""
        pid=self.getprogram_name()
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        self.t=get_token.GetToken()
        token=self.t.test_token()
        url = '%s%s/download/programs/%s.robot'%(API,Prefix,pid)
        payload = {'token': token, 'mid': 'fecab02aa09d7fdecdee8c1941035ef2','platform':'web'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print("单个程序文件下载接口调用成功：")
        print(r.text)

    def test091_sort_addprograms(self):
        """测试排序功能，新增程序文件"""
        print("新添加5个程序文件")
        for i in range(5):
            self.test01_createprogram()

    def test092_sort_program(self):
        """程序列表name：程序名 列升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"name"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test093_sort_program(self):
        """程序列表name：程序名 列降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-name"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test094_sort_program(self):
        """程序列表version：程序名 列升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"version"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test095_sort_program(self):
        """程序列表version：程序名 列降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"version"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test096_sort_program(self):
        """程序列表types：类型 列升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"types"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test097_sort_program(self):
        """程序列表types：类型 列降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-types"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test098_sort_program(self):
        """程序列表machine：型号 列升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"machine"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test099_sort_program(self):
        """程序列表machine：型号 列降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-machine"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test0991_sort_program(self):
        """程序列表create_at：创建日期 列升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"create_at"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test0992_sort_program(self):
        """程序列表create_at：创建日期 列降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-create_at"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test0993_sort_program(self):
        """程序列表modify_at：修改日期 列升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"modify_at"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test0994_sort_program(self):
        """程序列表modify_at：修改日期 列降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-modify_at"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
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
            print('成功获得程序文件回收站列表')
        return r

    def test13_get_recycleprogram(self):
        """分页显示文件回收站列表：显示第一页，每页显示五条记录,并且排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"  "}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test14_search_recycleprogram(self):
        """搜索程序回收站文件列表并返回搜索结果"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','search': '程序'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        if r.json()['total']!=0:
            print('搜索含有字符“程序”的程序列表前五条内容：\n%s'%r.text)
        else:
            print('搜索结果为空')


    def test15_getprogram_allID(self):
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
            print('程序列表为空')
        print("get所有程序文件id:%s "%t)
        return t

    def test16_deleteprogram_allID(self):
        """删除所有程序文件"""
        r=self.test02_getprogram()
        if r:
            print("删除程序列表中所有程序：")
            t_list=self.test15_getprogram_allID()
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
        r=self.test12_get_recycleprogram()
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
        """得到回收站所有程序文件id"""
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
            print('回收站程序列表为空')
        print("get所有回收站程序文件id:%s "%t)
        return t

    def test181_sort_recycleprogram(self):
        """回收站程序列表name：程序名 列升序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"name"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test182_sort_recycleprogram(self):
        """回收站程序列表name：程序名 列降序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-name"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test183_sort_recycleprogram(self):
        """回收站程序列表version：程序名 列升序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"version"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test184_sort_recycleprogram(self):
        """回收站程序列表version：程序名 列降序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"version"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test185_sort_recycleprogram(self):
        """回收站程序列表types：类型 列升序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"types"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test186_sort_recycleprogram(self):
        """回收站程序列表types：类型 列降序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-types"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test187_sort_recycleprogram(self):
        """回收站程序列表machine：型号 列升序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"machine"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test188_sort_recycleprogram(self):
        """回收站程序列表machine：型号 列降序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-machine"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test189_sort_recycleprogram(self):
        """回收站程序列表create_at：创建日期 列升序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"create_at"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test1891_sort_recycleprogram(self):
        """回收站程序列表create_at：创建日期 列降序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-create_at"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test1892_sort_recycleprogram(self):
        """回收站程序列表modify_at：修改日期 列升序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"modify_at"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test1893_sort_recycleprogram(self):
        """回收站程序列表modify_at：修改日期 列降序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-modify_at"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test19_deleterecycle_allID(self):
        """彻底删除回收站的所有程序文件"""
        t_list=self.test18_get_recycleprogram_allID()
        if t_list:
            print("删除回收站中所有程序：")
            for t in t_list:
                url=self.post_url+'/force-delete/%s'%t  #传入删除程序id
                header = self.header
                r=requests.post(url,headers=header)
                self.assertEqual(r.status_code,204)
                print('成功删除回收站程序文件id：%s'%t)
        else:
            print('程序列表已经为空')


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
    # a=post_request()
    # a.setUp()
    # a.testdownload_programs()
    # a.test0901_download_programs()
    # a.test0902_download_oneprogram()


