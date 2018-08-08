from test_cases.suit.suitecase_add import run_add
from test_cases.suit.suitecase_add_apply_all import run_add_apply_all
from test_cases.suit.suitecase_apply_all_data_confirm import run_apply_all_data
from test_cases.suit.suitecase_buy_count import run_buy_count
from test_cases.suit.suitecase_buy_data_confirm import run_buy_data
from test_cases.suit.suitecase_fabu import run_fabu
from test_cases.suit.suitecase_shenqingtihuo import run_shenqingtihuo
from test_cases.suit.suitecase_tihuoshenqingchaxun_data_confirm import run_tihuoshenqingchaxun_data

from test_cases.suit.suitecase_tihuoshenqing_data_confirm import run_tihuoshenqing_data


def run():
    run_add()  # 添加明细及相关数据验证
    run_add_apply_all()  # 申请入库
    run_apply_all_data()  # 申请入库后数据验证
    run_fabu()  # 发布及数据验证
    run_buy_count()  # 应邀以及数据统计验证
    run_buy_data()  # 应邀后数据验证
    run_tihuoshenqing_data()  # 提货申请界面数据验证
    run_shenqingtihuo()  # 申请提货
    run_tihuoshenqingchaxun_data()  # 提货申请查询界面数据验证


if __name__ == '__main__':
    run()
