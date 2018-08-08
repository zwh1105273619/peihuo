import unittest
from model.process_front import Process_Front
from model.untils import read_data
from app import db
from db_model.peihuo_model import HistoryData
import random
from args import *

class Test_Detail_Data(unittest.TestCase):
    """验证实物入库的数据是否与输入的一致"""

    # username='zwh_e835'
    # data_number=3


    def setUp(self):
        self.process_front=Process_Front()
        self.process_front.process_login(user_add)
        self.process_front.into_shiwuruku()
        self.datas =self.process_front.get_shiwuruku_alldata(number)

    def test_1(self):
        """测试录入的数据是否在数据库中"""
        for index,data in enumerate(self.datas):
            count=db.session.query(HistoryData).filter(HistoryData.username==user_add,
                                                 HistoryData.goodsid==data.get('goodsid','未找到'),
                                                 HistoryData.stockCode==data.get('stockcode','未找到'),
                                                 HistoryData.factoryName==data.get('factoryname','未找到'),
                                                 HistoryData.weight==data.get('weight','未找到'),
                                                 HistoryData.remark==data.get('remark','未找到'),
                                                 HistoryData.material==data.get('material','未找到'),
                                                 HistoryData.thickness==data.get('thickness','未找到'),
                                                 HistoryData.standard_width==data.get('standard_width','未找到'),
                                                 HistoryData.format==data.get('format','未找到'),
                                                 HistoryData.width==data.get('width','未找到'),
                                                 HistoryData.edge==data.get('edge','未找到'),
                                                 HistoryData.level==data.get('level','未找到'),
                                                 HistoryData.standard_thickness==data.get('standard_thickness','未找到'),
                                                 HistoryData.warehouse==data.get('warehouse','未找到'),
                                                 HistoryData.status==0).count()
            self.assertGreater(count,0,'第{}条数据:{}'.format(index+1,data))

    def tearDown(self):
        self.process_front.close()


if __name__ == '__main__':
    unittest.main()