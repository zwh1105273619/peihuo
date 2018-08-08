from model.process_front import Process_Front
import unittest
from app import db
from db_model.peihuo_model import Fabu
from args import *


class Test_Fabulishi_Data(unittest.TestCase):
    """发布历史查询界面数据核对"""

    # username='zwh_e836'
    # number=5


    def setUp(self):
        self.process_front=Process_Front()
        self.process_front.process_login(user_fabu)
        self.process_front.into_fabulishichaxun()
        self.datas=self.process_front.fabulishichaxun_check(number)

    def test_1(self):
        """循环获得的数据进行核对"""
        for index,data in enumerate(self.datas):
            count=db.session.query(Fabu).filter(
                Fabu.username==user_fabu,
                Fabu.contract==data.get('contractid','未找到'),
                Fabu.premium==data.get('premium','未找到'),
                Fabu.stockCode==data.get('stockcode','未找到'),
                Fabu.factoryname==data.get('factoryname','未找到'),
                Fabu.weight==data.get('weight','未找到'),
                Fabu.warehouse==data.get('warehouse','未找到'),
                Fabu.material==data.get('material','未找到'),
                Fabu.thickness==data.get('thickness','未找到'),
                Fabu.standard_width==data.get('standard_width','未找到'),
                Fabu.format==data.get('format','未找到'),
                Fabu.width==data.get('width','未找到'),
                Fabu.edge==data.get('edge','未找到'),
                Fabu.level==data.get('level','未找到'),
                Fabu.standard_thickness==data.get('standard_thickness','未找到'),
                Fabu.status==0,
                Fabu.invalidTime==data.get('invalidtime'),
            ).count()
            self.assertGreater(count,0,'第{}条数据:{}'.format(index+1,data))

    def tearDown(self):
        self.process_front.close()

if __name__ == '__main__':
    unittest.main()