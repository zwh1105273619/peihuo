import unittest
from model.process_front import Process_Front
from args import *


class Test_Apply_One(unittest.TestCase):
    """申请入库一条数据"""
    # username='zwh_e838'

    def setUp(self):
        self.process_front=Process_Front()
        self.process_front.process_login(user_shenqingruku_one)

        ##获得初始数据
        self.process_front.into_shiwuruku()
        self.start_shiwuruku=self.process_front.get_shiwuruku_count().get('num')
        self.process_front.into_rukushenqingchaxun()
        self.start_rukushenqingchaxun=self.process_front.get_table_count()
        self.process_front.fresh()
        self.process_front.into_shangpinshangjia()
        self.start_shangpinshangjia=self.process_front.get_table_count()

        ##添加明细并且进行入库申请
        self.process_front.into_shiwuruku()
        self.process_front.ruku_add_detail()
        self.process_front.fresh()
        self.process_front.into_shiwuruku()
        self.process_front.shiwuruku_apply(all=False)

        ##获取各个界面操作后的数据
        self.process_front.into_shiwuruku()
        self.end_shiwuruku = self.process_front.get_shiwuruku_count().get('num')
        self.process_front.into_rukushenqingchaxun()
        self.end_rukushenqingchaxun = self.process_front.get_table_count()
        self.process_front.fresh()
        self.process_front.into_shangpinshangjia()
        self.end_shangpinshangjia = self.process_front.get_table_count()

    def test_1(self):
        """各界面统计"""
        self.assertEqual(int(self.start_shiwuruku),int(self.end_shiwuruku),'实物入库界面')
        self.assertEqual(int(self.start_rukushenqingchaxun)+1, int(self.end_rukushenqingchaxun),'入库申请查询界面,开始数据{},结束数据{}'.format(self.start_rukushenqingchaxun,self.end_rukushenqingchaxun))
        self.assertEqual(int(self.start_shangpinshangjia)+1, int(self.end_shangpinshangjia),'商品上架界面,开始数据{},结束数据{}'.format(self.start_shangpinshangjia,self.end_shangpinshangjia))

    def tearDown(self):
        self.process_front.close()


if __name__ == '__main__':
    unittest.main()
