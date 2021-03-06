# coding=utf-8
import unittest
import HTMLTestRunner
import time
from common import readconfig
#测试api版本号
rt=readconfig.ReadConfig()
prefix=rt.get_prefix()
api_v=prefix.replace('/','')
# 相对路径
test_dir ='./test_case'
test_dir1 ='./report'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
# 定义带有当前测试时间的报告
now = time.strftime("%Y-%m-%d %H_%M_%S")
filename = test_dir1 + '/' + now + 'result.html'
# 二进制打开，准备写入文件
fp = open(filename, 'wb')
# 定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'API: %s 接口自动化测试报告'%api_v, description=u'用例执行情况')
runner.run(discover)