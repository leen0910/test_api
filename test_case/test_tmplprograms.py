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
        data={
          "name": "模板程序测试%s"%n,
          "author": "%s"%account,
          "size": 100,
          "data": "[{\"label\":\"涂胶模板\",\"name\":\"program\",\"id\":\"ae7c588f-bb98-42fd-99ea-f38045bb8f33\",\"data\":{\"version\":\"1.7.1\",\"machine\":\"QRST4-05401500\",\"main_io\":\"3.2M\",\"tool_io\":\"3.2T\",\"author\":\"root\",\"c_time\":\"2019-03-11 13:29:20\",\"m_time\":\"2019-03-26 10:01:12\",\"size\":1858,\"md5\":\"6de553f91ba95db22ecbb02cd16e82c9\",\"style\":\"template\",\"types\":\"\"},\"children\":[{\"label\":\"点到点\",\"name\":\"p2p\",\"data\":{\"x\":400,\"y\":0,\"z\":0,\"rz\":0}}]},{\"label\":\"全局变量\",\"name\":\"g_variable\",\"children\":[{\"label\":\"arm\",\"name\":\"variable\",\"id\":\"fbd6529e-c55e-4f04-a292-9028df0c4208\",\"comment\":\"左右臂\",\"data\":{\"value\":\"right\"}},{\"label\":\"ref_sys\",\"name\":\"variable\",\"id\":\"3efb5952-8635-4432-972a-d4009b45595b\",\"comment\":\"坐标系\",\"data\":{\"value\":\"abc228bc-1aa8-49bb-8b5a-e87567624d02\"}},{\"label\":\"wait_finish\",\"name\":\"variable\",\"id\":\"36481789-c875-4f2e-9bc7-d7730eddb835\",\"comment\":\"等待运动完成\",\"data\":{\"value\":true}},{\"label\":\"j_vel\",\"name\":\"variable\",\"id\":\"43e1d9af-4043-4a82-abf6-d4c8c3457f0a\",\"comment\":\"关节速度\",\"data\":{\"value\":0.5}},{\"label\":\"j_acc\",\"name\":\"variable\",\"id\":\"a9a96478-8766-420b-830b-95e0149c9476\",\"comment\":\"关节加速度\",\"data\":{\"value\":0.5}},{\"label\":\"j_dec\",\"name\":\"variable\",\"id\":\"662539a1-ccb6-460d-8f68-81dde512e283\",\"comment\":\"关节减速度\",\"data\":{\"value\":0.5}},{\"label\":\"l_vel\",\"name\":\"variable\",\"id\":\"24c36be7-a96d-4270-aa2e-63961cb523cb\",\"comment\":\"曲线速度\",\"data\":{\"value\":100}},{\"label\":\"l_acc\",\"name\":\"variable\",\"id\":\"126d0440-7bb3-4caf-922b-68e2a9630fa2\",\"comment\":\"曲线加速度\",\"data\":{\"value\":500}},{\"label\":\"l_dec\",\"name\":\"variable\",\"id\":\"27c204d3-ea96-4f7e-8844-0bec11400b61\",\"comment\":\"曲线减速度\",\"data\":{\"value\":500}},{\"label\":\"rel\",\"name\":\"variable\",\"id\":\"0647b6e6-2259-4f27-a038-bc6a93e8534e\",\"comment\":\"相对逼近\",\"data\":{\"value\":0.5}}]},{\"label\":\"坐标系\",\"name\":\"all_sys\",\"children\":[{\"label\":\"世界坐标系\",\"name\":\"world_sys\",\"id\":\"abc228bc-1aa8-49bb-8b5a-e87567624d02\",\"data\":{\"x\":0,\"y\":0,\"z\":0,\"rx\":0,\"ry\":0,\"rz\":0}}]}]",
          "version":"1.7.1",
          "types":"焊接",
          "machine":"QRST4-05401500"
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
        print("获取模板程序文件列表")
        if r.json()['total']!=0:
            t=r.json()['data'][0]['id']
        else:
            t=''
            print('模板程序列表为空')
        return t
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
        a=random.uniform(1,500)
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
        data ={"public":bool(1)}  #随机生成两位小数价格
        if url:
            r = requests.patch(url, data=json.dumps(data), headers=header)
            print(r.text)
            self.assertEqual(r.status_code,200)
        else:
            print('无模板程序设置为公开')

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

    def test14_get_recycleprogram(self):
        """得到模板文件回收站列表"""
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

    def test15_gettmpl_allID(self):
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

    # def test16_deletetmpl_allID(self):
    #     """删除所有模板程序文件"""
    #     r=self.test02_get_tmplprogram()
    #     if r:
    #         print("删除列表中所有模板程序：")
    #         t_list=self.test15_gettmpl_allID()
    #         for t in t_list:
    #             url=self.post_url+'/%s'%t  #传入删除程序id
    #             header = self.header
    #             r=requests.delete(url,headers=header)
    #             self.assertEqual(r.status_code,204)
    #             print('成功删除模板程序文件id：%s'%t)
    #     else:
    #         print('模板程序列表已经为空')

    def test17_recycleRecover_1stID(self):
        """回收站模板程序列表第一个文件还原"""
        r=self.test14_get_recycleprogram()
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

    def test18_get_recycletmpl_allID(self):
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

    def test19_deleterecycle_allID(self):
        """删除回收站的所有模板程序文件"""
        t_list=self.test18_get_recycletmpl_allID()
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

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
    # f=post_request()
    # f.setUp()
    # # f.test_create_tmplprogram_01()
    # f.modify_tmplprogram()
    # f.test_modifytmpl_public_11()




