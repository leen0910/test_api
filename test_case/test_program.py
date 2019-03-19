# coding:utf-8
import requests
import json
import unittest
import readconfig
import get_token
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

    def test_createprogram_ok(self):
        """成功上传程序文件"""
        self.rt=readconfig.ReadConfig()
        account=self.rt.get_account()
        url=self.post_url
        header = self.header
        n=random.randint(0,255*255*255)
        data={
          "name": "程序%s"%n,
          "author": "%s"%account,
          "size": 100,
          "data": "{\"type\":\"set\",\"fname\":\"1\",\"fdata\":{\"robot\":{\"label\":\"路点1\",\"name\":\"pos\",\"id\":\"fbd9e511-4174-46bd-8ae5-04ae4d2ce46a\",\"data\":{\"x\":400,\"y\":0,\"z\":0,\"rx\":0,\"coordinate\":\"world\"},\"breakpoint\":false,\"comment\":\"\",\"children\":[],\"isValid\":false},\"ref\":[]}}",
          "version":"V1.4.1",
          "types":"四轴-1",
          "machine":"qs-1",
          "model":"QR-400.1"
        }
         #正确的程序数据
        #将data序列化为json格式数据，传递给data参数
        r = requests.post(url, data=json.dumps(data), headers=header)
        print(r.text)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()