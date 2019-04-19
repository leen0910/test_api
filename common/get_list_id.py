import requests
import unittest

class GetListID(unittest.TestCase):
    def test_getoneid(self,url,header):
        """获取列表第一个id"""
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        n=r.json()['total']
        if n!=0:
           t=r.json()['data'][0]['id']
        else:
            t=''
            print('列表为空')
        print("列表第一个返回的id:%s "%t)
        return t

    def test_getallid(self,url,header):
        """获取列表所有id集合"""
        r = requests.get(url, headers=header)
        self.assertEqual(r.status_code,200)
        n=r.json()['total']
        t=[]
        if n!=0:
           for index in range(0,n):
                t.append(r.json()['data'][index]['id'])
        else:
            t=''
            print('列表为空')
        print("返回列表所有的id:%s "%t)
        return t

    def tearDown(self):
        pass

if __name__ == "__main__":
    t=GetListID()
