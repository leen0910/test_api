import requests
import unittest
from common import readconfig
from common import get_token




class get_request(unittest.TestCase):
    """上传文件是七牛的第三方接口，暂时不支持自动化，并且前前端调用有逻辑问题，需要手工验证"""
    def setUp(self):
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        self.post_url = '%s%s/startpages'%(API,Prefix)  # startpages接口
        self.t=get_token.GetToken()
        token=self.t.test_token()
        self.header= {
        'content-type': "application/json",
        'authorization':token,
        'x-platform':"web",
        'x-module-id': "53640a1502e2819fa3cb5d6d796f866c"
        }

    def test01_get_startpages(self):
        """获取启动页列表--Get List"""
        url=self.post_url
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        print('获取启动页文件')
        return r

    def test02_startpages_firstID(self):
        """获取启动页列表第一个图片id"""
        r=self.test01_get_startpages()
        if r.json()['total']!=0:
            t=r.json()['data'][0]['id']
        else:
            t=''
            print('启动页图片为空')
        print("get:第一张启动页的id:%s "%t)
        return t

    def test03_newestimages(self):
        """获取最新启动页"""
        url=self.post_url+'/newest-images'
        header = self.header
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        print(r.text)

    # def test04_dele_startpages(self):
    #     """删除第一个启动页"""
    #     r=self.test01_get_startpages()
    #     if r.json()['total']:
    #         print('删除第一张启动页')
    #         t=self.test02_startpages_firstID()
    #         url=self.post_url+'/%s'%t
    #         header = self.header
    #         r = requests.delete(url, headers=header)
    #     else:
    #         print('启动页为空，无文件删除')


    def test05_startpages_allID(self):
        """获取启动页列表所有图片id"""
        r=self.test01_get_startpages()
        n=r.json()['total']
        if n!=0:
            t=[]
            for index in range(0,n):
                t.append(r.json()['data'][index]['id'])
        else:
            t=''
            print('启动页图片为空')
        print("get所有启动页的id:%s "%t)
        return t

    def test06_dele_startpages(self):
        """删除所有启动页"""
        r=self.test01_get_startpages()
        if r.json()['total']:
            print('删除所有启动页')
            t_list=self.test05_startpages_allID()
            for t in t_list:
                url=self.post_url+'/%s'%t
                header = self.header
                r = requests.delete(url, headers=header)
                print('删除启动页id：%s'%t)
        else:
            print('启动页为空，无文件删除')

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()