# coding:utf-8
import requests
import json
import unittest
from common import readconfig
from common import get_token
from common import random_char
from common import get_list_id
from common import search_list
from common import common_settings
from test_case import test06_factorydevices
import random
import configparser
import ast

class post_request(unittest.TestCase):
    def setUp(self):
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        self.post_url = '%s%s/robots'%(API,Prefix)  # robots 接口
        self.t=get_token.GetToken()
        token=self.t.test_token()
        self.header= {
            'content-type': "application/json",
            'authorization':token,
            'x-platform':"web",
            'x-module-id': "bb0ae97fa4e1ef6de884f3ce13029376"
        }

    def test01_robots_create(self):
        """添加运行设备的虚拟数据，机器序列号必须与授权设备添加一致。"""
        print('读取info文件中记录的添加出厂设备：sr_list.')
        cf=configparser.ConfigParser()
        cf.read('C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\test_api\\info.txt')
        sr_list=cf.get('devices', 'sr_list')
        srs=ast.literal_eval(sr_list)
        url=self.post_url
        header = self.header
        if srs!=[]:
            print('开始添加授权设备信息的robots信息：')
            for sr in srs:
                self.random=random_char.RandomChar()
                name=self.random.random_char([],4,2)   # 生成4位长度混合字符串
                ver=self.random.random_char(["Ver_"],5,2)   # 随机版本号
                ip=random.randint(1,220)    # 随机ip地址
                status=["running","not connected","stopping","malfunction","free","pausing"]
                sta=random.choice(status)
                data={
                       "dev_info": {
                           "name": "虚拟连接设备--%s"%name,
                           "serial": "%s"%sr,
                           "model": "scara-400",
                           "ip": "192.168.1.%s"%ip,
                           "ctrl_ver": "%s"%ver
                       },
                       "run_info": {
                           "status": "%s"%sta,
                           "error": {
                               "code": 123,
                               "description": "限位急停"
                           },
                           "script": {
                               "name": "test.lua",
                               "count": 100
                           }
                       },
                       "joint_info": [
                           {
                               "name": "j0",
                               "voltage": 45,
                               "current": 1.2,
                               "temperatrue": 60,
                               "velocity": 0.1,
                               "position": 0
                           },
                           {
                               "name": "j1",
                               "voltage": 48.36,
                               "current": 1.2,
                               "temperatrue": 50,
                               "velocity": 0.1,
                               "position": 0
                           },
                           {
                               "name": "j2",
                               "voltage": 46.2,
                               "current": 1.2,
                               "temperatrue": 20,
                               "velocity": 0.1,
                               "position": 0
                           },
                           {
                               "name": "j3",
                               "voltage": 47.5,
                               "current": 1.2,
                               "temperatrue": 30,
                               "velocity": 0.1,
                               "position": 0
                           }
                       ]
                }
                r = requests.post(url, data=json.dumps(data), headers=header)
                self.assertEqual(r.status_code,201)
                if r.json()['total']==1:
                    print('添加虚拟的连接设备信息：%s'%sr)
                else:
                    print('添加错误数据')

        else:
            print('添加出厂设备信息为空，无法添加监控信息。')

    def test02_robots_getlist(self):
        """查找所有连接过服务器的设备"""
        url=self.post_url
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        if r.json()['total']!=0:
            print('在线设备总数：%s\n%s'%(r.json()['total'],r.text))
        else:
            print('连接服务器的设备列表为空。')

    def test03_robots_getone(self):
        """查看某一个设备状态详细情况"""
        print('先获得某一个充值请求的id.')
        url1=self.post_url
        header = self.header
        rt=get_list_id.GetListID()
        id=rt.test_getoneid(url1,header)
        url=self.post_url+'/%s'%id
        r = requests.get(url,headers=header)
        self.assertEqual(r.status_code,200)
        print('查看id: %s 的设备状态详细情况：\n%s'%(id,r.text))

    def test04_search_list(self):
        """调用common方法：设备状态列表搜索功能测试"""
        print("设备状态列表搜索key：")
        url=self.post_url
        header = self.header
        key="71"
        r=search_list.SearchList()
        r.search(url,header,key)

    def test05_filter_list(self):
        """遍历状态列表，进行过滤"""
        url=self.post_url
        header = self.header
        status=["running","not connected","stopping","malfunction","free","pausing"]
        for sta in status:
            payload = {'page[offset]': '0', 'page[limit]': '5','status':'%s'%sta}
            r = requests.get(url, params=payload, headers=header)
            self.assertEqual(r.status_code,200)
            print('过滤监控状态：%s 设备信息：\n%s'%(sta,r.text))

    def test06_sortlist_name(self):
        """设备监控信息dev_info.name：设备名 升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"dev_info.name"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('设备监控信息“设备名”升序排序：%s'%r.text)

    def test07_sortlist_name(self):
        """设备监控信息dev_info.name：帐户 降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-dev_info.name"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('设备监控信息“设备名”降序排序：%s'%r.text)

    def test08_sortlist_ip(self):
        """设备监控信息dev_info.ip：ip 升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"dev_info.ip"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('设备监控信息“ip”升序排序：%s'%r.text)

    def test09_sortlist_ip(self):
        """设备监控信息dev_info.ip：ip 降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-dev_info.ip"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('设备监控信息“ip”降序排序：%s'%r.text)

    def test10_sortlist_ctrl_ver(self):
        """设备监控信息dev_info.ctrl_ver：控制器版本 升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"dev_info.ctrl_ver"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('设备监控信息“控制器版本”升序排序：%s'%r.text)

    def test11_sortlist_ctrl_ver(self):
        """设备监控信息dev_info.ctrl_ver：控制器版本 降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-dev_info.ctrl_ver"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('设备监控信息“控制器版本”降序排序：%s'%r.text)

    def test12_sortlist_product_date(self):
        """设备监控信息dev_info.product_date：生产日期 升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"dev_info.product_date"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('设备监控信息“生产日期”升序排序：%s'%r.text)

    def test13_sortlist_product_date(self):
        """设备监控信息dev_info.product_date：生产日期 降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-dev_info.product_date"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('设备监控信息“生产日期”降序排序：%s'%r.text)

    def test14_sortlist_status(self):
        """设备监控信息run_info.status：状态 升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"run_info.status"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('设备监控信息“状态”升序排序：%s'%r.text)

    def test15_sortlist_status(self):
        """设备监控信息run_info.status：状态降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-run_info.status"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('设备监控信息“状态”降序排序：%s'%r.text)

    def test16_sortlist_suffice(self):
        """设备监控信息product_data.suffice：完成数量 升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"product_data.suffice"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('设备监控信息“完成数量”升序排序：%s'%r.text)

    def test17_sortlist_suffice(self):
        """设备监控信息product_data.suffice：完成数量 降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-product_data.suffice"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('设备监控信息“完成数量”降序排序：%s'%r.text)

    def test18_sortlist_aim(self):
        """设备监控信息product_data.aim：目标台数 升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"product_data.aim"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('设备监控信息“目标台数”升序排序：%s'%r.text)

    def test19_sortlist_aim(self):
        """设备监控信息product_data.aim：目标台数 降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-product_data.aim"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('设备监控信息“目标台数”降序排序：%s'%r.text)

    def test20_sortlist_pass_rate(self):
        """设备监控信息product_data.pass_rate：合格率 升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"product_data.pass_rate"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('设备监控信息“合格率”升序排序：%s'%r.text)

    def test21_sortlist_pass_rate(self):
        """设备监控信息product_data.pass_rate：合格率 降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-product_data.pass_rate"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('设备监控信息“合格率”降序排序：%s'%r.text)

    def test22_robots_clearall(self):
        """清空设备状态列表"""
        print('先get list,并返回所有设备的id')
        url1=self.post_url
        header = self.header
        rt=get_list_id.GetListID()
        t_list=rt.test_getallid(url1,header)
        """传入id参数，调用下一个接口"""
        print('清除所有设备监控信息：')
        for t in t_list:
            url=self.post_url+'/%s'%t
            header = self.header
            r = requests.delete(url, headers=header)
            self.assertEqual(r.status_code,204)
            print(t)

    def test23_delete_factorydevices(self):
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
    # # r.test01_robots_create()
    # # r.test05_filter_list()
    # r.test22_robots_clearall()
