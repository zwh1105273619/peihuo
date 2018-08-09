from model.process_front import Process_Front
import unittest
from config import user_buy_sold,user_buy_sell

class Test_Buy_Count(unittest.TestCase):
    """测试购物车购买确认后，买卖双方匹配查询界面统计"""

    def setUp(self):
        ##获得卖方匹配界面初始数据总数
        self.process_front = Process_Front()
        self.process_front.process_login(user_buy_sold)
        self.process_front.into_pipeichaxun()
        self.start_sold_number = int(self.process_front.get_table_count())
        self.process_front.quit()

        ##获得买方匹配界面初始数据总数
        self.process_front.process_login(user_buy_sell)
        self.process_front.into_pipeichaxun()
        self.start_sell_number = int(self.process_front.get_table_count())

        ##买方进行购物车应邀，记录数量
        self.process_front.fresh()
        self.process_front.into_index()
        self.shopping_number = self.process_front.shopping_cart()

        ##获得买方匹配界面最终数据总数
        self.process_front.fresh()
        self.process_front.into_pipeichaxun()
        self.end_sell_number = int(self.process_front.get_table_count())

        ##获得卖方匹配界面最终数据总数
        self.process_front.quit()
        self.process_front.process_login(user_buy_sold)
        self.process_front.into_pipeichaxun()
        self.end_sold_number = int(self.process_front.get_table_count())


    def test_1(self):
        """进行测试"""
        self.assertEqual(self.start_sell_number+self.shopping_number,self.end_sell_number,'买方数据验证,开始数据{},结束数据{}'.format(self.start_sell_number,self.end_sell_number))
        self.assertEqual(self.start_sold_number+self.shopping_number,self.end_sold_number,'卖方数据验证,开始数据{},结束数据{}'.format(self.start_sold_number,self.end_sold_number))

    def tearDown(self):
        self.process_front.close()

if __name__ == '__main__':
    unittest.main()