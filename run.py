import unittest

from data_test.HTMLTestRunnerNew import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("test_case", pattern="test*.py")

file_path = 'report\\test_result.html'
with open(file_path, 'wb')as f:
    HTMLTestRunner(stream=f, title='报告', description='下单接口报告', tester='Bomz').run(suite)


