import unittest
from datetime import datetime
from HTMLTestRunner import HTMLTestRunner
from config import report_every,report_name,cases_path

def run_tihuoshenqingchaxun_data():
    path = cases_path.get('tihuoshenqingchaxun_data')
    dis = unittest.TestLoader()
    cases = dis.discover(path, pattern='*.py')



    now = datetime.now()
    report_file = open(
        report_every.format(report_name.get('tihuoshenqingchaxun_data')), 'w', encoding='utf8')
    runner_tihuoshenqing_data = HTMLTestRunner(
        stream=report_file,
        title=report_name.get('tihuoshenqingchaxun_data'),
        description='配货项目测试报告')
    runner_tihuoshenqing_data.run(cases)


if __name__ == '__main__':
    run_tihuoshenqingchaxun_data()
