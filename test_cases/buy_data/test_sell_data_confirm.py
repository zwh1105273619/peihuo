from model.process_front import Process_Front
import unittest
from app import db
from db_model.peihuo_model import Fabu
from args import *


class Test_Sell_Data(unittest.TestCase):
    """匹配查询界面买方数据核对"""
    # username='zwh_e836'
    # number=5

    def setUp(self):
        self.process_front=Process_Front()
        self.process_front.process_login(user_buy_sell)
        self.process_front.into_pipeichaxun()
        self.datas=self.process_front.pipei_check(number)

    def test_1(self):
        """循环对数据进行验证"""
        for index,data in enumerate(self.datas):
            count=db.session.query(Fabu).filter(
                Fabu.username == user_buy_sold,
                Fabu.goodsid==data.get('goodsid','未找到'),
                Fabu.contract==data.get('contractid','未找到'),
                Fabu.weight==data.get('weightmatch','未找到'),
                Fabu.premium==data.get('premium','未找到'),
                Fabu.stockCode==data.get('stockcode','未找到'),
                Fabu.factoryname==data.get('factoryname','未找到'),
                Fabu.material==data.get('material','未找到'),
                Fabu.thickness==data.get('thickness','未找到'),
                Fabu.standard_width==data.get('standard_width','未找到'),
                Fabu.format==data.get('format','未找到'),
                Fabu.width==data.get('width','未找到'),
                Fabu.edge==data.get('edge','未找到'),
                Fabu.level==data.get('level','未找到'),
                Fabu.standard_thickness==data.get('standard_thickness','未找到'),
                Fabu.warehouse==data.get('warehouse','未找到'),
                Fabu.status==0,
            ).count()
            self.assertGreater(count,0,'第{}条数据:{}'.format(index+1,data))

    def tearDown(self):
        self.process_front.close()


if __name__ == '__main__':
    unittest.main()