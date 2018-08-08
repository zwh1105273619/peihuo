from HTMLTestRunner import HTMLTestRunner
from datetime import datetime
import unittest
from input_test.fabu import *
from test_cases.fabu.test_fabu_data_confirm import Test_Fabu_Data
from test_cases.fabu.test_fabulishi_data_confirm import Test_Fabulishi_Data
from test_cases.fabu.test_index_data_confirm import Test_Index_Data
from args import *


def run_fabu():
    load_3 = unittest.TestLoader().loadTestsFromTestCase(Test_Fabu_Data)
    load_4 = unittest.TestLoader().loadTestsFromTestCase(Test_Fabulishi_Data)
    load_5 = unittest.TestLoader().loadTestsFromTestCase(Test_Index_Data)

    suite = unittest.TestSuite()

    suite.addTest(load_3)
    suite.addTest(load_4)
    suite.addTest(load_5)

    now = datetime.datetime.now()
    report_file = open(
        r'F:\autotest\peihuo\file\report\fabu\report{}.html'.format(
            now.strftime('%Y%m%d%H%M%S')), 'w', encoding='utf8')
    runner_add = HTMLTestRunner(
        stream=report_file,
        title='发布相关',
        description='配货项目测试报告')

    fabu_304(user_fabu)

    runner_add.run(suite)


if __name__ == '__main__':
    run_fabu()
