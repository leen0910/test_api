# coding:utf-8
import requests
import unittest


class SearchList(unittest.TestCase):
    def search(self,url,header,key):
        """搜索列表，结果按每页5个返回第一页"""
        payload = {'page[offset]': '0', 'page[limit]': '5','search':key}
        r = requests.get(url, params=payload, headers=header)
        print(r.text)
        # self.assertEqual(r.status_code,200)
        if r.json()['total']!=0:
            print('搜索：%s 返回结果为：\n%s'%(key,r.text))
        else:
            print('搜索结果为空！')

if __name__ == '__main__':
    unittest.main()
#     url="https://test.robot-qixing.com:1014/v0/recharges"
#     header= {
#             'content-type': "application/json",
#             'authorization':"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVjNzVlZTY2ZDY1ODJhMDAwNThlNDY0YiIsInV1aWQiOiIyNTUwODE0MS0xYmZjLTQ5NmYtYTc2Yi04MDI0MWE0ZjUwOGQiLCJpc3MiOiJIWlFYLVJvYm90In0.38fxzet3Lbneo7TMDeW37vpSShUn_Nbn6txHewzSBiM"
# ,
#             'x-platform':"web",
#             'x-module-id': "161d77bb7e99f472f61ede6629b73ee6"
#         }
#     key="zhz"
#     SearchList().search(url,header,key)