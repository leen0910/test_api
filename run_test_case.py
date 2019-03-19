# coding=utf-8
import unittest
import HTMLTestRunner
import time
# 相对路径
test_dir ='./test_case'
test_dir1 ='./report'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
# 定义带有当前测试时间的报告，防止前一次报告被覆盖
now = time.strftime("%Y-%m-%d %H_%M_%S")
filename = test_dir1 + '/' + now + 'result.html'
# 二进制打开，准备写入文件
fp = open(filename, 'wb')
# 定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况')
runner.run(discover)