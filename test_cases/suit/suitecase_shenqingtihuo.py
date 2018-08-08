from HTMLTestRunner import HTMLTestRunner
from datetime import datetime
import unittest
from test_cases.tihuoguanli.test_shenqingtihuo_add_one import Test_Shenqingtihuo_Add_one
from test_cases.tihuoguanli.test_shenqingtihuo_add_all import Test_Shenqingtihuo_Add_All


def run_shenqingtihuo():
    load_1 = unittest.TestLoader().loadTestsFromTestCase(Test_Shenqingtihuo_Add_one)
    load_2 = unittest.TestLoader().loadTestsFromTestCase(Test_Shenqingtihuo_Add_All)

    suite = unittest.TestSuite()

    suite.addTest(load_1)
    suite.addTest(load_2)

    now = datetime.now()
    report_file = open(
        r'F:\autotest\peihuo\file\report\shenqingtihuo\report{}.html'.format(
            now.strftime('%Y%m%d%H%M%S')), 'w', encoding='utf8')
    runner_shenqingtihuo = HTMLTestRunner(
        stream=report_file, title='申请提货', description='配货项目测试报告')

    runner_shenqingtihuo.run(suite)


if __name__ == '__main__':
    run_shenqingtihuo()
