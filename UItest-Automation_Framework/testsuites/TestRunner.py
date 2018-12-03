# coding = utf-8
import HTMLTestRunner
import os
import time
import unittest

from testsuites.test_ehr_loggin import EhrLoggin

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
# 获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
# 设置报告名称格式
HtmlFile = report_path + now + 'HTMLtemplate.html'
fp = open(HtmlFile, "wb")
#
# unittest下addTest()方法来加载测试用例到测试套件中去
suite = unittest.TestSuite()
suite.addTest(EhrLoggin('test_07_normal_login'))

# makeSuite()方法，一次性加载一个类文件下所有测试用例到suite中去
# suite = unittest.TestSuite(unittest.makeSuite(EhrBirthday))

# discover（）方法去加载一个路径下所有的测试用例
#
# suite = unittest.TestLoader().discover("testsuites")

if __name__ == '__main__':
    # 执行用例
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="EHR项目测试报告", description="用例测试情况")
    runner.run(suite)
