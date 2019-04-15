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
        self.post_url = '%s%s/tmplprograms'%(API,Prefix)  #create tmplprograms接口
        self.t=get_token.GetToken()
        token=self.t.test_token()
        self.header= {
        'content-type': "application/json",
        'authorization':token,
        'x-platform':"web",
        'x-module-id': "03767159816cac28b1e3f2a0e0014b2b"
        }
    #
    def test01_create_tmplprogram(self):
        """成功上传模板程序文件"""
        account=self.rt.get_account()
        url=self.post_url
        header = self.header
        n=random.randint(0,255*255*255)
        n1=random.randint(0,20)
        data={
          "name": "模板程序测试%s"%n,
          "author": "%s"%account,
          "size": 100,
          "data": "[{\"label\":\"涂胶模板\",\"name\":\"program\",\"id\":\"ae7c588f-bb98-42fd-99ea-f38045bb8f33\",\"data\":{\"version\":\"1.7.1\",\"machine\":\"QRST4-05401500\",\"main_io\":\"3.2M\",\"tool_io\":\"3.2T\",\"author\":\"root\",\"c_time\":\"2019-03-11 13:29:20\",\"m_time\":\"2019-03-26 10:01:12\",\"size\":1858,\"md5\":\"6de553f91ba95db22ecbb02cd16e82c9\",\"style\":\"template\",\"types\":\"\"},\"children\":[{\"label\":\"点到点\",\"name\":\"p2p\",\"data\":{\"x\":400,\"y\":0,\"z\":0,\"rz\":0}}]},{\"label\":\"全局变量\",\"name\":\"g_variable\",\"children\":[{\"label\":\"arm\",\"name\":\"variable\",\"id\":\"fbd6529e-c55e-4f04-a292-9028df0c4208\",\"comment\":\"左右臂\",\"data\":{\"value\":\"right\"}},{\"label\":\"ref_sys\",\"name\":\"variable\",\"id\":\"3efb5952-8635-4432-972a-d4009b45595b\",\"comment\":\"坐标系\",\"data\":{\"value\":\"abc228bc-1aa8-49bb-8b5a-e87567624d02\"}},{\"label\":\"wait_finish\",\"name\":\"variable\",\"id\":\"36481789-c875-4f2e-9bc7-d7730eddb835\",\"comment\":\"等待运动完成\",\"data\":{\"value\":true}},{\"label\":\"j_vel\",\"name\":\"variable\",\"id\":\"43e1d9af-4043-4a82-abf6-d4c8c3457f0a\",\"comment\":\"关节速度\",\"data\":{\"value\":0.5}},{\"label\":\"j_acc\",\"name\":\"variable\",\"id\":\"a9a96478-8766-420b-830b-95e0149c9476\",\"comment\":\"关节加速度\",\"data\":{\"value\":0.5}},{\"label\":\"j_dec\",\"name\":\"variable\",\"id\":\"662539a1-ccb6-460d-8f68-81dde512e283\",\"comment\":\"关节减速度\",\"data\":{\"value\":0.5}},{\"label\":\"l_vel\",\"name\":\"variable\",\"id\":\"24c36be7-a96d-4270-aa2e-63961cb523cb\",\"comment\":\"曲线速度\",\"data\":{\"value\":100}},{\"label\":\"l_acc\",\"name\":\"variable\",\"id\":\"126d0440-7bb3-4caf-922b-68e2a9630fa2\",\"comment\":\"曲线加速度\",\"data\":{\"value\":500}},{\"label\":\"l_dec\",\"name\":\"variable\",\"id\":\"27c204d3-ea96-4f7e-8844-0bec11400b61\",\"comment\":\"曲线减速度\",\"data\":{\"value\":500}},{\"label\":\"rel\",\"name\":\"variable\",\"id\":\"0647b6e6-2259-4f27-a038-bc6a93e8534e\",\"comment\":\"相对逼近\",\"data\":{\"value\":0.5}}]},{\"label\":\"坐标系\",\"name\":\"all_sys\",\"children\":[{\"label\":\"世界坐标系\",\"name\":\"world_sys\",\"id\":\"abc228bc-1aa8-49bb-8b5a-e87567624d02\",\"data\":{\"x\":0,\"y\":0,\"z\":0,\"rx\":0,\"ry\":0,\"rz\":0}}]}]",
          "version":"1.7.%s"%n1,
          "types":"焊接",
          "machine":"Q"
        }
        #正确的子程序数据
        #将data序列化为json格式数据，传递给data参数
        r = requests.post(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,201)
    #
    #
    def test02_get_tmplprogram(self):
        """得到模板程序文件列表"""
        url=self.post_url
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        # print(r.text)
        print("成功获取模板程序文件列表")
        if r.json()['total']!=0:
            t=r.json()['data'][0]['id']
        else:
            t=''
            print('模板程序列表为空')
        return t

    def test22_get_tmplprogram(self):
        """分页显示个人模版文件列表：显示第一页，每页显示五条记录,并且排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"  "}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test23_search_tmplprogram(self):
        """搜索个人模板文件列表并返回搜索结果"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','search': '测试'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        if r.json()['total']!=0:
            print('搜索含有字符“测试”的模板程序列表前五条内容：\n%s'%r.text)
        else:
            print('搜索结果为空')

    def modify_tmplprogram(self):
        """修改第一个模板程序的主方法"""
        t=self.test02_get_tmplprogram()
        # t=r.json()['data'][0]['id']
        if t:
            self.url=self.post_url+'/%s'%t  #传入程序id
        else:
            print('模板程序列表为空')
            self.url=''
        return self.url


    def test03_modifytmpl_name(self):
        """修改模板程序name字段"""
        print("新增一个模板程序文件")
        self.test01_create_tmplprogram()  #先上传一个程序
        url=self.modify_tmplprogram()
        header = self.header
        n=random.randint(0,255*255)
        data = {"name": "修改模板%s"%n}  #随机生成修改后的程序名
        if url:
            r = requests.patch(url, data=json.dumps(data), headers=header)
            print(r.text)
            self.assertEqual(r.status_code,200)
        else:
            print('无模板的name字段修改')

    def test04_modifytmpl_author(self):
        """修改模板程序author字段"""
        url=self.modify_tmplprogram()
        header = self.header
        n=random.randint(0,255)
        data = {"author": "修改作者%s"%n}  #随机生成修改后的名
        if url:
            r = requests.patch(url, data=json.dumps(data), headers=header)
            print(r.text)
            self.assertEqual(r.status_code,200)
        else:
            print('无模板的author字段修改')

    def test05_modifytmpl_version(self):
        """修改模板程序version字段"""
        url=self.modify_tmplprogram()
        header = self.header
        n=random.randint(0,99)
        data = {"version": "V_modify_%s"%n}  #随机生成修改后的名
        if url:
            r = requests.patch(url, data=json.dumps(data), headers=header)
            print(r.text)
            self.assertEqual(r.status_code,200)
        else:
            print('无模板的verdion字段修改')

    def test06_modifytmpl_types(self):
        """修改模板程序types字段"""
        url=self.modify_tmplprogram()
        header = self.header
        n=random.randint(0,99)
        data = {"types": "类型修改-%s"%n}  #随机生成修改后的名
        if url:
            r = requests.patch(url, data=json.dumps(data), headers=header)
            print(r.text)
            self.assertEqual(r.status_code,200)
        else:
            print('无模板的types字段修改')

    # def test07_modifytmpl_model(self):
    #     """修改子程序model字段"""
    #     url=self.modify_tmplprogram()()
    #     header = self.header
    #     n=random.randint(0,99)
    #     data = {"model": "QR-400修改-%s"%n}  #随机生成修改后的名
    #     r = requests.patch(url, data=json.dumps(data), headers=header)
    #     print(r.text)
    #     self.assertEqual(r.status_code,200)

    def test08_modifytmpl_machine(self):
        """修改模板程序machine字段"""
        url=self.modify_tmplprogram()
        header = self.header
        n=random.randint(0,99)
        data = {"machine": "QS修改-%s"%n}  #随机生成修改后的名
        if url:
            r = requests.patch(url, data=json.dumps(data), headers=header)
            print(r.text)
            self.assertEqual(r.status_code,200)
        else:
            print('无模板的machine字段修改')


    def test09_modifytmpl_data(self):
        """修改模板程序data字段"""
        url=self.modify_tmplprogram()
        header = self.header
        data = {"data": "[{\"label\":\"修改测试模板\",\"name\":\"program\",\"id\":\"ae7c588f-bb98-42fd-99ea-f38045bb8f33\",\"data\":{\"version\":\"1.7.1\",\"machine\":\"QRST4-05401500\",\"main_io\":\"3.2M\",\"tool_io\":\"3.2T\",\"author\":\"root\",\"c_time\":\"2019-03-11 13:29:20\",\"m_time\":\"2019-03-26 10:01:12\",\"size\":1858,\"md5\":\"6de553f91ba95db22ecbb02cd16e82c9\",\"style\":\"template\",\"types\":\"\"},\"children\":[{\"label\":\"点到点\",\"name\":\"p2p\",\"data\":{\"x\":400,\"y\":0,\"z\":0,\"rz\":0}}]},{\"label\":\"全局变量\",\"name\":\"g_variable\",\"children\":[{\"label\":\"arm\",\"name\":\"variable\",\"id\":\"fbd6529e-c55e-4f04-a292-9028df0c4208\",\"comment\":\"左右臂\",\"data\":{\"value\":\"right\"}},{\"label\":\"ref_sys\",\"name\":\"variable\",\"id\":\"3efb5952-8635-4432-972a-d4009b45595b\",\"comment\":\"坐标系\",\"data\":{\"value\":\"abc228bc-1aa8-49bb-8b5a-e87567624d02\"}},{\"label\":\"wait_finish\",\"name\":\"variable\",\"id\":\"36481789-c875-4f2e-9bc7-d7730eddb835\",\"comment\":\"等待运动完成\",\"data\":{\"value\":true}},{\"label\":\"j_vel\",\"name\":\"variable\",\"id\":\"43e1d9af-4043-4a82-abf6-d4c8c3457f0a\",\"comment\":\"关节速度\",\"data\":{\"value\":0.5}},{\"label\":\"j_acc\",\"name\":\"variable\",\"id\":\"a9a96478-8766-420b-830b-95e0149c9476\",\"comment\":\"关节加速度\",\"data\":{\"value\":0.5}},{\"label\":\"j_dec\",\"name\":\"variable\",\"id\":\"662539a1-ccb6-460d-8f68-81dde512e283\",\"comment\":\"关节减速度\",\"data\":{\"value\":0.5}},{\"label\":\"l_vel\",\"name\":\"variable\",\"id\":\"24c36be7-a96d-4270-aa2e-63961cb523cb\",\"comment\":\"曲线速度\",\"data\":{\"value\":100}},{\"label\":\"l_acc\",\"name\":\"variable\",\"id\":\"126d0440-7bb3-4caf-922b-68e2a9630fa2\",\"comment\":\"曲线加速度\",\"data\":{\"value\":500}},{\"label\":\"l_dec\",\"name\":\"variable\",\"id\":\"27c204d3-ea96-4f7e-8844-0bec11400b61\",\"comment\":\"曲线减速度\",\"data\":{\"value\":500}},{\"label\":\"rel\",\"name\":\"variable\",\"id\":\"0647b6e6-2259-4f27-a038-bc6a93e8534e\",\"comment\":\"相对逼近\",\"data\":{\"value\":0.5}}]},{\"label\":\"坐标系\",\"name\":\"all_sys\",\"children\":[{\"label\":\"世界坐标系\",\"name\":\"world_sys\",\"id\":\"abc228bc-1aa8-49bb-8b5a-e87567624d02\",\"data\":{\"x\":0,\"y\":0,\"z\":0,\"rx\":0,\"ry\":0,\"rz\":0}}]}]"}  #修改后的
        if url:
            r = requests.patch(url, data=json.dumps(data), headers=header)
            print(r.text)
            self.assertEqual(r.status_code,200)
        else:
            print('无模板的data字段修改')

    def test10_modifytmpl_price(self):
        """修改模板程序price字段"""
        url=self.modify_tmplprogram()
        header = self.header
        a=random.uniform(100,500)
        n=round(a,2)
        data = {"price": n}  #随机生成两位小数价格
        if url:
            r = requests.patch(url, data=json.dumps(data), headers=header)
            print(r.text)
            self.assertEqual(r.status_code,200)
        else:
            print('无模板的price字段修改')

    def test11_modifytmpl_public(self):
        """修改模板程序为公开"""
        url=self.modify_tmplprogram()
        header = self.header
        data ={"public":bool(1)}
        if url:
            r = requests.patch(url, data=json.dumps(data), headers=header)
            print('成功将模板列表第一个模板设置为公开：\n%s'%r.text)
            self.assertEqual(r.status_code,200)
        else:
            print('无模板程序设置为公开')

    def test111_sort_addtmpl(self):
        """测试排序功能，新增模板文件"""
        print("新添加5个程序文件")
        for i in range(5):
            self.test01_create_tmplprogram()   #增加模板
            self.test10_modifytmpl_price()    #修改价格

    def test112_sort_tmpl(self):
        """模板程序列表name：程序名 列升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"name"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test113_sort_tmpl(self):
        """模板程序列表name：程序名 列降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-name"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test114_sort_tmpl(self):
        """模板程序列表version：程序名 列升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"version"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test115_sort_tmpl(self):
        """模板程序列表version：程序名 列降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"version"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test116_sort_tmpl(self):
        """模板程序列表price：售价 列升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"price"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test117_sort_tmpl(self):
        """模板程序列表price：售价 列降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-price"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test12_view_onetmpl(self):
        """查看某个模板程序的详细内容"""
        url=self.modify_tmplprogram()
        header = self.header
        if url:
            r = requests.get(url, headers=header)
            self.assertEqual(r.status_code,200)
            print(r.text)
        else:
            print('模板列表为空')

    def test13_delete_tmplprogram(self):
        """删除第一个模板程序"""
        self.test01_create_tmplprogram()  #先上传一个模板
        t=self.test02_get_tmplprogram()
        if t:
            print("删除模板程序列中第一个程序")
            url=self.post_url+'/%s'%t  #传入删除程序id
            header = self.header
            r=requests.delete(url,headers=header)
            print(r.text)
            self.assertEqual(r.status_code,204)
        else:
            print('模板程序列表为空')

    def test14_get_recycletmpl(self):
        """得到模板程序回收站列表"""
        url=self.post_url+'/recycle-bins'
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        t=r.json()['total']
        if t==0:
            print("回收站为空")
        else:
            print('成功获得模板回收站列表')
        return r

    def test15_get_recycletmpl(self):
        """分页显示模板程序回收站列表：显示第一页，每页显示五条记录,并且排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"  "}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test16_search_recycletmpl(self):
        """搜索模板程序回收站文件列表并返回搜索结果"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','search': '模板'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        if r.json()['total']!=0:
            print('搜索含有字符“模板”的模板程序列表前五条内容：\n%s'%r.text)
        else:
            print('搜索结果为空')

    def test161_filter_recycletmpl(self):
        """按类型:焊接 & 机型:Q,过滤模板程序回收站列表"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','class':'焊接','model':'Q'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        if r.json()['total']!=0:
            print('按类型:焊接 & 机型:Q,过滤模板程序列表前五条内容：\n%s'%r.text)
        else:
            print('过滤内容为空')

    def test162_filter_recycletmpl(self):
        """按类型:焊接,过滤模板程序回收站列表"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','class':'焊接'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        if r.json()['total']!=0:
            print('按类型:焊接 过滤模板程序列表前五条内容：\n%s'%r.text)
        else:
            print('过滤内容为空')

    def test163_filter_recycletmpl(self):
        """按机型:Q,过滤模板程序回收站列表"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','model':'Q'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        if r.json()['total']!=0:
            print('按机型:Q,过滤模板程序列表前五条内容：\n%s'%r.text)
        else:
            print('过滤内容为空')

    def test17_gettmpl_allID(self):
        """得到所有模板程序文件列表的id"""
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
            print('模板程序列表为空')
        print("get所有模板程序文件id:%s "%t)
        return t

    def test18_deletetmpl_allID(self):
        """删除所有模板程序文件"""
        self.test01_create_tmplprogram()
        r=self.test02_get_tmplprogram()
        if r:
            print("删除列表中所有模板程序：")
            t_list=self.test17_gettmpl_allID()
            for t in t_list:
                url=self.post_url+'/%s'%t  #传入删除程序id
                header = self.header
                r=requests.delete(url,headers=header)
                self.assertEqual(r.status_code,204)
                print('成功删除模板程序文件id：%s'%t)
        else:
            print('模板程序列表已经为空')

    def test19_recycleRecover_1stID(self):
        """回收站模板程序列表第一个文件还原"""
        r=self.test14_get_recycletmpl()
        if r.json()['total']!=0:
            t=r.json()['data'][0]['id']
            print("还原回收站中第一个模板程序：")
            url=self.post_url+'/retrieval/%s'%t  #传入删除程序id
            header = self.header
            r=requests.post(url,headers=header)
            self.assertEqual(r.status_code,201)
            print('还原回收站模板文件id：%s'%t)
        else:
            print('模板程序列表已经为空')

    def test191_sort_recycletmpl(self):
        """回收站模板程序列表name：程序名 列升序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"name"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test192_sort_recycletmpl(self):
        """回收站模板程序列表name：程序名 列降序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-name"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test193_sort_recycletmpl(self):
        """回收站模板程序列表version：程序名 列升序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"version"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test194_sort_recycletmpl(self):
        """回收站模板程序列表version：程序名 列降序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"version"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test195_sort_recycletmpl(self):
        """回收站模板程序列表price：售价 列升序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"price"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test196_sort_recycletmpl(self):
        """回收站模板程序列表price：售价 列降序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-price"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test197_sort_recycletmpl(self):
        """回收站模板程序列表author：作者 列升序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"author"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test198_sort_recycletmpl(self):
        """回收站模板程序列表author：作者 列降序排序"""
        url=self.post_url+'/recycle-bins'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-author"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test20_get_recycletmpl_allID(self):
        """得到回收站所有模板程序文件id"""
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
            print('回收站模板程序列表为空')
        print("get所有回收站模板程序文件id:%s "%t)
        return t

    def test21_deleterecycle_allID(self):
        """删除回收站的所有模板程序文件"""
        t_list=self.test20_get_recycletmpl_allID()
        if t_list:
            print("删除回收站中所有模板程序：")
            for t in t_list:
                url=self.post_url+'/force-delete/%s'%t  #传入删除程序id
                header = self.header
                r=requests.post(url,headers=header)
                self.assertEqual(r.status_code,204)
                print('成功删除回收站模板程序文件id：%s'%t)
        else:
            print('模板程序列表已经为空')

    def test24_filter_tmplprogram(self):
        """按类型:焊接 & 机型:Q,过滤模板程序列表"""
        print('新建符合过滤条件的模板程序')
        for i in range(3):
            self.test01_create_tmplprogram()
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','class':'焊接','model':'Q'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        if r.json()['total']!=0:
            print('按类型:焊接 & 机型:Q,过滤模板程序列表前五条内容：\n%s'%r.text)
        else:
            print('过滤类型:焊接 & 机型:Q,内容为空')

    def test25_filter_tmplprogram(self):
        """按类型:焊接,过滤模板程序列表"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','class':'焊接'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        if r.json()['total']!=0:
            print('按类型:焊接 过滤模板程序列表前五条内容：\n%s'%r.text)
        else:
            print('过滤类型:焊接，内容为空')

    def test26_filter_tmplprogram(self):
        """按机型:Q,过滤模板程序列表"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','model':'Q'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        if r.json()['total']!=0:
            print('按机型:Q,过滤模板程序列表前五条内容：\n%s'%r.text)
        else:
            print('过滤 机型:Q,内容为空')


    def test27_get_public(self):
        """得到公开模板程序列表"""
        url=self.post_url+'/public'
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        if r.json()['total']!=0:
            print("成功获取公开模板程序文件列表。")
            t=r.json()['data'][0]['id']
        else:
            print('公开模板程序列表为空。')
            t=''
        return t

    def get_public_name(self):
        """得到公开模板程序列表第一个文件名字"""
        url=self.post_url+'/public'
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        if r.json()['total']!=0:
            t=r.json()['data'][0]['name']
        else:
            print('公开模板程序列表为空')
            t=''
        return t

    def test2701_download_tmpls(self):
        """公开模板列表中选择多个文件下载:获取下载文件包名"""
        oneid=self.test27_get_public()
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        url = '%s%s/download/tmplprograms'%(API,Prefix)
        header = self.header
        data=[
            '%s'%oneid
        ]
        r = requests.post(url,data=json.dumps(data),headers=header)
        self.assertEqual(r.status_code,200)
        print(r.text)
        oneidname=r.json()['data']['name']
        print('返回第一个公开模板程序文件下载包name: %s'%oneidname)
        price=r.json()['data']['total_price']
        print('下载模板需要的费用：%s'%price)
        return oneidname

    def test2702_download_tmpls(self):
        """公开模板列表中选择多个文件下载:下载文件"""
        name=self.test2701_download_tmpls()
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        self.t=get_token.GetToken()
        token=self.t.test_token()
        url = '%s%s/download/tmplprograms/%s'%(API,Prefix,name)
        payload = {'token': token, 'mid': '03767159816cac28b1e3f2a0e0014b2b','platform':'web'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print("多个模板程序文件打包下载接口调用成功：")
        print(r.text)

    def test2703_download_onetmpl(self):
        """仅下载单个模板程序文件"""
        pid=self.get_public_name()
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        self.t=get_token.GetToken()
        token=self.t.test_token()
        url = '%s%s/download/tmplprograms/%s.robot'%(API,Prefix,pid)
        payload = {'token': token, 'mid': '03767159816cac28b1e3f2a0e0014b2b','platform':'web'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print("单个模板程序文件下载接口调用成功：")
        print(r.text)


    def test271_sort_publictmpl(self):
        """回收站模板程序列表name：程序名 列升序排序"""
        url=self.post_url+'/public'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"name"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test272_sort_publictmpl(self):
        """公开模板程序列表name：程序名 列降序排序"""
        url=self.post_url+'/public'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-name"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test273_sort_publictmpl(self):
        """公开模板程序列表version：程序名 列升序排序"""
        url=self.post_url+'/public'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"version"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test274_sort_publictmpl(self):
        """公开模板程序列表version：程序名 列降序排序"""
        url=self.post_url+'/public'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"version"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test275_sort_publictmpl(self):
        """公开模板程序列表price：售价 列升序排序"""
        url=self.post_url+'/public'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"price"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test276_sort_publictmpl(self):
        """公开模板程序列表price：售价 列降序排序"""
        url=self.post_url+'/public'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-price"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test277_sort_publictmpl(self):
        """公开模板程序列表author：作者 列升序排序"""
        url=self.post_url+'/public'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"author"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test278_sort_publictmpl(self):
        """公开模板程序列表author：作者 列降序排序"""
        url=self.post_url+'/public'
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-author"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        print(r.text)
        self.assertEqual(r.status_code,200)

    def test28_get_public(self):
        """得到公开模板程序列表第一页内容"""
        url=self.post_url+'/public'
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5'}
        r = requests.get(url,params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        if r.json()['total']!=0:
            print("获取公开模板程序文件列表第一页：")
            print(r.text)
        else:
            print('公开模板程序列表为空')

    def test29_search_public(self):
        """搜索公开模板程序列表"""
        url=self.post_url+'/public'
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','search':'模板'}
        r = requests.get(url,params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        if r.json()['total']!=0:
            print("搜索公开模板含 有“模板”的文件，返回第一页内容")
            print(r.text)
        else:
            print('搜索公开模板含 有“模板”的文件，结果为空')

    def test30_filter_public(self):
        """过滤为免费公开模板程序列表"""
        url=self.post_url+'/public'
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','price':'free'}
        r = requests.get(url,params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        if r.json()['total']!=0:
            print("过滤为免费公开模板程序列表第一页")
            print(r.text)
        else:
            print('无免费模板')

    def test31_filter_public(self):
        """过滤公开模板程序列表：类型"""
        url=self.post_url+'/public'
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','class':'焊接'}
        r = requests.get(url,params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        if r.json()['total']!=0:
            print("过滤类型：“焊接”，公开模板程序列表第一页")
            print(r.text)
        else:
            print('过滤类型：“焊接”，结果为空')

    def test32_filter_public(self):
        """过滤公开模板程序列表：型号"""
        url=self.post_url+'/public'
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','model':'Q','class':'焊接','price':'free'}
        r = requests.get(url,params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        if r.json()['total']!=0:
            print("过滤型号：“Q” & 类型：“焊接” & 免费，公开模板程序列表第一页")
            print(r.text)
        else:
            print('过滤型号：“Q” & 类型：“焊接” & 免费，结果为空')

    def test33_filter_public(self):
        """过滤公开模板程序列表：综合过滤条件"""
        url=self.post_url+'/public'
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','model':'Q'}
        r = requests.get(url,params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        if r.json()['total']!=0:
            print("过滤型号：“Q”，公开模板程序列表第一页")
            print(r.text)
        else:
            print('过滤型号：“Q”返回结果为空')

    def test50_clearall(self):
        """清空模板列表和回收站"""
        print('清空模板列表')
        self.test18_deletetmpl_allID()
        print('清空模板回收站')
        self.test21_deleterecycle_allID()

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
    # f=post_request()
    # f.setUp()
    # # f.test_create_tmplprogram_01()
    # f.modify_tmplprogram()
    # f.test_modifytmpl_public_11()
    # f.test2700_download_onetmpl()




