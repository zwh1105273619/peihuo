import unittest
from datetime import datetime
from HTMLTestRunner import HTMLTestRunner
from config import report_every,report_name,cases_path

def run_apply_data():

    path = cases_path.get('apply_data')
    dis=unittest.TestLoader()

    cases = dis.discover(path, pattern='*.py')

    now = datetime.now()
    report_file = open(
        report_every.format(report_name.get('apply_data')), 'w', encoding='utf8')
    runner_buy_count = HTMLTestRunner(
        stream=report_file,
        title=report_name.get('apply_data'),
        description='配货项目测试报告')

    runner_buy_count.run(cases)


if __name__ == '__main__':
    run_apply_data()
