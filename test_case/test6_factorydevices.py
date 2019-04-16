# coding:utf-8
import requests
import json
import unittest
from common import readconfig
from common import get_token
from common import get_device
import random



class post_request(unittest.TestCase):
    def setUp(self):
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        self.post_url = '%s%s/factorydevices'%(API,Prefix)  #create factorydevices接口
        self.t=get_token.GetToken()
        token=self.t.test_token()
        self.header= {
        'content-type': "application/json",
        'authorization':token,
        'x-platform':"web",
        'x-module-id': "a07120661734420a4f577898f46e4fa7"
        }

    def test01_createprogram(self):
        """读取本地测试设备文件，添加新的出厂设备"""
        devices=get_device.GetDevices().test_readdevices()
        url=self.post_url
        header = self.header
        for device in devices:
            data={
                "name": "%s"%device[0],
                "serial": "%s"%device[1],
                "status": random.randint(0,3),
                "ctrl_ver": "V_1.2.1",
                "driver_ver": "V_8.3",
                "product_date": "2018-08-08",
                "maintain_times": 0
            }
            r = requests.post(url, data=json.dumps(data), headers=header)
            self.assertEqual(r.status_code,201)
            print('成功添加设备：%s'%device[0])
            print(r.text)

    def test02_newdevices_allID(self):
        """上个用例添加新设备的id号返回"""
        url=self.post_url
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        n=r.json()['total']
        if n!=0:
            t=[]
            for index in range(0,5):       #个数写死，设备文件中的设备数为5
                t.append(r.json()['data'][index]['id'])
        else:
            t=''
            print('设备列表为空')
        print("get添加设备的id:%s "%t)
        return t

    def test03_create_exists(self):
        """重复添加出厂设备，error返回：device already exists"""
        devices=get_device.GetDevices().test_readdevices()
        url=self.post_url
        header = self.header
        for device in devices:
            data={
                "name": "%s"%device[0],
                "serial": "%s"%device[1],
                "status": random.randint(0,3),
                "ctrl_ver": "V_1.2.1",
                "driver_ver": "V_8.3",
                "product_date": "2018-08-08",
                "maintain_times": 0
            }
            r = requests.post(url, data=json.dumps(data), headers=header)
            self.assertEqual(r.json()['code'],4115)
            print('不可以重复添加设备：%s'%device[0])
            print(r.json()['error'])

    def test04_create_invalid(self):
        """添加无效序列号，error返回：invalid device serial"""
        url=self.post_url
        header = self.header
        data={
            "name": "测试error",
            "serial": "1234",      #错误的sr号
            "status": random.randint(0,3),
            "ctrl_ver": "V_1.2.1",
            "driver_ver": "V_8.3",
            "product_date": "2018-08-08",
            "maintain_times": 0
        }
        r = requests.post(url, data=json.dumps(data), headers=header)
        self.assertEqual(r.json()['code'],4006)
        print('无效的设备序列号：')
        print(r.json()['error'])

    def test05_getlist_factorydevices(self):
        """获取出厂设备列表，并分页"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print(r.text)

    def test06_searchlist_factorydevices(self):
        """搜索出厂设备列表"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','search':'64'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        if r.json()['total']!=0:
            print('搜索：64 返回结果为：\n%s'%r.text)
        else:
            print('搜索结果为空！')

    def test07_sortlist_ctrl_ver(self):
        """设备列表按“控制器版本”升序排序：ctrl_ver"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"ctrl_ver"}'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('设备列表按“控制器版本”升序排序：\n%s'%r.text)

    def test08_sortlist_ctrl_ver(self):
        """设备列表按“控制器版本”降序排序：ctrl_ver"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-ctrl_ver"}'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('设备列表按“控制器版本”降序排序：\n%s'%r.text)

    def test09_sortlist_driver_ver(self):
        """设备列表按“驱动器版本”升序排序：driver_ver"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"driver_ver"}'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('设备列表按“驱动器版本”升序排序：\n%s'%r.text)

    def test10_sortlist_driver_ver(self):
        """设备列表按“驱动器版本”降序排序：driver_ver"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-driver_ver"}'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('设备列表按“驱动器版本”降序排序：\n%s'%r.text)

    def test11_sortlist_status(self):
        """设备列表按“状态”升序排序：status"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"status"}'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('设备列表按“状态”升序排序：\n%s'%r.text)

    def test12_sortlist_status(self):
        """设备列表按“状态”降序排序：status"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-status"}'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('设备列表按“状态”降序排序：\n%s'%r.text)

    def test13_sortlist_maintain_times(self):
        """设备列表按“维修次数”升序排序：maintain_times"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"maintain_times"}'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('设备列表按“维修次数”升序排序：\n%s'%r.text)

    def test14_sortlist_maintain_times(self):
        """设备列表按“维修次数”降序排序：maintain_times"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-maintain_times"}'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('设备列表按“维修次数”降序排序：\n%s'%r.text)

    def test15_sortlist_product_date(self):
        """设备列表按“生产日期”升序排序：product_date"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"product_date"}'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('设备列表按“生产日期”升序排序：\n%s'%r.text)

    def test16_sortlist_product_date(self):
        """设备列表按“生产日期”降序排序：product_date"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-product_date"}'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('设备列表按“生产日期”降序排序：\n%s'%r.text)

    def test17_filter_list(self):
        """设备列表过滤条件：状态：未出产"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','status':'0'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('过滤“未出产”的设备列表：\n%s'%r.text)

    def test18_filter_list(self):
        """设备列表过滤条件：状态：已交付"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','status':'1'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('过滤“已交付”的设备列表：\n%s'%r.text)

    def test19_filter_list(self):
        """设备列表过滤条件：状态：维修中"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','status':'2'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('过滤“维修中”的设备列表：\n%s'%r.text)

    def test20_filter_list(self):
        """设备列表过滤条件：状态：已报废"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','status':'3'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('过滤“已报废”的设备列表：\n%s'%r.text)

    def test21_get_one(self):
        """查看某个id详细信息"""
        t=self.test02_newdevices_allID()
        t1=t[0]
        url=self.post_url+'/%s'%t1
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        print('id号：%s 设备详细信息：\n%s'%(t1,r.text))

    def test22_updateone_status(self):
        """更新设备信息：状态改为维修中"""
        t=self.test02_newdevices_allID()
        t1=t[0]
        url=self.post_url+'/%s'%t1
        header = self.header
        data={
            "status":2
        }
        r = requests.patch(url,data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,201)
        print('id号：%s 状态已更新：\n%s'%(t1,r.text))

    def test23_updateone_ctrl_ver(self):
        """更新设备信息：控制器版本"""
        t=self.test02_newdevices_allID()
        t1=t[0]
        url=self.post_url+'/%s'%t1
        header = self.header
        data={
            "ctrl_ver": "修改_V.1"
        }
        r = requests.patch(url,data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,201)
        print('id号：%s 控制器版本已更新：\n%s'%(t1,r.text))

    def test24_updateone_driver_ver(self):
        """更新设备信息：驱动器版本"""
        t=self.test02_newdevices_allID()
        t1=t[0]
        url=self.post_url+'/%s'%t1
        header = self.header
        data={
            "driver_ver": "修改_V8"
        }
        r = requests.patch(url,data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,201)
        print('id号：%s 驱动器版本已更新：\n%s'%(t1,r.text))

    def test25_updateone_product_date(self):
        """更新设备信息：出厂日期"""
        t=self.test02_newdevices_allID()
        t1=t[0]
        url=self.post_url+'/%s'%t1
        header = self.header
        data={
            "product_date": "2017-07-07"
        }
        r = requests.patch(url,data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,201)
        print('id号：%s 出厂日期已更新：\n%s'%(t1,r.text))

    def test26_updateone_maintain_times(self):
        """更新设备信息：维修次数"""
        t=self.test02_newdevices_allID()
        t1=t[0]
        url=self.post_url+'/%s'%t1
        header = self.header
        data={
            "maintain_times": 5
        }
        r = requests.patch(url,data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,201)
        print('id号：%s 维修次数更新：\n%s'%(t1,r.text))

    def delete_allid(self):
        """删除添加的所有设备Id"""
        ids=self.test02_newdevices_allID()
        header = self.header
        for id in ids:
            url=self.post_url+'/%s'%id
            r = requests.delete(url, headers=header)
            self.assertEqual(r.status_code,204)
            print('成功删除设备：%s'%id)


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()