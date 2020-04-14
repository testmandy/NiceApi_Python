# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 14:03
# @Author  : mandy
import unittest
import HTMLTestRunner

from testcases.system_lib import SystemLib

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(SystemLib('test_systemLib_search'))
    suite.addTest(SystemLib('test_question_pageList'))
    fr = open('res.html', 'wb')
    report = HTMLTestRunner.HTMLTestRunner(stream=fr, title='测试报告', description='测试报告详情')
    report.run(suite)