# coding:utf-8
import requests
import json
import unittest
from common import readconfig
from common import get_token
from common import random_char
from common import get_list_id

class post_request(unittest.TestCase):
    """上传用户反馈添加图片调用七牛接口，需要手工验证（前端上传图片业务逻辑有bug）"""
    def setUp(self):
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        self.post_url = '%s%s/feedbacks'%(API,Prefix)  #feedback接口
        self.t=get_token.GetToken()
        token=self.t.test_token()
        self.header= {
        'content-type': "application/json",
        'authorization':token,
        'x-platform':"web",
        'x-module-id': "a8f3e2b3d7b38bdbb2bb13ea3508792d"
        }
    def test01_feedbacks_create(self):
        """添加用户建议反馈：纯文本"""
        url=self.post_url
        header = self.header
        self.random=random_char.RandomChar()
        text=self.random.random_char([],10,2)   # 生成10位长度混合字符串
        qq=self.random.random_char([],10,1)   # 生成10位长度数字
        data={
            "text": "用户建议%s"%text,
            "type": 0,     # 0=建议，1=问题，2=其它
            "contact": "%s@qq.com"%qq,
            "origin": "PC"
        }
        r = requests.post(url, data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,201)
        if r.json()['total']==1:
            print('成功添加用户建议反馈id：%s'%r.json()['data'][0]['id'])
        else:
            print('添加错误数据')

    def test02_feedbacks_create(self):
        """添加用户问题反馈：纯文本"""
        url=self.post_url
        header = self.header
        self.random=random_char.RandomChar()
        text=self.random.random_char([],10,2)   # 生成10位长度混合字符串
        qq=self.random.random_char([],10,1)   # 生成10位长度数字
        data={
            "text": "用户问题%s"%text,
            "type": 1,     # 0=建议，1=问题，2=其它
            "contact": "%s@qq.com"%qq,
            "origin": "PC"
        }
        r = requests.post(url, data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,201)
        if r.json()['total']==1:
            print('成功添加用户问题反馈id：%s'%r.json()['data'][0]['id'])
        else:
            print('添加错误数据')

    def test03_feedbacks_create(self):
        """添加用户其它反馈：纯文本"""
        url=self.post_url
        header = self.header
        self.random=random_char.RandomChar()
        text=self.random.random_char([],10,2)   # 生成10位长度混合字符串
        qq=self.random.random_char([],10,1)   # 生成10位长度数字
        data={
            "text": "用户其它反馈%s"%text,
            "type": 2,     # 0=建议，1=问题，2=其它
            "contact": "%s@qq.com"%qq,
            "origin": "PC"
        }
        r = requests.post(url, data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,201)
        if r.json()['total']==1:
            print('成功添加用户其它反馈id：%s'%r.json()['data'][0]['id'])
        else:
            print('添加错误数据')

    def test04_feedbacks_create(self):
        """添加反馈内容含有换行，空格等多字符组成"""
        url=self.post_url
        header = self.header
        self.random=random_char.RandomChar()
        qq=self.random.random_char([],10,1)   # 生成10位长度数字
        data={
            "text": """  空格4个字符    然后换行
-------换行-------------------------------
添加多种字符~！@#￥%……&*（）——+、】【‘;/.,
再添加字符`1!@#$%^&*()_+\][{}|';:"/.,<>?
123456789""",
            "type": 2,     # 0=建议，1=问题，2=其它
            "contact": "%s@qq.com"%qq,
            "origin": "PC"
        }
        r = requests.post(url, data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,201)
        if r.json()['total']==1:
            print('成功添加用户其它反馈id：%s'%r.json()['data'][0]['id'])
        else:
            print('添加错误数据')

    def test05_feedbacks_create(self):
        """添加反馈内容正好500字符(此限制只在前端，后端无字数限制)"""
        url=self.post_url
        header = self.header
        self.random=random_char.RandomChar()
        qq=self.random.random_char([],10,1)   # 生成10位长度数字
        data={
            "text": """明还合小该点下见照组字小组按、随按、与个与与模的出还可与用串串定说工该提数提位机该用工出个指数出度小
长数。个串式要点度明符生各说字数。用种字度模式、的应个种个指用应小成具可串机符数该数点数常数常生下机
定数出的求整数长位位的见指成应提随出可定的符整的指数工。常生用指定随机具提数说点位、小个说各见可按个
定数随字位长与明符可具工生与按随长度明要符围字模可说字围定生随数机给随指可随字位还整位随围数说合个、
该还长生。的可说可见用字成与提可了明数合各模位还与方各的的符机成可具成还与户具可范说提数点度还的户数
照说生随符说指、还范机、机的明字。方还用机照数定的点生种机生户户数可小。数提可模、的具字出种长成个度
的成符种用成明户数符数用按见出应模模说、小工指数符可字小户字提符生提给生范度数的数合指度给。位等成按
等组该随数长数具定出数说要应符数字围种还式整机定定围见的随、、字出等下还随位数见种工随要数可出定户指
要的种用生具生还。的的求位与该工指度模随字还符，可生小该与常数组字数定的各定还。给户还机数符字的数机
等。符数具工了符式位各、各指、整数的长、组数数指常生数与成数位组范点可求机说下定符说点成按数围数字照""",
            "type": 2,     # 0=建议，1=问题，2=其它
            "contact": "%s@qq.com"%qq,
            "origin": "PC"
        }
        r = requests.post(url, data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,201)
        if r.json()['total']==1:
            print('成功添加用户其它反馈id：%s'%r.json()['data'][0]['id'])
        else:
            print('添加错误数据')

    def test06_feedbacks_getlist(self):
        """获取用户反馈列表。"""
        url=self.post_url
        header = self.header
        r = requests.get(url,headers=header)
        self.assertEqual(r.status_code,200)
        print('用户反馈列表：\n%s'%r.text)

    def test07_sortlist_type(self):
        """用户反馈列表type：类型 列升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"type"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('用户反馈列表“类型”列升序排序：%s'%r.text)

    def test08_sortlist_type(self):
        """用户反馈列表type：类型 列降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-type"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('用户反馈列表“类型”列降序排序：%s'%r.text)

    def test09_sortlist_type(self):
        """用户反馈列表status：状态 列升序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"status"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('用户反馈列表“状态”列升序排序：%s'%r.text)

    def test10_sortlist_type(self):
        """用户反馈列表status：状态 列降序排序"""
        url=self.post_url
        payload = {'page[offset]': '0', 'page[limit]': '5','addition':'{"sort":"-status"}'}
        header = self.header
        r = requests.get(url,params=payload,headers=header)
        self.assertEqual(r.status_code,200)
        print('用户反馈列表“状态”列降序排序：%s'%r.text)

    def test11_feedbacks_getone(self):
        """查找某一个反馈"""
        print('先获得某一个反馈的id.')
        url1=self.post_url
        header = self.header
        rt=get_list_id.GetListID()
        id=rt.test_getoneid(url1,header)
        url=self.post_url+'/%s'%id
        r = requests.get(url,headers=header)
        self.assertEqual(r.status_code,200)
        print('查看id: %s 的用户反馈：\n%s'%(id,r.text))

    def test12_feedbacks_update(self):
        """更新某一个反馈为已处理状态"""
        print('先获得某一个反馈的id.')
        url1=self.post_url
        header = self.header
        rt=get_list_id.GetListID()
        id=rt.test_getoneid(url1,header)
        url=self.post_url+'/%s'%id
        data={
            "status": bool(1)
        }
        r = requests.patch(url, data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,201)
        print('id: %s 的处理状态已更新：\n%s'%(id,r.text))

    def test13_post_settings(self):
        """配置用户反馈列表订阅邮件列表"""
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
        'x-module-id': "a8f3e2b3d7b38bdbb2bb13ea3508792d"
        }
        data={
            "content": [
            "16955414@qq.com",
            "leen0910@gmail.com"
            ]
        }
        r = requests.post(url,data=json.dumps(data),headers=header)
        self.assertEqual(r.status_code,201)
        print('上传2个邮箱订阅成功：\n%s'%r.text)

    def test14_get_settings(self):
        """获取用户反馈列表订阅邮件列表"""
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
        'x-module-id': "a8f3e2b3d7b38bdbb2bb13ea3508792d"
        }
        r = requests.get(url,headers=header)
        self.assertEqual(r.status_code,200)
        print('用户反馈的邮箱订阅列表：\n%s'%r.json()['data'][0]['content'])

    def test15_feedbacks_process(self):
        """处理用户反馈(发送邮件)"""
        print('先get list,并返回第一个下载请求的id')
        url1=self.post_url
        header = self.header
        rt=get_list_id.GetListID()
        id=rt.test_getoneid(url1,header)
        """传入id参数，调用下一个接口"""
        url=self.post_url+'/process'+'/%s'%id
        header = self.header
        data={
            "subscribers": [
                "leen0910@gmail.com",
                "16955414@qq.com"
            ]
        }
        r = requests.post(url, data=json.dumps(data), headers=header)
        self.assertEqual(r.status_code,200)
        print('已处理下载申请：\n%s'%r.text)

    def test16_clear_settings(self):
        """清空用户反馈列表订阅邮件列表"""
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
        'x-module-id': "a8f3e2b3d7b38bdbb2bb13ea3508792d"
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

    def test17_feedbacks_clearall(self):
        """清空用户反馈列表"""
        print('先get list,并返回所有用户反馈的id')
        url1=self.post_url
        header = self.header
        rt=get_list_id.GetListID()
        t_list=rt.test_getallid(url1,header)
        """传入id参数，调用下一个接口"""
        print('清除所有用户反馈：')
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