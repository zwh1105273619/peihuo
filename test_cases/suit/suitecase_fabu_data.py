import unittest
from datetime import datetime



from HTMLTestRunner import HTMLTestRunner
from config import report_every,report_name,user_fabu,cases_path
from input_test.fabu import fabu_304



def run_fabu():
    path = cases_path.get('fabu')
    dis = unittest.TestLoader()
    cases = dis.discover(path, pattern='*.py')

    now = datetime.now()
    report_file = open(
        report_every.format(report_name.get('fabu_data')), 'w', encoding='utf8')
    runner_add = HTMLTestRunner(
        stream=report_file,
        title=report_name.get('fabu_data'),
        description='配货项目测试报告')

    fabu_304(user_fabu)

    runner_add.run(cases)


if __name__ == '__main__':
    run_fabu()
