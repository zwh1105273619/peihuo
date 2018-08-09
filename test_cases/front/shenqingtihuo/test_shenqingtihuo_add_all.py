import unittest
from model.process_front import Process_Front
from config import user_add


class Test_Shenqingtihuo_Add_All(unittest.TestCase):
    """录入仓单用户全选数据申请入库"""

    def setUp(self):
        self.process_front = Process_Front()
        self.process_front.process_login(user_add)

        # 获得提货申请界面表格统计数据
        self.process_front.into_tihuoshenqing()
        self.start_num_tihuoshenqing = self.process_front.get_table_count()

        # 获得提货申请查询界面表格统计统计
        self.process_front.fresh()
        self.process_front.into_tihuoshenqingchaxun()
        self.start_num_tihuoshenqingchaxun = self.process_front.get_table_count()

        # 申请一条数据入库
        self.process_front.fresh()
        self.process_front.into_tihuoshenqing()
        self.process_front.shenqingtihuo(one=False)

        # 获得提货申请界面表格统计数据
        self.process_front.fresh()
        self.process_front.into_tihuoshenqing()
        self.end_num_tihuoshenqing = self.process_front.get_table_count()

        # 获得提货申请查询界面表格统计统计
        self.process_front.fresh()
        self.process_front.into_tihuoshenqingchaxun()
        self.end_num_tihuoshenqingchaxun = self.process_front.get_table_count()

    def test_1(self):
        """两个界面数据验证"""
        if self.start_num_tihuoshenqing > 10:
            self.assertEqual(
                self.start_num_tihuoshenqing,
                self.end_num_tihuoshenqing + 10,
                '提货申请界面表格统计数据验证,初始数据:{},结束数据:{}'.format(
                    self.start_num_tihuoshenqing,
                    self.end_num_tihuoshenqing))
        else:
            self.assertEqual(
                self.end_num_tihuoshenqing,
                0,
                '提货申请界面表格统计数据验证,初始数据:{},结束数据:{}'.format(
                    self.start_num_tihuoshenqing,
                    self.end_num_tihuoshenqing))
        self.assertEqual(
            self.start_num_tihuoshenqingchaxun,
            self.end_num_tihuoshenqingchaxun - 1,
            '提货申请查询界面表格统计数据验证，初始数据:{},结束数据:{}'.format(
                self.start_num_tihuoshenqingchaxun,
                self.end_num_tihuoshenqingchaxun))

    def tearDown(self):
        self.process_front.close()


if __name__ == '__main__':
    unittest.main()
