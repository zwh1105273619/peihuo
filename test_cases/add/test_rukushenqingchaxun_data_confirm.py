import unittest
from model.process_front import Process_Front
from app import db
from db_model.peihuo_model import HistoryData
from args import *


class Test_Rukushenqingchaxun_Data(unittest.TestCase):
    """"入库申请查询界面数据核对"""
    ##cal_weight
    ##count_weight
    ##data_detail
    # username='zwh_e835'
    # number=1

    def setUp(self):
        self.process_front=Process_Front()
        self.process_front.process_login(user_add)
        self.process_front.into_rukushenqingchaxun()
        self.datas=self.process_front.rukushengqingchaxun_check(number)

    def test_1(self):
        """随机选择数据进行核对"""
        for index,data in enumerate(self.datas):
            self.assertEqual(data.get('cal_weight'),data.get('count_weight'),'第{}次重量核对不正确,计算重量{}.界面重量{}'.format(index+1,data.get('cal_weight'),data.get('count_weight')))

            for detail in data.get('data_detail'):

                count = db.session.query(HistoryData).filter(HistoryData.username == user_add,
                                                            HistoryData.goodsid == detail.get('goodsid','未找到'),
                                                            HistoryData.stockCode == detail.get('stockcode','未找到'),
                                                            HistoryData.factoryName == detail.get('factoryname','未找到'),
                                                            HistoryData.weight == detail.get('weight','未找到'),
                                                            HistoryData.material == detail.get('material','未找到'),
                                                            HistoryData.thickness == detail.get('thickness','未找到'),
                                                            HistoryData.standard_width == detail.get('standard_width','未找到'),
                                                            HistoryData.format == detail.get('format','未找到'),
                                                            HistoryData.width == detail.get('width','未找到'),
                                                            HistoryData.edge == detail.get('edge','未找到'),
                                                            HistoryData.level == detail.get('level','未找到'),
                                                            HistoryData.standard_thickness ==detail.get('standard_thickness','未找到'),
                                                            HistoryData.warehouse == detail.get('warehouse','未找到'),
                                                            HistoryData.status==0,
                                                            ).count()
                self.assertGreater(count, 0, '第{}条数据:{}'.format(index+1,detail))


    def tearDown(self):
        self.process_front.close()

if __name__ == '__main__':
    unittest.main()





