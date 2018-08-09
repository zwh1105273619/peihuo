from test_cases.suit.suitecase_add_data import run_add
from test_cases.suit.suitecase_apply import run_apply
from test_cases.suit.suitecase_apply_data_confirm import run_apply_data
from test_cases.suit.suitecase_buy_count import run_buy_count
from test_cases.suit.suitecase_buy_data_confirm import run_buy_data
from test_cases.suit.suitecase_fabu_data import run_fabu
from test_cases.suit.suitecase_shenqingtihuo import run_shenqingtihuo
from test_cases.suit.suitecase_tihuoshenqingchaxun_data_confirm import run_tihuoshenqingchaxun_data
from test_cases.suit.suitecase_tihuoshenqing_data_confirm import run_tihuoshenqing_data
from clear.clear_file import clear


def run():
    run_add()  # 添加明细及相关数据验证
    run_apply()  # 申请入库
    run_apply_data()  # 申请入库后数据验证
    run_fabu()  # 发布及数据验证
    run_buy_count()  # 应邀以及数据统计验证
    run_buy_data()  # 应邀后数据验证
    run_tihuoshenqing_data()  # 提货申请界面数据验证
    run_shenqingtihuo()  # 申请提货
    run_tihuoshenqingchaxun_data()  # 提货申请查询界面数据验证


if __name__ == '__main__':
    ##移动everyreport中的文件再开始跑脚本
    clear('everyreport')
    run()
