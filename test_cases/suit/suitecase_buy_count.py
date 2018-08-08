from HTMLTestRunner import HTMLTestRunner
from datetime import datetime
import unittest
from test_cases.buy_count.test_buy_count import Test_Buy_Count


def run_buy_count():
    load_1 = unittest.TestLoader().loadTestsFromTestCase(Test_Buy_Count)

    suite = unittest.TestSuite()

    suite.addTest(load_1)

    now = datetime.now()
    report_file = open(
        r'F:\autotest\peihuo\file\report\buy_count\report{}.html'.format(
            now.strftime('%Y%m%d%H%M%S')), 'w', encoding='utf8')
    runner_buy_count = HTMLTestRunner(
        stream=report_file,
        title='应邀数量验证',
        description='配货项目测试报告')

    runner_buy_count.run(suite)


if __name__ == '__main__':
    run_buy_count()
