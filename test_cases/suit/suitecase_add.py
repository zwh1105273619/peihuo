from HTMLTestRunner import HTMLTestRunner
from datetime import datetime
import unittest
import os
from input_test.deatail_add import *
from test_cases.add.test_shenqingruku_all import Test_Apply_All
from test_cases.add.test_shenqingruku_one import Test_Apply_One
from test_cases.add.test_detail_add_data_confirm import Test_Detail_Data
from test_cases.add.test_rukushenqingchaxun_data_confirm import Test_Rukushenqingchaxun_Data
from args import *


def run_add():

    load_2 = unittest.TestLoader().loadTestsFromTestCase(Test_Apply_One)
    load_3 = unittest.TestLoader().loadTestsFromTestCase(Test_Detail_Data)

    suite = unittest.TestSuite()

    suite.addTest(load_2)
    suite.addTest(load_3)

    now = datetime.datetime.now()
    report_file = open(
        r'F:\autotest\peihuo\file\report\add\report{}.html'.format(
            now.strftime('%Y%m%d%H%M%S')), 'w', encoding='utf8')
    runner_add = HTMLTestRunner(
        stream=report_file,
        title='录入明细相关',
        description='配货项目测试报告')

    input_detail_304(user_add)

    runner_add.run(suite)


if __name__ == '__main__':
    run_add()
