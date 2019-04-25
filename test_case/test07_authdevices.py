# coding:utf-8
import requests
import json
import unittest
from common import readconfig
from common import get_token
from common import get_device
from test_case import test06_factorydevices
from common import search_list
import random



class post_request(unittest.TestCase):
    def setUp(self):
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        self.post_url = '%s%s/authdevices'%(API,Prefix)  #create authdevices接口
        self.t=get_token.GetToken()
        token=self.t.test_token()
        self.header= {
        'content-type': "application/json",
        'authorization':token,
        'x-platform':"web",
        'x-module-id': "feead8e4b3443077d5b28e29288fbf4c"
        }

    def test01_create_authdevices(self):
        """添加授权设备"""
        devices=get_device.GetDevices().test_readdevices()
        url=self.post_url
        header = self.header
        for device in devices:
            data={
                    "name": "%s"%device[0],
                    "serial": "%s"%device[1],
                    "status":1,        #状态已激活
                    "expire_date": "2040-08-08 23:59:59",
                    "remark": "测试remark",
                    "company": {
                        "name": "%s"%device[2],
                        "province": "%s"%device[3],
                        "city": "%s"%device[4],
                        "district": "%s"%device[5],
                        "remark": "%s"%device[6]
                    }
                }
            r = requests.post(url, data=json.dumps(data), headers=header)
            self.assertEqual(r.status_code,201)
            print('成功添加授权设备：%s'%device[0])
            print(r.text)

    def test02_auth_duplicate(self):
        """重复添加授权设备：device already exists"""
        devices=get_device.GetDevices().test_readdevices()
        url=self.post_url
        header = self.header
        for device in devices:
            data={
                    "name": "%s"%device[0],
                    "serial": "%s"%device[1],
                    "status":1,        #状态已激活
                    "expire_date": "2040-08-08 23:59:59",
                    "remark": "测试remark",
                    "company": {
                        "name": "%s"%device[2],
                        "province": "%s"%device[3],
                        "city": "%s"%device[4],
                        "district": "%s"%device[5],
                        "remark": "%s"%device[6]
                    }
                }
            r = requests.post(url, data=json.dumps(data), headers=header)
            self.assertEqual(r.json()['code'],4115)
            print('不可以重复授权设备：%s'%device[0])
            print(r.json()['error'])


    def test03_auth_illegal(self):
        """授权设备sn号不存在：illegal serial"""
        url=self.post_url
        header = self.header
        data={
                "name": "不存在设备",
                "serial": "0ebdb826-2fa2-43d0-b1e8-389a46b29c47",   #SN格式正确，但是不存在出厂设备列表中
                "status":1,        #状态已激活
                "expire_date": "2040-08-08 23:59:59",
                "remark": "测试不存在设备",
                "company": {
                    "name": "测试1",
                    "province": "浙江",
                    "city": "杭州市",
                    "district": "拱墅区",
                    "remark": "祥园路108号"
                }
            }
        r = requests.post(url, data=json.dumps(data), headers=header)
        self.assertEqual(r.json()['code'],4116)
        print('不存在的设备序列号：')
        print(r.json()['error'])

    def test04_auth_invalid(self):
        """添加sn格式非法：invalid device serial"""
        url=self.post_url
        header = self.header
        data={
                "name": "非法sn",
                "serial": "0ebdb826-2fa2-43d0",   #SN格式非法。
                "status":1,        #状态已激活
                "expire_date": "2040-08-08 23:59:59",
                "remark": "非法sn",
                "company": {
                    "name": "测试1",
                    "province": "浙江",
                    "city": "杭州市",
                    "district": "拱墅区",
                    "remark": "祥园路108号"
                }
            }
        r = requests.post(url, data=json.dumps(data), headers=header)
        self.assertEqual(r.json()['code'],4006)
        print('非法序列号：')
        print(r.json()['error'])

    def test05_getlist_authdevices(self):
        """获取授权设备列表，并分页"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print(r.text)

    def test06_searchlist_authdevices(self):
        """调用common方法：搜索授权设备列表"""
        print("授权设备列表搜索key：")
        url=self.post_url
        header = self.header
        key="64"
        r=search_list.SearchList()
        r.search(url,header,key)


    def test07_filter_list(self):
        """授权设备列表过滤条件：状态：未激活"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','status':'0'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('过滤“未激活”的授权设备列表：\n%s'%r.text)

    def test08_filter_list(self):
        """授权设备列表过滤条件：状态：已激活"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','status':'1'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('过滤“已激活”的授权设备列表：\n%s'%r.text)

    def test09_filter_list(self):
        """授权设备列表过滤条件：状态：已过期"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','status':'2'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('过滤“已过期”的授权设备列表：\n%s'%r.text)

    def test10_sortlist_name(self):
        """授权列表按“设备名称”升序排序：name"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"name"}'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('授权列表按“设备名称”升序排序：\n%s'%r.text)

    def test11_sortlist_name(self):
        """授权列表按“设备名称”降序排序：name"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-name"}'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('授权列表按“设备名称”降序排序：\n%s'%r.text)

    def test09_sortlist_company(self):
        """授权列表按“公司名称”升序排序：company.name"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"company.name"}'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('授权列表按“公司名称”升序排序：\n%s'%r.text)

    def test10_sortlist_company(self):
        """授权列表按“公司名称”降序排序：company.name"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-company.name"}'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('授权列表按“公司名称”降序排序：\n%s'%r.text)

    def test11_sortlist_activate_status(self):
        """授权列表按“激活状态”升序排序：activate_status"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"activate_status"}'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('授权列表按“激活状态”升序排序：\n%s'%r.text)

    def test12_sortlist_activate_status(self):
        """授权列表按“激活状态”降序排序：activate_status"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-activate_status"}'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('授权列表按“激活状态”降序排序：\n%s'%r.text)

    def test13_sortlist_expire_date(self):
        """授权列表按“有效期”升序排序：expire_date"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"expire_date"}'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('授权列表按“有效期”升序排序：\n%s'%r.text)

    def test14_sortlist_expire_date(self):
        """授权列表按“有效期”降序排序：expire_date"""
        url=self.post_url
        header = self.header
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-expire_date"}'}
        r = requests.get(url, params=payload, headers=header)
        self.assertEqual(r.status_code,200)
        print('授权列表按“有效期”降序排序：\n%s'%r.text)

    def test15_newdevices_allID(self):
        """返回新授权设备的id号"""
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
            print('授权列表为空')
        print("get新授权设备的id:%s "%t)
        return t

    def test16_get_one(self):
        """查看某个id详细信息"""
        t=self.test15_newdevices_allID()
        t1=t[0]
        url=self.post_url+'/%s'%t1
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        print('id号：%s 授权设备详细信息：\n%s'%(t1,r.text))

    def test17_updateone_name(self):
        """修改记录的设备名"""
        t=self.test15_newdevices_allID()
        t1=t[0]
        url=self.post_url+'/%s'%t1
        header = self.header
        data={
                "name": "修改—设备名"
            }
        r = requests.patch(url,data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,202)
        print('id号：%s 设备名已更新：\n%s'%(t1,r.text))

    def test18_updateone_company(self):
        """修改记录的公司信息"""
        t=self.test15_newdevices_allID()
        t1=t[0]
        url=self.post_url+'/%s'%t1
        header = self.header
        data={
                "company": {
                        "name": "修改-公司名称",
                        "province": "江苏",
                        "city": "南京市",
                        "district": "江宁区",
                        "remark": "修改--公司地址改为江苏省"
                    }
            }
        r = requests.patch(url,data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,202)
        print('id号：%s 公司信息已更新：\n%s'%(t1,r.text))

    def test19_updateone_status(self):
        """修改记录的激活状态"""
        t=self.test15_newdevices_allID()
        t1=t[0]
        url=self.post_url+'/%s'%t1
        header = self.header
        data={
              "status": 0
            }
        r = requests.patch(url,data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,202)
        print('id号：%s 状态更新为“未激活”：\n%s'%(t1,r.text))

    def test20_updateone_date(self):
        """修改记录的有效期"""
        t=self.test15_newdevices_allID()
        t1=t[0]
        url=self.post_url+'/%s'%t1
        header = self.header
        data={
              "expire_date": "2022-01-11 23:59:59"
            }
        r = requests.patch(url,data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,202)
        print('id号：%s 修改有效期时间：\n%s'%(t1,r.text))

    def test21_updateone_remark(self):
        """修改记录的备注信息"""
        t=self.test15_newdevices_allID()
        t1=t[0]
        url=self.post_url+'/%s'%t1
        header = self.header
        data={
              "remark": "修改--备注信息",
            }
        r = requests.patch(url,data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,202)
        print('id号：%s 修改备注信息：\n%s'%(t1,r.text))


    def test22_count_all(self):
        """统计全部省份下的所有公司数量和设备数量"""
        url=self.post_url+'/count'
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        print('统计全部省份下的所有公司数量和设备数量：\n%s'%r.text)
        print('统计全部公司数量：%s'%r.json()['data'][0]['total_com'])
        print('统计全部设备数量：%s'%r.json()['data'][0]['total_dev'])

    def test23_return_provices(self):
        """遍历返回所有包含省份"""
        url=self.post_url+'/count'
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        prov=r.json()['data'][0]['provinces']
        provinces=[]
        print('遍历统计包含的省份为：')
        for k in prov:
            provinces.append(k['name'])
            print(k['name'])
        return provinces

    def test24_countby_prov(self):
        """遍历统计各个省份下的设备总数和公司总数"""
        provs=self.test23_return_provices()
        for prov in provs:
            url=self.post_url+'/%s'%prov
            header = self.header
            r = requests.get(url, headers=header)
            self.assertEqual(r.status_code,200)
            print('按省份：%s 统计所有设备总数和公司总数：\n%s'%(prov,r.text))


    def getall_prov_comp(self):
        """遍历所有省份及公司名称"""
        provs=self.test23_return_provices()
        prov_list=[]
        for prov in provs:
            url=self.post_url+'/%s'%prov
            header = self.header
            r = requests.get(url, headers=header)
            self.assertEqual(r.status_code,200)
            coms=r.json()['data']['com_list']
            for com in coms:
                d={}
                d[prov]=com
                prov_list.append(d)
        return prov_list

    def test25_countby_prov_comp(self):
        """遍历统计每个省份下每个公司名下的设备总数"""
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        provs=self.getall_prov_comp()
        print(provs)
        for prov in provs:
            for element in prov:
                url='%s%s/auth-devices'%(API,Prefix)+'/%s'%element+'/%s'%prov[element]    # 晕死，主接口名不一致，重新定义
                header = self.header
                r = requests.get(url, headers=header)
                # self.assertEqual(r.status_code,200)
                print('按省份：%s &公司名称：%s 统计的设备总数：\n%s'%(element,prov[element],r.text))

    def test26_delete_one(self):
        """删除一条授权信息"""
        t=self.test15_newdevices_allID()
        t1=t[0]
        url=self.post_url+'/%s'%t1
        header = self.header
        r = requests.delete(url, headers=header)
        self.assertEqual(r.status_code,204)
        print('id号：%s 授权设备删除成功：\n%s'%(t1,r.text))


    def test27_delete_factorydevices(self):
        """删除新添加设备的出厂设备记录"""
        tr=test06_factorydevices.post_request()
        tr.setUp()
        tr.delete_allid()


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
    # r=post_request()
    # r.setUp()
    # r.test25_countby_prov_comp()
