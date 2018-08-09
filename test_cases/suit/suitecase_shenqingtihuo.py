import unittest
from datetime import datetime

from HTMLTestRunner import HTMLTestRunner

from config import report_every,report_name,cases_path

def run_shenqingtihuo():

    path = cases_path.get('shenqingtihuo')

    dis = unittest.TestLoader()
    cases = dis.discover(path, pattern='*.py')  ##从指定的目录下，以.py结尾的文件中自动去寻找测试用例





    now = datetime.now()
    report_file = open(
        report_every.format(report_name.get('shenqingtihuo')), 'w', encoding='utf8')
    runner_shenqingtihuo = HTMLTestRunner(
        stream=report_file, title=report_name.get('shenqingtihuo'), description='配货项目测试报告')

    runner_shenqingtihuo.run(cases)


if __name__ == '__main__':
    run_shenqingtihuo()
