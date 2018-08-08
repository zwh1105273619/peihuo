from object import Page
from selenium.webdriver.common.by import By
import datetime
import time
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
import re
import random


class Process_Front(Page):

    # 表格定位器
    locator_table_count = (
        By.XPATH,
        '//div[@id="pagination"]/span[@class="total_detail"]')
    locator_pageSelect = (By.XPATH, '//div[@id="pagination"]/span[1]/select')
    locator_table_all = (By.ID, 'bottomSelectAll')
    locator_table_first = (
        By.XPATH,
        '//div[@id="table_set"]/tbody/tr[1]/td[1]/input')

    # 导航定位器
    locator_menu_title = (
        By.XPATH,
        '//div[@class="menu_content"]/div[@class="title_line menu_content_title"]')

    # 登陆界面定位器
    locator_username = (By.ID, 'mobile')
    locator_pwd = (By.ID, 'login_pwd')
    locator_check_code = (By.ID, 'check_code')
    locator_btn = (By.ID, 'login_btn_a')

    # 首页定位器
    locator_info = (By.CLASS_NAME, 'login_user_info')
    locator_beihai = (By.PARTIAL_LINK_TEXT, '北海诚德')
    locator_index_304 = (
        By.XPATH,
        '//div[@id="category_container"]/ul/li[1]/a')
    locator_index_201 = (
        By.XPATH,
        '//div[@id="category_container"]/ul/li[2]/a')
    locator_buy_now = (By.ID, 'buy_now')
    locator_add_cart = (By.ID, 'add_cart')
    locator_index_first = (
        By.XPATH,
        '//table[@id="table_set"]/tbody/tr[1]/td[1]/input')
    locator_quit = (By.XPATH, '//*[@id="top_bar"]/div/div[1]/a')
    locator_btn_pipei = (By.XPATH, '//div[@class="buttons"]/button[2]')
    locator_buy_count = (By.CLASS_NAME, 'f_float_r')
    locator_cartCount = (By.ID, 'cartCount')
    locator_shopCartNum = (By.ID, 'shopCartNum')
    locator_selectedNum = (By.ID, 'selectedNum')
    locator_bottomSelectAll = (By.ID, 'bottomSelectAll')

    # 菜单栏定位器
    locator_rukushengqing = (By.ID, 'side_menu_node_a_1')
    locator_shiwuruku = (By.ID, 'side_menu_node_a_2')
    locator_rukushengqing_query = (By.ID, 'side_menu_node_a_3')
    locator_kucunguanli = (By.ID, 'side_menu_node_4')
    locator_kucunchaxun = (By.ID, 'side_menu_node_a_5')
    locator_kucunlishichaxun = (By.ID, 'side_menu_node_a_6')
    locator_shangjiafabu = (By.ID, 'side_menu_node_7')
    locator_shangpinshangjia = (By.ID, 'side_menu_node_a_8')
    locator_fabu = (By.ID, 'side_menu_node_a_9')
    locator_fabulishi = (By.ID, 'side_menu_node_a_10')
    locator_pipeichaxun = (By.ID, 'side_menu_node_a_11')
    locator_tihuoguanli = (By.ID, 'side_menu_node_a_12')
    locator_tihuoshenqing = (By.ID, 'side_menu_node_a_13')
    locator_tihuoshenqingchaxun = (By.ID, 'side_menu_node_a_14')
    locator_tihuodanchaxun = (By.ID, 'side_menu_node_a_15')

    # 实物入库界面定位器
    locator_goodsId = (By.ID, 'goodsId')
    locator_tableAddBtn = (By.ID, 'tableAddBtn')
    # locator_delete
    locator_delete = (
        By.XPATH,
        '//*[@id="2"]/div/div[2]/div[1]/div[1]/div[2]/button')
    locator_tableEditBtn = (By.ID, 'tableEditBtn')
    locator_applyBtn = (By.ID, 'applyBtn')
    locator_exportBtn = (By.ID, 'exportBtn')
    locator_importBtn = (By.ID, 'importBtn')
    locator_shiwuruku_count_text = (By.CLASS_NAME, 'f_float_r')

    # 添加修改明细界面定位器
    locator_stockCode = (By.ID, 'stockCode')
    locator_factoryName = (By.ID, 'factoryName')
    locator_weight = (By.ID, 'weight')
    locator_1 = (By.ID, '1')
    locator_2 = (By.NAME, '冷轧304标准厚度')
    locator_3 = (By.ID, '3')
    locator_4 = (By.ID, '4')
    locator_5 = (By.ID, '5')
    locator_6 = (By.ID, '6')
    locator_7 = (By.ID, '7')
    locator_8 = (By.ID, '8')
    locator_warehouseName = (By.ID, 'warehouseName')
    locator_stockRemark = (By.ID, 'stockRemark')
    locator_add_detail_btn_yes = (
        By.XPATH, '/html/body/div[2]/div/div/div[2]/div[3]/button[1]')
    locator_add_detail_btn_cancel = (
        By.XPATH, '/html/body/div[2]/div/div/div[2]/div[3]/button[2]')

    # 删除明细二级界面定位器
    locator_shiwuruku_del_yes = (
        By.XPATH, '//div[@class="jconfirm-box"]/div[@class="buttons"]/button[1]')
    locator_shiwuruku_del_cancel = (
        By.XPATH, '//div[@class="jconfirm-box"]/div[@class="buttons"]/button[2]')

    # 申请入库二级界面定位器
    locator_shenqingruku_textarea = (
        By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[3]/div/div/textarea')
    locator_shenqingruku_yes = (
        By.XPATH, '//div[@class="jconfirm-box"]/div[@class="buttons"]/button[1]')
    locator_shenqingruku_cancel = (
        By.XPATH, '//div[@class="jconfirm-box"]/div[@class="buttons"]/button[2]')
    locator_shenqingruku_confirm = (
        By.XPATH, '//div[@class="jconfirm-box"]/div[@class="buttons"]/button')

    # 入库申请查询界面定位器
    locator_stockType = (By.ID, 'stockType')
    locator_status = (By.ID, 'status')
    locator_applyStartDate = (By.NAME, 'applyStartDate')
    locator_applyEndDate = (By.NAME, 'applyEndDate')
    locator_searchBtn = (By.ID, 'searchBtn')
    locator_resetBtn = (By.ID, 'resetBtn')

    # 匹配查询定位器
    locator_pipei_first = (
        By.XPATH,
        '//table[@id="table_set"]/tbody/tr[1]/td[1]/i')
    locator_pipei_add_more_div = (By.CLASS_NAME, 'add_more_div')

    # 商品上架界面定位器
    locator_shangjia_issueBtn = (By.ID, 'issueBtn')
    locator_shangjia_lotGroundBtn = (By.ID, 'lotGroundBtn')
    locator_shangjia_exportIssueBtn = (By.ID, 'exportIssueBtn')

    # 商品上架界面发布二级明细定位器
    locator_shangjia_contract = (By.ID, 'contract')
    locator_shangjia_invaliDate = (By.ID, 'invaliDate')
    locator_shangjia_premium = (By.ID, 'premium')
    locator_invateOneTime = (By.ID, 'invateOneTime')
    locator_shangjia_yes = (By.ID, 'public_details')
    locator_shangjia_cancel = (
        By.XPATH, '//*[@id="do_issue_detail_modal"]/div/div/div[3]/button[2]')

    # 发布界面定位器
    locator_modifyPremium = (By.ID, 'locator_modifyPremium')
    locator_batchAddition = (By.ID, 'batchAddition')
    locator_batchReduction = (By.ID, 'batchReduction')
    locator_cancelBtn = (By.ID, 'cancelBtn')
    locator_ghostCancelBtn = (By.ID, 'ghostCancelBtn')

    # 提货申请界面定位器
    locator_shenqingtihuo = (
        By.XPATH,
        '//div[@class="table_btn"]/div[@class="f_float_l"]/div/button')
    locator_tihuoshenqing_yes = (
        By.XPATH, '//div[@class="panel_btn"]/button[1]')
    locator_tihuoshenqing_all = (By.CLASS_NAME, 'selectAll')
    locator_tihuoshenqing_first = (
        By.XPATH, '//div[@id="table_set"]/tbody/tr[1]/td[1]/input')

    def login(self, username=None, password='1', check_code='1234'):
        """登录"""

        # 登录定位器
        locator_wrong_info = (
            By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[3]/div')

        self.open_url('http://192.168.1.43:8083/login')
        self.find_element_type(username, self.locator_username)
        self.find_element_type(password, self.locator_pwd)
        self.find_element_type(check_code, self.locator_check_code)
        self.find_element_click(self.locator_btn)

        # 判断登陆用户名密码是否正确，再去找对应的界面元素
        if username.strip() == 'zwh_e800' and password == '1':
            self.find_element(self.locator_info)
        else:
            self.find_element(locator_wrong_info)

        url = self.get_url()
        return url

    def process_login(self, username=None):
        """流程使用登录"""
        self.open_url('http://192.168.1.43:8083/login')
        self.find_element_type(username, self.locator_username)
        self.find_element_type('1', self.locator_pwd)
        self.find_element_type('1234', self.locator_check_code)
        self.find_element_click(self.locator_btn)
        self.find_element(self.locator_info)

    def quit(self):
        """退出登录"""
        self.find_element_click(self.locator_quit)

    def into_index(self):
        """进入首页"""
        self.open_url('http://192.168.1.43:8083/web/html/index.html')

    def into_shiwuruku(self):
        """进入实物入库界面"""
        self.open_url('http://192.168.1.43:8083/web/html/my_distribution.html')
        self.find_element_click(self.locator_rukushengqing)
        time.sleep(0.5)
        self.find_element_click(self.locator_shiwuruku)
        time.sleep(0.5)
        text = self.get_text(self.locator_menu_title)
        return text

    def into_rukushenqingchaxun(self):
        """进入入库申请查询相关界面"""
        self.open_url('http://192.168.1.43:8083/web/html/my_distribution.html')
        time.sleep(0.5)
        self.find_element_click(self.locator_rukushengqing)
        time.sleep(0.5)
        self.find_element_click(self.locator_rukushengqing_query)
        text = self.get_text(self.locator_menu_title)
        return text

    def into_shangpinshangjia(self):
        """进入商品上架界面"""
        self.open_url('http://192.168.1.43:8083/web/html/my_distribution.html')
        self.find_element_click(self.locator_shangjiafabu)
        time.sleep(0.5)
        self.find_element_click(self.locator_shangpinshangjia)
        time.sleep(0.5)
        text = self.get_text(self.locator_menu_title)
        return text

    def into_fabu(self):
        """进入发布界面"""
        self.open_url('http://192.168.1.43:8083/web/html/my_distribution.html')
        time.sleep(0.5)
        self.find_element_click(self.locator_shangjiafabu)
        time.sleep(0.5)
        self.find_element_click(self.locator_fabu)
        text = self.get_text(self.locator_menu_title)
        return text

    def into_fabulishichaxun(self):
        """进入发布历史查询界面"""
        self.open_url('http://192.168.1.43:8083/web/html/my_distribution.html')
        time.sleep(0.5)
        self.find_element_click(self.locator_shangjiafabu)
        time.sleep(0.5)
        self.find_element_click(self.locator_fabulishi)
        text = self.get_text(self.locator_menu_title)
        return text

    def into_kucunchaxun(self):
        """进入库存查询界面"""
        self.open_url('http://192.168.1.43:8083/web/html/my_distribution.html')
        time.sleep(0.5)
        self.find_element_click(self.locator_kucunguanli)
        time.sleep(0.5)
        self.find_element_click(self.locator_kucunchaxun)
        text = self.get_text(self.locator_menu_title)
        return text

    def into_kucunlishichaxun(self):
        """进入库存历史查询"""
        self.open_url('http://192.168.1.43:8083/web/html/my_distribution.html')
        time.sleep(0.5)
        self.find_element_click(self.locator_kucunguanli)
        time.sleep(0.5)
        self.find_element_click(self.locator_kucunlishichaxun)
        text = self.get_text(self.locator_menu_title)
        return text

    def into_pipeichaxun(self):
        """进入匹配查询界面"""
        self.open_url('http://192.168.1.43:8083/web/html/my_distribution.html')
        time.sleep(0.5)
        text = self.get_text(self.locator_menu_title)
        return text

    def into_tihuoshenqing(self):
        """进入提货申请界面"""
        self.open_url('http://192.168.1.43:8083/web/html/my_distribution.html')
        time.sleep(0.5)
        self.find_element_click(self.locator_tihuoguanli)
        time.sleep(0.5)
        self.find_element_click(self.locator_tihuoshenqing)
        text = self.get_text(self.locator_menu_title)
        return text

    def into_tihuoshenqingchaxun(self):
        """进入提货申请查询界面"""
        self.open_url('http://192.168.1.43:8083/web/html/my_distribution.html')
        time.sleep(0.5)
        self.find_element_click(self.locator_tihuoguanli)
        time.sleep(0.5)
        self.find_element_click(self.locator_tihuoshenqingchaxun)
        text = self.get_text(self.locator_menu_title)
        return text

    def into_tihuodanchaxun(self):
        """进入提货单查询界面"""
        self.open_url('http://192.168.1.43:8083/web/html/my_distribution.html')
        self.find_element_click(self.locator_tihuoguanli)
        time.sleep(0.5)
        self.find_element_click(self.locator_tihuodanchaxun)
        time.sleep(0.5)
        text = self.get_text(self.locator_menu_title)
        return text

    def get_table_count(self):
        """获得所有表格下方的统计数据总和"""
        try:
            text = self.get_text(self.locator_table_count)
            pattern = re.compile('\d+')
            count = pattern.findall(text)[0]
        except TimeoutException:
            count = 0
        return int(count)

    def change_table_data(self, text):
        """修改表格每页显示多少条"""
        self.select_by_text(text, self.locator_pageSelect)

    def get_table_trs(self):
        """获取表格所有的列"""
        html = self.get_html()
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', attrs={'id': 'table_set'})
        tbody = table.find('tbody')
        trs = tbody.find_all('tr')
        return trs

    def index_check(self, number=1, kind=304):
        """首页查询"""

        if kind == 304:
            self.find_element_click(self.locator_index_304)
        elif kind == 201:
            self.find_element_click(self.locator_index_201)
        try:
            self.change_table_data('100')
        except TimeoutException:
            return '首页无数据'

        time.sleep(2)
        count = int(self.get_table_count())
        number = count if number > count else number

        trs = self.get_table_trs()

        datas = []

        for index in range(number):
            tr = trs[0]
            if tr:
                if kind == 304:
                    data = {
                        'goodsid': tr.find('td', attrs={'name': 'goodsName'}).text,
                        'contract': tr.find('td', attrs={'name': 'contractId'}).text,
                        'factoryname': tr.find('td', attrs={'name': 'factoryName'}).text,
                        'weightleft': tr.find('td', attrs={'name': 'weightLeft'}).text,
                        'material': tr.find('td', attrs={'id': '1'}).text,
                        'thickness': tr.find('td', attrs={'id': '2'}).text.split('*')[0],
                        'standard_width': tr.find('td', attrs={'id': '2'}).text.split('*')[1],
                        'format': tr.find('td', attrs={'id': '4'}).text,
                        'width': tr.find('td', attrs={'id': '5'}).text,
                        'edge': tr.find('td', attrs={'id': '6'}).text,
                        'level': tr.find('td', attrs={'id': '7'}).text,
                        'standard_thickness': tr.find('td', attrs={'id': '8'}).text,
                        'warehouse': tr.find('td', attrs={'name': 'warehouseName'}).text,
                        'stockremark': tr.find('td', attrs={'name': 'stockRemark'}).attrs.get('remark'),
                        'premium': str(int(float(tr.find('td', attrs={'name': 'premium'}).text) * 1000)),
                        'refprice': tr.find('td', attrs={'name': 'refPrice'}).text,
                    }
                else:
                    data = {
                        'goodsid': tr.find('td', attrs={'name': 'goodsName'}).text,
                        'contract': tr.find('td', attrs={'name': 'contractId'}).text,
                        'factoryname': tr.find('td', attrs={'name': 'factoryName'}).text,
                        'weightleft': tr.find('td', attrs={'name': 'weightLeft'}).text,
                        'material': tr.find('td', attrs={'id': '9'}).text,
                        'thickness': tr.find('td', attrs={'id': '10'}).text,
                        'standard_width': tr.find('td', attrs={'id': '11'}).text,
                        'format': tr.find('td', attrs={'id': '12'}).text,
                        'width': tr.find('td', attrs={'id': '13'}).text,
                        'edge': tr.find('td', attrs={'id': '14'}).text,
                        'level': tr.find('td', attrs={'id': '15'}).text,
                        'standard_thickness': tr.find('td', attrs={'id': '16'}).text,
                        'warehouse': tr.find('td', attrs={'name': 'warehouseName'}).text,
                        'stockremark': tr.find('td', attrs={'name': 'stockRemark'}).attrs.get('remark'),
                        'premium': tr.find('td', attrs={'name': 'premium'}).text,
                        'refprice': tr.find('td', attrs={'name': 'refPrice'}).text,
                    }
            datas.append(data)
        print(datas)
        return datas

    def get_shiwuruku_count(self, kind='冷轧304卷'):
        # 获得实物入库界面统计数字
        self.select_by_text(kind, self.locator_goodsId)
        try:

            text = self.get_text(self.locator_shiwuruku_count_text)
            pattern = re.compile('\d+')
            count = pattern.findall(text)
            # print({'num':int(count[0]),'weight':int(count[1])})
            return {'num': int(count[0]), 'weight': int(count[1])}

        except TimeoutException:

            return {'num': 0, 'weight': 0}

    def ruku_add_detail(
            self,
            stockCode=datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
            factoryName='福建宏旺',
            weight='10',
            stockRemark='测试',
            material='304/2B',
            standard_thickness='0.3',
            standard_width='1000',
            standard='2B',
            actual_width='1.0',
            edge='毛边',
            level='一级',
            thickness='2.0',
            warehouseName='无锡浦新硕放库'):
        """添加明细"""

        # 实物入库相关定位器
        locator_error_btn = (
            By.XPATH,
            '/html/body/div[4]/div[2]/div/div/div/div/div[4]/button')
        locator_text = (
            By.XPATH,
            '//div[@class="jconfirm-box"]/div[@class="content-pane"]/div')

        # 依次点击进入实物入库tab，将商品切换至冷轧304并点击添加弹出二级框
        # self.find_element_click(self.locator_rukushengqing)
        # self.find_element_click(self.locator_shiwuruku)
        self.select_by_text('冷轧304卷', self.locator_goodsId)
        self.find_element_click(self.locator_tableAddBtn)

        # 填写明细信息并提交
        self.find_element_type(stockCode, self.locator_stockCode)  # 钢卷号
        self.select_by_text(factoryName, self.locator_factoryName)  # 厂家
        self.find_element_type(weight, self.locator_weight)  # 重量
        self.select_by_text(material, self.locator_1)  # 材质

        ele = self.find_elements_id('2')[1]
        self.select_by_text_ele(thickness, ele)  # 厚度

        self.select_by_text(standard_width, self.locator_3)  # 宽度
        self.find_element_type(standard, self.locator_4)  # 规格
        self.find_element_type(actual_width, self.locator_5)  # 实宽
        self.select_by_text(edge, self.locator_6)  # 边部
        self.select_by_text(level, self.locator_7)  # 等级
        self.find_element_type(standard_thickness, self.locator_8)  # 参厚
        self.select_by_text(warehouseName, self.locator_warehouseName)  # 仓库
        self.find_element_type(stockRemark, self.locator_stockRemark)  # 备注
        self.find_element_click(self.locator_add_detail_btn_yes)

        # 抓取操作后的提示文字
        try:
            text = self.get_text(locator_text)
        except TimeoutException:
            text = '无提示信息'

        return text

    def get_shiwuruku_alldata(self, number=1, kind='冷轧304卷'):
        """获得实物入库界面前几条数据"""

        locator_first = (
            By.XPATH,
            '//*[@id="table_set"]/tbody/tr[1]/td[1]/input')

        self.select_by_text(kind, self.locator_goodsId)
        self.find_element(self.locator_shiwuruku_count_text)
        time.sleep(5)

        count = int(self.get_shiwuruku_count().get('num'))
        number = count if number > count else number

        trs = self.get_table_trs()
        data = []
        for index in range(1, number + 1):
            tr = trs[index - 1]
            data_detail = {
                'goodsid': kind,
                'stockcode': tr.find('td', attrs={'name': 'stockCode'}).text,
                'factoryname': tr.find('td', attrs={'name': 'factoryName'}).text,
                'weight': tr.find('td', attrs={'name': 'weight'}).text,
                'remark': tr.find('td', attrs={'name': 'stockRemark'}).attrs.get('remark'),
                'material': tr.find('td', attrs={'name': re.compile('冷轧\d+材质/表面')}).text,
                'thickness': tr.find('td', attrs={'name': re.compile('冷轧\d+标准厚度')}).text,
                'standard_width': tr.find('td', attrs={'name': re.compile('冷轧\d+标准宽度')}).text,
                'format': tr.find('td', attrs={'name': re.compile('冷轧\d+标签规格')}).text,
                'width': tr.find('td', attrs={'name': re.compile('冷轧\d+实宽')}).text,
                'edge': tr.find('td', attrs={'name': re.compile('冷轧\d+边部')}).text,
                'level': tr.find('td', attrs={'name': re.compile('冷轧\d+等级')}).text,
                'standard_thickness': tr.find('td', attrs={'name': re.compile('冷轧\d+参厚')}).text,
                'warehouse': tr.find('td', attrs={'name': 'warehouseName'}).text,
            }

            data.append(data_detail)
        print(data)
        return data

    def shiwuruku_del(self, kind='冷轧304卷', all=True):
        """实物入库删除"""
        locator_all = (
            By.XPATH,
            '//*[@id="table_set"]/thead/tr/th[1]/label/input_test')
        locator_one = (
            By.XPATH,
            '//*[@id="table_set"]/tbody/tr[1]/td[1]/input_test')

        self.select_by_text(kind, self.locator_goodsId)
        self.find_element(locator_one)
        if all:
            self.find_element_click(locator_all)
        else:
            self.find_element_click(locator_one)
        self.find_element_click(self.locator_delete)
        self.find_element_click(self.locator_shiwuruku_del_yes)

    def shiwuruku_apply(self, kind='冷轧304卷', all=True):
        """实物入库申请入库"""
        locator_all = (
            By.XPATH,
            '//*[@id="table_set"]/thead/tr/th[1]/label/input')
        locator_one = (
            By.XPATH,
            '//*[@id="table_set"]/tbody/tr[1]/td[1]/input')
        locator_text = (
            By.XPATH,
            '//div[@class="jconfirm-box"]/div[@class="content-pane"]/div')

        self.select_by_text(kind, self.locator_goodsId)
        self.find_element(locator_one)
        if all:
            self.find_element_click(locator_all)
        else:
            self.find_element_click(locator_one)
        self.find_element_click(self.locator_applyBtn)
        self.find_element_click(self.locator_shenqingruku_yes)

        try:
            text = self.get_text(locator_text)
        except TimeoutException:
            text = '无提示信息'

        self.find_element_click(self.locator_shenqingruku_confirm)
        print(text)
        return text

    def rukushengqingchaxun_check(self, number=1, kind='冷轧304卷'):
        """入库申请查询查看对应数据"""

        self.select_by_text(kind, self.locator_goodsId)

        self.change_table_data('100')

        count = int(self.get_table_count())

        # 如果数据总数大于100，在100中取；如果随机数大于总数据，取总数居
        count = 100 if count > 100 else count
        number = count if number > count else number

        trs = self.get_table_trs()

        datas = []
        # 列表从上往下取数据
        for index in range(number):
            tr = trs[index]
            if tr:
                count_weight = int(
                    tr.find(
                        'td', attrs={
                            'name': 'weightTotal'}).text)
                goodsid = tr.find('td', attrs={'name': 'goodsName'}).text

            # 点击+号
            js = 'document.getElementsByClassName("plus_get_more")[{}].click()'.format(
                index)
            time.sleep(2)
            self.run_js(js)
            time.sleep(5)

            # 获得内层数据
            html = self.get_html()
            soup = BeautifulSoup(html, 'html.parser')
            tr_in = soup.find('tr', attrs={'class': 'add_more_tr'})
            tbody_in = tr_in.find('tbody')
            trs_in = tbody_in.find_all('tr')
            cal_weight = 0
            data = []
            for t in trs_in:
                # 获得子列表中的数据，以及计算总重
                cal_weight += int(t.find('td', attrs={'name': 'weight'}).text)

                data_detail = {
                    'goodsid': goodsid,
                    'stockcode': t.find('td', attrs={'name': 'stockCode'}).text,
                    'factoryname': t.find('td', attrs={'name': 'factoryName'}).text,
                    'weight': t.find('td', attrs={'name': 'weight'}).text,
                    'material': t.find('td', attrs={'name': '冷轧304材质/表面'}).text,
                    'thickness': t.find('td', attrs={'name': '冷轧304标准厚度'}).text,
                    'standard_width': t.find('td', attrs={'name': '冷轧304标准宽度'}).text,
                    'format': t.find('td', attrs={'name': '冷轧304标签规格'}).text,
                    'width': t.find('td', attrs={'name': '冷轧304实宽'}).text,
                    'edge': t.find('td', attrs={'name': '冷轧304边部'}).text,
                    'level': t.find('td', attrs={'name': '冷轧304等级'}).text,
                    'standard_thickness': t.find('td', attrs={'name': '冷轧304参厚'}).text,
                    'warehouse': t.find('td', attrs={'name': 'warehouseName'}).text,
                    'status': t.find('td', attrs={'name': 'status'}).text,
                    'remark': t.find('td', attrs={'name': 'stockRemark'}).attrs.get('remark')
                }
                data.append(data_detail)

            datas.append({'cal_weight': cal_weight,
                          'count_weight': count_weight,
                          'data_detail': data})
            self.fresh()
            self.into_rukushenqingchaxun()
            self.select_by_text(kind, self.locator_goodsId)
            self.change_table_data('100')
        print(datas)
        return datas

    def kucunchaxun_check(self, number=1, kind='冷轧304卷'):
        """库存查询界面数据核对"""
        self.select_by_text(kind, self.locator_goodsId)
        time.sleep(5)
        self.change_table_data('100')

        count = int(self.get_table_count())

        number = count if number > count else number

        time.sleep(3)

        trs = self.get_table_trs()

        data = []
        for index in range(1, number + 1):
            tr = trs[index - 1]
            data_detail = {
                'goodsid': tr.find('td', attrs={'name': 'goodsName'}).text,
                'frzStatus': tr.find('td', attrs={'name': 'frzStatus'}).text,
                'stockcode': tr.find('td', attrs={'name': 'stockCode'}).text,
                'factoryname': tr.find('td', attrs={'name': 'factoryName'}).text,
                'weight': tr.find('td', attrs={'name': 'weightTotal'}).text,
                'weightfrz': tr.find('td', attrs={'name': 'weightFrz'}).text,
                'weightavlb': tr.find('td', attrs={'name': 'weightAvlb'}).text,
                'stocksource': tr.find('td', attrs={'name': 'stockSource'}).text,
                'applytime': tr.find('td', attrs={'name': 'applyTime'}).text,
                'warehouse': tr.find('td', attrs={'name': 'warehouseName'}).text,
                'stockyype': tr.find('td', attrs={'name': 'stockType'}).text,
                'stockid': tr.find('td', attrs={'name': 'stockId'}).text,
                'material': tr.find('td', attrs={'name': '1'}).text,
                'thickness': tr.find('td', attrs={'name': '2'}).text,
                'standard_width': tr.find('td', attrs={'name': '3'}).text,
                'format': tr.find('td', attrs={'name': '4'}).text,
                'width': tr.find('td', attrs={'name': '5'}).text,
                'edge': tr.find('td', attrs={'name': '6'}).text,
                'level': tr.find('td', attrs={'name': '7'}).text,
                'standard_thickness': tr.find('td', attrs={'name': '8'}).text,
                'remark': tr.find('td', attrs={'name': 'stockRemark'}).attrs.get('remark'),
            }
            data.append(data_detail)
        print(data)
        return data

    def shangpinshangjia_check(self, number=1, kind='冷轧304卷'):
        """商品上架界面数据核对"""

        # 选择冷卷品种
        self.select_by_text(kind, self.locator_goodsId)
        time.sleep(5)
        self.change_table_data('100')

        count = int(self.get_table_count())
        number = count if number > count else number

        time.sleep(5)
        trs = self.get_table_trs()
        data = []
        for index in range(1, number + 1):
            tr = trs[index - 1]
            if tr:
                if kind == '冷轧304卷':
                    data_detail = {
                        'goodsid': tr.find('td', attrs={'name': 'goodsName'}).text,
                        'stockcode': tr.find('td', attrs={'name': 'stockCode'}).text,
                        'factoryname': tr.find('td', attrs={'name': 'factoryName'}).text,
                        'weight': tr.find('td', attrs={'name': 'weightAvlb'}).text,
                        'warehouse': tr.find('td', attrs={'name': 'warehouseName'}).text,
                        'stockyype': tr.find('td', attrs={'name': 'stockType'}).text,
                        'applyid': tr.find('td', attrs={'name': 'applyId'}).text,
                        'stockid': tr.find('td', attrs={'name': 'stockId'}).text,
                        'material': tr.find('td', attrs={'name': '1'}).text,
                        'thickness': tr.find('td', attrs={'name': '2'}).text,
                        'standard_width': tr.find('td', attrs={'name': '3'}).text,
                        'format': tr.find('td', attrs={'name': '4'}).text,
                        'width': tr.find('td', attrs={'name': '5'}).text,
                        'edge': tr.find('td', attrs={'name': '6'}).text,
                        'level': tr.find('td', attrs={'name': '7'}).text,
                        'standard_thickness': tr.find('td', attrs={'name': '8'}).text,
                    }
                else:
                    data_detail = {
                        'goodsid': tr.find('td', attrs={'name': 'goodsName'}).text,
                        'stockcode': tr.find('td', attrs={'name': 'stockCode'}).text,
                        'factoryname': tr.find('td', attrs={'name': 'factoryName'}).text,
                        'weight': tr.find('td', attrs={'name': 'weightAvlb'}).text,
                        'warehouse': tr.find('td', attrs={'name': 'warehouseName'}).text,
                        'stockyype': tr.find('td', attrs={'name': 'stockType'}).text,
                        'applyid': tr.find('td', attrs={'name': 'applyId'}).text,
                        'stockid': tr.find('td', attrs={'name': 'stockId'}).text,
                        'material': tr.find('td', attrs={'name': '9'}).text,
                        'thickness': tr.find('td', attrs={'name': '10'}).text,
                        'standard_width': tr.find('td', attrs={'name': '11'}).text,
                        'format': tr.find('td', attrs={'name': '12'}).text,
                        'width': tr.find('td', attrs={'name': '13'}).text,
                        'edge': tr.find('td', attrs={'name': '14'}).text,
                        'level': tr.find('td', attrs={'name': '15'}).text,
                        'standard_thickness': tr.find('td', attrs={'name': '16'}).text,
                    }

            data.append(data_detail)
        print(data)
        return data

    def fabu(
            self,
            premium,
            contract='CR304',
            date_valid=True,
            all=False,
            invateOneTime=False):
        """发布上架"""

        # 定位器
        locator_first = (
            By.XPATH,
            '//*[@id="table_set"]/tbody/tr[1]/td[1]/input')
        locator_all = (
            By.XPATH,
            '//*[@id="table_set"]/thead/tr/th[1]/label/input_test')
        locator_select_day = (
            By.XPATH, '/html/body/div[4]/div[1]/table/tbody/tr[1]/td[1]')

        locator_text_1 = (
            By.XPATH,
            '/html/body/div[2]/div[2]/div/div/div/div/div[3]/div')
        locator_text_2 = (
            By.XPATH,
            '/html/body/div[4]/div[2]/div/div/div/div/div[3]/div')  # 合约编码

        # 判断是发布一条还是全部
        if not all:
            self.find_element_click(locator_first)
        else:
            self.find_element_click(locator_all)
        self.find_element_click(self.locator_shangjia_issueBtn)

        # 输入升贴水
        self.find_element_type(premium, self.locator_shangjia_premium)

        # 选择有效日期，默认是当天，否则选择过期日期
        if not date_valid:
            self.find_element_click(self.locator_shangjia_invaliDate)
            self.find_element_click(locator_select_day)

        # 选择合约
        self.select_by_text(contract, self.locator_shangjia_contract)

        # 是否一次性应邀
        if invateOneTime is True:
            self.find_element_click(self.locator_invateOneTime)

        self.find_element_click(self.locator_shangjia_yes)
        # 获取提示文本
        try:
            text = self.get_text(locator_text_1)
        except TimeoutException:
            text = self.get_text(locator_text_2)
        return text

    def fabu_check(self, number=1, kind='冷轧304卷'):
        """发布界面数据核对"""

        # 选择商品
        self.select_by_text(kind, self.locator_goodsId)
        time.sleep(5)

        # 若无数据，返回None
        try:
            self.change_table_data('100')
        except TimeoutException:
            return None

        count = int(self.get_table_count())
        number = count if number > count else number

        time.sleep(5)
        trs = self.get_table_trs()
        data = []
        for index in range(1, number + 1):
            tr = trs[index - 1]
            if tr:
                if kind == '冷轧304卷':
                    data_detail = {
                        'goodsid': tr.find('td', attrs={'name': 'goodsName'}).text,
                        'contractid': tr.find('td', attrs={'name': 'contractId'}).text,
                        'premium': str(int(float(tr.find('td', attrs={'name': 'premium'}).text.replace(',', '').replace('￥', '')) * 1000)),
                        'stockcode': tr.find('td', attrs={'name': 'stockCode'}).text,
                        'factoryname': tr.find('td', attrs={'name': 'factoryName'}).text,
                        'weight': tr.find('td', attrs={'name': 'weight'}).text,
                        'weightleft': tr.find('td', attrs={'name': 'weightLeft'}).text,
                        'matchtotalqtt': tr.find('td', attrs={'name': 'matchTotalQtt'}).text,
                        'warehouse': tr.find('td', attrs={'name': 'warehouseName'}).text,
                        'stockid': tr.find('td', attrs={'name': 'stockId'}).text,
                        'material': tr.find('td', attrs={'name': '1'}).text,
                        'thickness': tr.find('td', attrs={'name': '2'}).text,
                        'standard_width': tr.find('td', attrs={'name': '3'}).text,
                        'format': tr.find('td', attrs={'name': '4'}).text,
                        'width': tr.find('td', attrs={'name': '5'}).text,
                        'edge': tr.find('td', attrs={'name': '6'}).text,
                        'level': tr.find('td', attrs={'name': '7'}).text,
                        'standard_thickness': tr.find('td', attrs={'name': '8'}).text,
                        'tradetype': tr.find('td', attrs={'name': 'tradeType'}).text,
                        'issueid': tr.find('td', attrs={'name': 'issueId'}).text,
                        'status': tr.find('td', attrs={'name': 'status'}).text,
                        'remark': tr.find('td', attrs={'class': 'remark'}).attrs.get('remark'),
                        'issuetime': tr.find('td', attrs={'name': 'issueTime'}).text,
                        'canceltime': tr.find('td', attrs={'name': 'cancelTime'}).text,
                        'invalidtime': tr.find('td', attrs={'name': 'invalidTime'}).text,
                    }
                else:
                    data_detail = {
                        'goodsid': tr.find('td', attrs={'name': 'goodsName'}).text,
                        'contractid': tr.find('td', attrs={'name': 'contractId'}).text,
                        'premium': tr.find('td', attrs={'name': 'premium'}).text,
                        'stockcode': tr.find('td', attrs={'name': 'stockCode'}).text,
                        'factoryname': tr.find('td', attrs={'name': 'factoryName'}).text,
                        'weight': tr.find('td', attrs={'name': 'weight'}).text,
                        'weightleft': tr.find('td', attrs={'name': 'weightLeft'}).text,
                        'matchtotalqtt': tr.find('td', attrs={'name': 'matchTotalQtt'}).text,
                        'warehouse': tr.find('td', attrs={'name': 'warehouseName'}).text,
                        'stockid': tr.find('td', attrs={'name': 'stockId'}).text,
                        'material': tr.find('td', attrs={'name': '9'}).text,
                        'thickness': tr.find('td', attrs={'name': '10'}).text,
                        'standard_width': tr.find('td', attrs={'name': '11'}).text,
                        'format': tr.find('td', attrs={'name': '12'}).text,
                        'width': tr.find('td', attrs={'name': '13'}).text,
                        'edge': tr.find('td', attrs={'name': '14'}).text,
                        'level': tr.find('td', attrs={'name': '15'}).text,
                        'standard_thickness': tr.find('td', attrs={'name': '16'}).text,
                        'tradetype': tr.find('td', attrs={'name': 'tradeType'}).text,
                        'issueid': tr.find('td', attrs={'name': 'issueId'}).text,
                        'status': tr.find('td', attrs={'name': 'status'}).text,
                        'remark': tr.find('td', attrs={'class': 'remark'}).attrs.get('remark'),
                        'issuetime': tr.find('td', attrs={'name': 'issueTime'}).text,
                        'canceltime': tr.find('td', attrs={'name': 'cancelTime'}).text,
                        'invalidtime': tr.find('td', attrs={'name': 'invalidTime'}).text,
                    }
            data.append(data_detail)
        print(data)
        return data

    def fabulishichaxun_check(self, number=1, kind='冷轧304卷'):
        """发布历史查询界面数据核对"""
        self.select_by_text(kind, self.locator_goodsId)
        time.sleep(5)
        try:
            self.change_table_data('100')
        except TimeoutException:
            return None

        count = int(self.get_table_count())
        number = count if number > count else number

        time.sleep(5)
        trs = self.get_table_trs()
        data = []
        for index in range(number):
            tr = trs[index]
            if tr:
                if kind == '冷轧304卷':
                    data_detail = {
                        'goodsid': tr.find('td', attrs={'name': 'goodsName'}).text,
                        'contractid': tr.find('td', attrs={'name': 'contractId'}).text,
                        'premium': str(int(float(tr.find('td', attrs={'name': 'premium'}).text.replace(',', '').replace('￥', '')) * 1000)),
                        'stockcode': tr.find('td', attrs={'name': 'stockCode'}).text,
                        'factoryname': tr.find('td', attrs={'name': 'factoryName'}).text,
                        'weight': tr.find('td', attrs={'name': 'weight'}).text,
                        'weightleft': tr.find('td', attrs={'name': 'weightLeft'}).text,
                        'matchtotalqtt': tr.find('td', attrs={'name': 'matchTotalQtt'}).text,
                        'warehouse': tr.find('td', attrs={'name': 'warehouseName'}).text,
                        'material': tr.find('td', attrs={'name': '1'}).text,
                        'thickness': tr.find('td', attrs={'name': '2'}).text,
                        'standard_width': tr.find('td', attrs={'name': '3'}).text,
                        'format': tr.find('td', attrs={'name': '4'}).text,
                        'width': tr.find('td', attrs={'name': '5'}).text,
                        'edge': tr.find('td', attrs={'name': '6'}).text,
                        'level': tr.find('td', attrs={'name': '7'}).text,
                        'standard_thickness': tr.find('td', attrs={'name': '8'}).text,
                        'tradetype': tr.find('td', attrs={'name': 'tradeType'}).text,
                        'issueid': tr.find('td', attrs={'name': 'issueId'}).text,
                        'status': tr.find('td', attrs={'name': 'status'}).text,
                        'remark': tr.find('td', attrs={'class': 'remark'}).attrs.get('remark'),
                        'issuetime': tr.find('td', attrs={'name': 'issueTime'}).text,
                        'canceltime': tr.find('td', attrs={'name': 'cancelTime'}).text,
                        'invalidtime': tr.find('td', attrs={'name': 'invalidTime'}).text,
                    }
                else:
                    data_detail = {
                        'goodsid': tr.find('td', attrs={'name': 'goodsName'}).text,
                        'contractid': tr.find('td', attrs={'name': 'contractId'}).text,
                        'premium': tr.find('td', attrs={'name': 'premium'}).text,
                        'stockcode': tr.find('td', attrs={'name': 'stockCode'}).text,
                        'factoryname': tr.find('td', attrs={'name': 'factoryName'}).text,
                        'weight': tr.find('td', attrs={'name': 'weight'}).text,
                        'weightleft': tr.find('td', attrs={'name': 'weightLeft'}).text,
                        'matchtotalqtt': tr.find('td', attrs={'name': 'matchTotalQtt'}).text,
                        'warehouse': tr.find('td', attrs={'name': 'warehouseName'}).text,
                        'material': tr.find('td', attrs={'name': '9'}).text,
                        'thickness': tr.find('td', attrs={'name': '10'}).text,
                        'standard_width': tr.find('td', attrs={'name': '11'}).text,
                        'format': tr.find('td', attrs={'name': '12'}).text,
                        'width': tr.find('td', attrs={'name': '13'}).text,
                        'edge': tr.find('td', attrs={'name': '14'}).text,
                        'level': tr.find('td', attrs={'name': '15'}).text,
                        'standard_thickness': tr.find('td', attrs={'name': '16'}).text,
                        'tradetype': tr.find('td', attrs={'name': 'tradeType'}).text,
                        'issueid': tr.find('td', attrs={'name': 'issueId'}).text,
                        'status': tr.find('td', attrs={'name': 'status'}).text,
                        'remark': tr.find('td', attrs={'class': 'remark'}).attrs.get('remark'),
                        'issuetime': tr.find('td', attrs={'name': 'issueTime'}).text,
                        'canceltime': tr.find('td', attrs={'name': 'cancelTime'}).text,
                        'invalidtime': tr.find('td', attrs={'name': 'invalidTime'}).text,
                    }
            data.append(data_detail)
        print(data)
        return data

    def tihuoshenqing_check(self, number=1, kind='冷轧304卷'):
        """提货申请界面数据核对"""
        self.select_by_text(kind, self.locator_goodsId)
        self.change_table_data('100')
        time.sleep(5)

        count = self.get_table_count()
        count = 100 if count > 100 else count
        number = count if number > count else number

        trs = self.get_table_trs()
        datas = []
        for index in range(number):
            tr = trs[index]
            if tr:
                if kind == '冷轧304卷':
                    data = {
                        'warehouse': tr.find('td', attrs={'name': 'warehouseName'}).text,
                        'goodsid': tr.find('td', attrs={'name': 'goodsName'}).text,
                        'stockcode': tr.find('td', attrs={'name': 'stockCode'}).text,
                        'factoryname': tr.find('td', attrs={'name': 'factoryName'}).text,
                        'weightavlb': tr.find('td', attrs={'name': 'weightAvlb'}).text,
                        'material': tr.find('td', attrs={'name': '1'}).text,
                        'thickness': tr.find('td', attrs={'name': '2'}).text,
                        'standard_width': tr.find('td', attrs={'name': '3'}).text,
                        'format': tr.find('td', attrs={'name': '4'}).text,
                        'width': tr.find('td', attrs={'name': '5'}).text,
                        'edge': tr.find('td', attrs={'name': '6'}).text,
                        'level': tr.find('td', attrs={'name': '7'}).text,
                        'standard_thickness': tr.find('td', attrs={'name': '8'}).text,
                        'stocktype': tr.find('td', attrs={'name': 'stockType'}).text,
                        'stockid': tr.find('td', attrs={'name': 'stockId'}).text,
                    }
                else:
                    data = {
                        'warehouse': tr.find('td', attrs={'name': 'warehouseName'}).text,
                        'goodsid': tr.find('td', attrs={'name': 'goodsName'}).text,
                        'stockcode': tr.find('td', attrs={'name': 'stockCode'}).text,
                        'factoryname': tr.find('td', attrs={'name': 'factoryName'}).text,
                        'weightavlb': tr.find('td', attrs={'name': 'weightAvlb'}).text,
                        'material': tr.find('td', attrs={'name': '9'}).text,
                        'thickness': tr.find('td', attrs={'name': '10'}).text,
                        'standard_width': tr.find('td', attrs={'name': '11'}).text,
                        'format': tr.find('td', attrs={'name': '12'}).text,
                        'width': tr.find('td', attrs={'name': '13'}).text,
                        'edge': tr.find('td', attrs={'name': '14'}).text,
                        'level': tr.find('td', attrs={'name': '15'}).text,
                        'standard_thickness': tr.find('td', attrs={'name': '16'}).text,
                        'stocktype': tr.find('td', attrs={'name': 'stockType'}).text,
                        'stockid': tr.find('td', attrs={'name': 'stockId'}).text,
                    }
                datas.append(data)
        print(datas)
        return datas

    def shenqingtihuo(self, kind='冷轧304卷', one=True):
        """申请提货"""
        self.select_by_text(kind, self.locator_goodsId)
        self.move(500, 500)
        time.sleep(1)

        if one:
            js_one = 'document.getElementsByClassName("singleBox")[0].click()'
            self.run_js(js_one)
            # self.find_element_click(self.locator_tihuoshenqing_first)
        else:
            js_all = 'document.getElementsByClassName("selectAll")[0].click()'
            self.run_js(js_all)
            # self.find_element_click(self.locator_tihuoshenqing_all)

        self.find_element_click(self.locator_shenqingtihuo)
        self.find_element_click(self.locator_tihuoshenqing_yes)

    def tihuoshenqingchaxun_check(self, number=1, kind='冷轧304卷'):
        """提货申请查询界面数据核对"""

        # 选择商品，更改每页数据条数
        self.select_by_text(kind, self.locator_goodsId)
        self.change_table_data('100')
        time.sleep(5)

        count = int(self.get_table_count())
        # 如果数据总数大于100，在100中取；如果随机数大于总数据，取总数居
        count = 100 if count > 100 else count
        number = count if number > count else number

        trs = self.get_table_trs()

        datas = []
        # 列表从上往下取数据
        for index in range(number):
            tr = trs[index]
            if tr:
                count_weight = int(
                    tr.find(
                        'td', attrs={
                            'name': 'weightTotal'}).text)
                goodsid = tr.find('td', attrs={'name': 'goodsName'}).text

            # 点击+号
            js = 'document.getElementsByClassName("plus_get_more")[{}].click()'.format(
                index)
            time.sleep(2)
            self.run_js(js)
            time.sleep(5)

            # 获得内层数据
            html = self.get_html()
            soup = BeautifulSoup(html, 'html.parser')
            tr_in = soup.find('tr', attrs={'class': 'add_more_tr'})
            tbody_in = tr_in.find('tbody')
            trs_in = tbody_in.find_all('tr')
            cal_weight = 0
            data = []
            for t in trs_in:
                # 获得子列表中的数据，以及计算总重
                cal_weight += int(t.find('td', attrs={'name': 'weight'}).text)

                data_detail = {
                    'goodsid': goodsid,
                    'stockcode': t.find('td', attrs={'name': 'stockCode'}).text,
                    'factoryname': t.find('td', attrs={'name': 'factoryName'}).text,
                    'weight': t.find('td', attrs={'name': 'weight'}).text,
                    'material': t.find('td', attrs={'name': re.compile('冷轧\d+材质/表面')}).text,
                    'thickness': t.find('td', attrs={'name': re.compile('冷轧\d+标准厚度')}).text,
                    'standard_width': t.find('td', attrs={'name': re.compile('冷轧\d+标准宽度')}).text,
                    'format': t.find('td', attrs={'name': re.compile('冷轧\d+标签规格')}).text,
                    'width': t.find('td', attrs={'name': re.compile('冷轧\d+实宽')}).text,
                    'edge': t.find('td', attrs={'name': re.compile('冷轧\d+边部')}).text,
                    'level': t.find('td', attrs={'name': re.compile('冷轧\d+等级')}).text,
                    'standard_thickness': t.find('td', attrs={'name': re.compile('冷轧\d+参厚')}).text,
                    'warehouse': t.find('td', attrs={'name': 'warehouseName'}).text,
                    'stocksource': t.find('td', attrs={'name': 'stockSource'}).text,
                    'stockid': t.find('td', attrs={'name': 'stockId'}).text,
                }
                data.append(data_detail)

            datas.append({'cal_weight': cal_weight,
                          'count_weight': count_weight,
                          'data_detail': data})
            self.fresh()
            self.into_tihuoshenqingchaxun()
            self.select_by_text(kind, self.locator_goodsId)
            self.change_table_data('100')
        print(datas)
        return datas

        pass

    def tihuodanchaxun_check(self):
        """提货单查询数据核对"""
        pass

    def shopping_cart(self, all=True):
        """购物车"""
        time.sleep(2)
        if all:
            self.find_element_click(self.locator_bottomSelectAll)
        else:
            self.find_element_click(self.locator_table_first)
        self.find_element_click(self.locator_add_cart)
        self.find_element_click(self.locator_cartCount)

        # 全选购物车并获取所选需求单总数
        self.move_botton()
        time.sleep(2)

        js = 'document.getElementById("bottomSelectAll").click()'
        self.run_js(js)
        time.sleep(1)
        # self.find_element_click(self.locator_bottomSelectAll)
        num = self.get_text(self.locator_selectedNum)

        self.find_element_click(self.locator_buy_now)
        self.find_element_click(self.locator_btn_pipei)
        return int(num)

    def pipei_check(self, number=1, kind='冷轧304卷'):
        """匹配查询界面数据核对"""

        # 选择商品，更改页面数据条数
        self.select_by_text(kind, self.locator_goodsId)
        self.change_table_data('100')

        count = int(self.get_table_count())
        count = 100 if count > 100 else count
        number = count if number > count else number

        trs = self.get_table_trs()
        datas = []
        for index in range(number):
            # 获得外层数据
            tr = trs[index]
            if tr:
                goodsid = tr.find('td', attrs={'name': 'goodsName'}).text
                contractid = tr.find('td', attrs={'name': 'contractId'}).text
                weightmatch = tr.find('td', attrs={'name': 'weightMatch'}).text
                premium = self.deal_premium(
                    tr.find('td', attrs={'name': 'premium'}).text)
                price = tr.find('td', attrs={'name': 'price'}).text
                credit = tr.find('td', attrs={'name': 'credit'}).text
                remark = tr.find(
                    'td', attrs={
                        'class': 'remark'}).attrs.get('remark'),

            # 点击+号
            js = 'document.getElementsByClassName("plus_get_more")[{}].click()'.format(
                index)
            time.sleep(2)
            self.run_js(js)

            time.sleep(5)

            # 获得内层数据
            html = self.get_html()
            soup = BeautifulSoup(html, 'html.parser')
            tr = soup.find('tr', attrs={'class': 'add_more_tr'})
            tbody = tr.find('tbody')
            tr = tbody.find('tr')
            if tr:
                data = {
                    'goodsid': goodsid,
                    'contractid': contractid,
                    'weightmatch': weightmatch,
                    'premium': premium,
                    'price': price,
                    'credit': credit,
                    'remark': remark,
                    'stockcode': tr.find('td', attrs={'name': 'stockCode'}).text,
                    'factoryname': tr.find('td', attrs={'name': 'factoryName'}).text,
                    'weighttotal': tr.find('td', attrs={'name': 'weightTotal'}).text,
                    'material': tr.find('td', attrs={'name': re.compile('冷轧\d+材质/表面')}).text,
                    'thickness': tr.find('td', attrs={'name': re.compile('冷轧\d+标准厚度')}).text,
                    'standard_width': tr.find('td', attrs={'name': re.compile('冷轧\d+标准宽度')}).text,
                    'format': tr.find('td', attrs={'name': re.compile('冷轧\d+标签规格')}).text,
                    'width': tr.find('td', attrs={'name': re.compile('冷轧\d+实宽')}).text,
                    'edge': tr.find('td', attrs={'name': re.compile('冷轧\d+边部')}).text,
                    'level': tr.find('td', attrs={'name': re.compile('冷轧\d+等级')}).text,
                    'standard_thickness': tr.find('td', attrs={'name': re.compile('冷轧\d+参厚')}).text,
                    'warehouse': tr.find('td', attrs={'name': 'warehouseName'}).text,
                    'remark': tr.find('td', attrs={'name': 'stockRemark'}).attrs.get('remark'),
                }
                self.fresh()
                self.select_by_text(kind, self.locator_goodsId)
                self.change_table_data('100')
            datas.append(data)
        print(datas)
        return datas


if __name__ == '__main__':
    now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    process = Process_Front()
    process.process_login('zwh_e835')

    # process.open_url('http://192.168.1.43:8083/')
    # process.index_check(number=5)
    # process.shopping_cart()

    # 退出
    # process.quit()

    # 进入库存查询
    # process.into_kucunchaxun()
    # process.kucunchaxun_check()

    # 进入实物入库
    # process.into_shiwuruku()
    # process.shiwuruku_apply()
    # #获得实物入库table所有数据
    # process.get_shiwuruku_alldata(10)

    # 实物入库删除
    # process.shiwuruku_del(all=False)

    # 添加明细
    # process.ruku_add_detail()

    # 申请入库
    # process.shiwuruku_apply(all=False)

    # 进入入库申请查询
    # process.into_rukushenqingchaxun()
    # process.rukushengqingchaxun_check(2)

    # 进入商品上架界面
    # process.into_shangpinshangjia()
    # process.fabu(premium='100',invateOneTime=True)
    # process.shangpinshangjia_check(1)

    # #进入发布界面
    # text=process.into_fabu()
    # text.replace(' ','')
    # print(text)
    # process.fabu_check()

    # 首页查询
    # process.index_query()

    # 进入匹配查询
    # process.into_pipeichaxun()
    # process.pipei_first()
    # process.pipei_check(1)

    # 进入发布历史查询界面
    # process.into_fabulishichaxun()
    # process.fabulishichaxun_check(3)

    # process.into_tihuoshenqing()
    # # process.tihuoshenqing_check(2)
    # process.shenqingtihuo(one=False)

    # 进入提货申请查询
    process.into_tihuoshenqingchaxun()
    process.tihuoshenqingchaxun_check()
