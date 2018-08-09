import unittest
from datetime import datetime
from HTMLTestRunner import HTMLTestRunner

from input_test.add import input_detail_304

from config import report_every,report_name,user_add,cases_path



def run_add():

    path=cases_path.get('add')

    dis=unittest.TestLoader()

    cases=dis.discover(path, pattern='*.py')

    now = datetime.now()


    report_file = open(
        report_every.format(report_name.get('add_data')), 'w', encoding='utf8')

    runner_add = HTMLTestRunner(
        stream=report_file,
        title=report_name.get('add_data'),
        description='配货项目测试报告')

    input_detail_304(user_add)

    runner_add.run(cases)


if __name__ == '__main__':
    run_add()
