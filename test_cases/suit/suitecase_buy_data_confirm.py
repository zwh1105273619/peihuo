from HTMLTestRunner import HTMLTestRunner
from datetime import datetime
import unittest
from test_cases.buy_data.test_sell_data_confirm import Test_Sell_Data
from test_cases.buy_data.test_sold_data_confirm import Test_Sold_Data


def run_buy_data():
    load_1 = unittest.TestLoader().loadTestsFromTestCase(Test_Sell_Data)
    load_2 = unittest.TestLoader().loadTestsFromTestCase(Test_Sold_Data)

    suite = unittest.TestSuite()

    suite.addTest(load_1)
    suite.addTest(load_2)

    now = datetime.now()

    report_file = open(
        r'F:\autotest\peihuo\file\report\buy_data\report{}.html'.format(
            now.strftime('%Y%m%d%H%M%S')), 'w', encoding='utf8')
    runner_buy_count = HTMLTestRunner(
        stream=report_file,
        title='应邀数据验证',
        description='配货项目测试报告')

    runner_buy_count.run(suite)


if __name__ == '__main__':
    run_buy_data()
