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
import random

class post_request(unittest.TestCase):
    def setUp(self):
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        self.post_url = '%s%s/recharges'%(API,Prefix)  # recharges接口
        self.user=self.rt.get_account()
        self.t=get_token.GetToken()
        token=self.t.test_token()
        self.header= {
            'content-type': "application/json",
            'authorization':token,
            'x-platform':"web",
            'x-module-id': "161d77bb7e99f472f61ede6629b73ee6"
        }

    def test01_recharges_create(self):
        """提交充值请求: 接口校验不完善，account应该与登录帐户保持一致"""
        url=self.post_url
        header = self.header
        user=self.user
        self.random=random_char.RandomChar()
        num=self.random.random_char([],20,2)   # 生成20位长度混合字符串
        money=int(self.random.random_char([],3,0))   # 生成3位长度数字
        t=self.random.localtime()    # 格式化生成当前时间戳
        n=random.randint(0,2)   # 随机付款方式
        data={
            "partner":"%s"%user,
            "num":"%s"%num,
            "money":money,
            "time":"%s"%t,
            "method":n,
            "contact":"test1234@163.com"
        }
        r = requests.post(url, data=json.dumps(data), headers=header)
        print(r.text)
        self.assertEqual(r.status_code,201)
        if r.json()['total']==1:
            print('用户：%s，提交充值：%s的申请'%(r.json()['data'][0]['partner'],r.json()['data'][0]['money']))
        else:
            print('添加错误数据')

    def test02_recharges_add10(self):
        """为测试需求，调用上一接口添加10条充值记录"""
        print('添加10条充值记录：')
        for i in range(10):
            self.test01_recharges_create()

    def test03_recharges_getlist(self):
        """获取充值请求列表"""
        url=self.post_url
        header = self.header
        r = requests.get(url,headers=header)
        self.assertEqual(r.status_code,200)
        print('获取充值请求列表：%s'%r.text)

    def test04_sortlist_partner(self):
        """充值请求列表partner：帐户 升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"partner"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('充值请求列表“帐户”升序排序：%s'%r.text)

    def test05_sortlist_partner(self):
        """充值请求列表partner：帐户 降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-partner"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('充值请求列表“帐户”降序排序：%s'%r.text)

    def test06_sortlist_method(self):
        """充值请求列表method：交易方式 升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"method"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('充值请求列表“交易方式”升序排序：%s'%r.text)

    def test07_sortlist_method(self):
        """充值请求列表method：交易方式 降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-method"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('充值请求列表“交易方式”降序排序：%s'%r.text)

    def test08_sortlist_money(self):
        """充值请求列表money：金额 升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"money"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('充值请求列表“金额”升序排序：%s'%r.text)

    def test09_sortlist_money(self):
        """充值请求列表money：金额 降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-money"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('充值请求列表“金额”降序排序：%s'%r.text)

    def test10_sortlist_time(self):
        """充值请求列表time：付款时间 升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"time"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('充值请求列表“付款时间”升序排序：%s'%r.text)

    def test11_sortlist_time(self):
        """充值请求列表time：付款时间 降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-time"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('充值请求列表“付款时间”降序排序：%s'%r.text)

    def test12_search_list(self):
        """下载申请列表搜索功能测试"""
        print("充值请求列表搜索key：")
        url=self.post_url
        header = self.header
        key="2019"
        r=search_list.SearchList()
        r.search(url,header,key)

    def test13_get_method(self):
        """获取支付方式"""
        url=self.post_url+'/methods'
        header = self.header
        r = requests.get(url,headers=header)
        self.assertEqual(r.status_code,200)
        print('支持的支付方式：%s'%r.text)

    def test14_recharges_getone(self):
        """查看某一个Id的充值请求"""
        print('先获得某一个充值请求的id.')
        url1=self.post_url
        header = self.header
        rt=get_list_id.GetListID()
        id=rt.test_getoneid(url1,header)
        url=self.post_url+'/%s'%id
        r = requests.get(url,headers=header)
        self.assertEqual(r.status_code,200)
        print('查看id: %s 的充值请求：\n%s'%(id,r.text))

    def test15_delete_one(self):
        """删除某一个Id的充值请求"""
        print('先获得某一个充值请求的id.')
        url1=self.post_url
        header = self.header
        rt=get_list_id.GetListID()
        id=rt.test_getoneid(url1,header)
        url=self.post_url+'/%s'%id
        r = requests.delete(url,headers=header)
        self.assertEqual(r.status_code,204)
        print('删除id: %s 的充值请求：\n%s'%(id,r.text))

    def test16_post_settings(self):
        """调用common_settings配置充值请求列表订阅邮件列表"""
        module_id="161d77bb7e99f472f61ede6629b73ee6"
        email1="16951414@qq.com"
        email2="leen0910@gmail.com"
        r=common_settings.post_request(module_id)
        r.test1_post_settings(email1,email2)
        # r.test2_get_settings()
        # r.test3_clear_settings()

    def test17_get_settings(self):
        """调用common_settings获取充值请求列表订阅邮件列表"""
        module_id="161d77bb7e99f472f61ede6629b73ee6"
        r=common_settings.post_request(module_id)
        r.test2_get_settings()


    def test18_recharges_process(self):
        """处理充值请求(发送邮件)"""
        print('先get list,并返回第一个充值请求的id')
        url1=self.post_url
        header = self.header
        rt=get_list_id.GetListID()
        id=rt.test_getoneid(url1,header)
        """传入id参数，调用下一个接口"""
        url=self.post_url+'/process'+'/%s'%id
        header = self.header
        data={
            "subscribers": [
                "16955414@qq.com"
            ]
        }
        r = requests.post(url, data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,200)
        t=r.json()['data'][0]['status']
        if t==bool(1):
            print('已处理充值请求：\n%s'%r.text)
        else:
            print('充值请求处理失败：%s'%t)


    def test19_clear_settings(self):
        """调用common_settings清空充值请求列表订阅邮件列表"""
        module_id="161d77bb7e99f472f61ede6629b73ee6"
        r=common_settings.post_request(module_id)
        r.test3_clear_settings()

    def test20_recharges_clearall(self):
        """清空充值请求列表"""
        print('先get list,并返回所有充值请求的id')
        url1=self.post_url
        header = self.header
        rt=get_list_id.GetListID()
        t_list=rt.test_getallid(url1,header)
        """传入id参数，调用下一个接口"""
        print('清除所有充值请求：')
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