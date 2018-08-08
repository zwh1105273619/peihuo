from HTMLTestRunner import HTMLTestRunner
from datetime import datetime
import unittest
from test_cases.tihuoguanli.test_tihuoshenqing_add_data_confirm import Test_Tihuoshenqing_Add_Data


def run_tihuoshenqing_data():
    load_1 = unittest.TestLoader().loadTestsFromTestCase(Test_Tihuoshenqing_Add_Data)

    suite = unittest.TestSuite()

    suite.addTest(load_1)

    now = datetime.now()
    report_file = open(
        r'F:\autotest\peihuo\file\report\tihuoshenqing_data\report{}.html'.format(
            now.strftime('%Y%m%d%H%M%S')), 'w', encoding='utf8')
    runner_tihuoshenqing_data = HTMLTestRunner(
        stream=report_file, title='提货申请界面数据验证', description='配货项目测试报告')

    runner_tihuoshenqing_data.run(suite)


if __name__ == '__main__':
    run_tihuoshenqing_data()
