# coding:utf-8
import requests
import json
from common import readconfig
from common import get_token



class post_request():

    def __init__(self,module_id):
        self.rt=readconfig.ReadConfig()
        API=self.rt.get_api()
        Prefix=self.rt.get_prefix()
        self.post_url = '%s%s/settings'%(API,Prefix)  #settings接口
        self.t=get_token.GetToken()
        token=self.t.test_token()
        self.header= {
        'content-type': "application/json",
        'authorization':token,
        'x-platform':"web",
        'x-module-id': "%s"%module_id
        }


    def test1_post_settings(self,email1,email2):
        """配置module的订阅邮件列表"""
        url = self.post_url
        header=self.header
        data={
            "content": [
            email1,
            email2
            ]
        }
        r = requests.post(url,data=json.dumps(data),headers=header)
        print('module_id: %s上传2个邮箱订阅成功：\n%s'%(module_id, r.text))

    def test2_get_settings(self):
        """获取module订阅邮件列表"""
        url = self.post_url
        header=self.header
        r = requests.get(url,headers=header)
        print('module_id: %s邮箱订阅列表：\n%s'%(module_id,r.json()['data'][0]['content']))

    def test3_clear_settings(self):
        """清空module订阅邮件列表"""
        url = self.post_url
        header=self.header
        data={
            "content": [

            ]
        }
        r = requests.post(url,data=json.dumps(data),headers=header)
        if r.json()['data'][0]['content']==[]:
            print('module_id: %s已清空邮箱订阅。'%module_id)
        else:
            print('module_id: %s邮箱订阅未清空：%s'%(module_id,r.json()['data'][0]['content']))


    def tearDown(self):
        pass

if __name__ == "__main__":
    module_id="a8f3e2b3d7b38bdbb2bb13ea3508792d"
    email1="16951414@qq.com"
    email2="leen0910@sina.com"
    r=post_request(module_id)
    r.test1_post_settings(email1,email2)
    r.test2_get_settings()
    r.test3_clear_settings()
