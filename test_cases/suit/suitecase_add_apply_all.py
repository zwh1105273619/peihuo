from HTMLTestRunner import HTMLTestRunner
from datetime import datetime
import unittest
from test_cases.add.test_shenqingruku_all import Test_Apply_All


def run_add_apply_all():

    load_1 = unittest.TestLoader().loadTestsFromTestCase(Test_Apply_All)

    suite = unittest.TestSuite()

    suite.addTest(load_1)

    now = datetime.now()
    report_file = open(
        r'F:\autotest\peihuo\file\report\add_apply_all\report{}.html'.format(
            now.strftime('%Y%m%d%H%M%S')), 'w', encoding='utf8')
    runner_buy_count = HTMLTestRunner(
        stream=report_file,
        title='全部申请入库',
        description='配货项目测试报告')

    runner_buy_count.run(suite)


if __name__ == '__main__':
    run_add_apply_all()
