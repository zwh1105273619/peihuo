import unittest
from model.process_front import Process_Front
import time
import datetime
from config import user_add


class Test_Apply_All(unittest.TestCase):
    """申请入库多条数据"""

    # username='zwh_e837'

    def setUp(self):
        self.process_front=Process_Front()
        self.process_front.process_login(user_add)

        ##获得初始数据
        self.process_front.into_rukushenqingchaxun()
        self.start_rukushenqingchaxun=self.process_front.get_table_count()
        self.process_front.fresh()
        self.process_front.into_shangpinshangjia()
        self.start_shangpinshangjia=self.process_front.get_table_count()

        ##全部入库申请
        self.process_front.fresh()
        self.process_front.into_shiwuruku()
        self.start_shiwuruku = self.process_front.get_shiwuruku_count().get('num')
        self.process_front.shiwuruku_apply()

        ##获取各个界面操作后的数据
        self.process_front.fresh()
        self.process_front.into_shiwuruku()
        self.end_shiwuruku = self.process_front.get_shiwuruku_count().get('num')
        self.process_front.fresh()
        self.process_front.into_rukushenqingchaxun()
        self.end_rukushenqingchaxun = self.process_front.get_table_count()
        self.process_front.fresh()
        self.process_front.into_shangpinshangjia()
        self.end_shangpinshangjia = self.process_front.get_table_count()

    def test_1(self):
        """各界面统计"""
        self.assertEqual(self.end_shiwuruku,0,'实物入库界面')
        self.assertEqual(int(self.start_rukushenqingchaxun)+1, int(self.end_rukushenqingchaxun),'入库申请查询界面,开始数据{},结束数据{}'.format(self.start_rukushenqingchaxun,self.end_rukushenqingchaxun))
        self.assertEqual(int(self.start_shangpinshangjia)+int(self.start_shiwuruku), int(self.end_shangpinshangjia),'商品上架界面,开始数据{},结束数据{}'.format(self.start_shangpinshangjia,self.end_shangpinshangjia))

    def tearDown(self):
        self.process_front.close()


if __name__ == '__main__':
    unittest.main()
