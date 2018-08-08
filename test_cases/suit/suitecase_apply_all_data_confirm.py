from HTMLTestRunner import HTMLTestRunner
from datetime import datetime
import unittest
from test_cases.add.test_rukushenqingchaxun_data_confirm import Test_Rukushenqingchaxun_Data
from test_cases.fabu.test_shangpinshangjia_data_confirm import Test_Shangpin_Data
from test_cases.fabu.test_kucunchaxun_data_confirm import Test_Kucunchaxun_Data


def run_apply_all_data():

    load_1 = unittest.TestLoader().loadTestsFromTestCase(Test_Rukushenqingchaxun_Data)
    load_2 = unittest.TestLoader().loadTestsFromTestCase(Test_Shangpin_Data)
    load_3 = unittest.TestLoader().loadTestsFromTestCase(Test_Kucunchaxun_Data)

    suite = unittest.TestSuite()

    suite.addTest(load_1)
    suite.addTest(load_2)

    now = datetime.now()
    report_file = open(
        r'F:\autotest\peihuo\file\report\apply_all_data\report{}.html'.format(
            now.strftime('%Y%m%d%H%M%S')), 'w', encoding='utf8')
    runner_buy_count = HTMLTestRunner(
        stream=report_file,
        title='全部申请入库后数据验证',
        description='配货项目测试报告')

    runner_buy_count.run(suite)


if __name__ == '__main__':
    run_apply_all_data()
