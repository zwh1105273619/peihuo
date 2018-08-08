import unittest
from model.process_front import Process_Front
from db_model.peihuo_model import HistoryData
from app import db
from args import *


class Test_Tihuoshenqing_Add_Data(unittest.TestCase):
    """录入仓单提货申请界面数据核对"""

    def setUp(self):
        self.process_front = Process_Front()
        self.process_front.process_login(user_add)
        self.process_front.into_tihuoshenqing()
        self.datas = self.process_front.tihuoshenqing_check(number)

    def test_1(self):
        """循环取数据进行验证"""
        for index, data in enumerate(self.datas):
            count = db.session.query(HistoryData).filter(
                HistoryData.username == user_add,
                HistoryData.stockCode == data.get('stockcode', '未找到'),
                HistoryData.warehouse == data.get('warehouse'),
                HistoryData.goodsid == data.get('goodsid'),
                HistoryData.factoryName == data.get('factoryname'),
                HistoryData.weight == data.get('weightavlb'),
                HistoryData.material == data.get('material'),
                HistoryData.thickness == data.get('thickness'),
                HistoryData.standard_width == data.get('standard_width'),
                HistoryData.format == data.get('format'),
                HistoryData.width == data.get('width'),
                HistoryData.edge == data.get('edge'),
                HistoryData.level == data.get('level'),
                HistoryData.standard_thickness == data.get('standard_thickness'),
                HistoryData.status==0,
            ).count()
            self.assertGreater(count, 0, '第{}条数据:{}'.format(index + 1, data))

    def tearDown(self):
        self.process_front.close()


if __name__ == '__main__':
    unittest.main()
