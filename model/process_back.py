from object import Page
from selenium.webdriver.common.by import By
import datetime
import time
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException


class Process_Back(Page):
    """后台类"""

    # 菜单栏定位器
    locator_jichuguanli = (By.ID, 'afis_menu_node_a_16')
    locator_bangzhuzhongxin = (By.ID, 'afis_menu_node_a_81')
    locator_zhanghaoguanli = (By.ID, 'afis_menu_node_a_17')
    locator_caidanguanli = (By.ID, 'afis_menu_node_a_18')
    locator_jueseguanli = (By.ID, 'afis_menu_node_a_19')
    locator_quanxianguanli = (By.ID, 'afis_menu_node_a_20')
    locator_juesecaozuoyuanguanli = (By.ID, 'afis_menu_node_a_21')
    locator_neirongguanli = (By.ID, 'afis_menu_node_a_101')

    locator_huiyuanguanli = (By.ID, 'afis_menu_node_a_22')
    locator_huiyuanxinxichaxun = (By.ID, 'afis_menu_node_a_23')
    locator_huiyuanxinxiguanli = (By.ID, 'afis_menu_node_a_24')

    locator_rukuguanli = (By.ID, 'afis_menu_node_a_25')
    locator_shiwuruku = (By.ID, 'afis_menu_node_a_26')
    locator_rukufuhe = (By.ID, 'afis_menu_node_a_28')
    locator_cangchukucundaoru = (By.ID, 'afis_menu_node_a_102')

    locator_kucunguanli = (By.ID, 'afis_menu_node_a_29')
    locator_kucunchaxun = (By.ID, 'afis_menu_node_a_30')
    locator_kucunhuizongchaxun = (By.ID, 'afis_menu_node_a_31')
    locator_huoquanzhuanrang = (By.ID, 'afis_menu_node_a_32')
    locator_huoquanzhuanrangchaxun = (By.ID, 'afis_menu_node_a_33')
    locator_kucunguohu = (By.ID, 'afis_menu_node_a_34')
    locator_chukuguanli = (By.ID, 'afis_menu_node_a_35')
    locator_jiaoyicangdanchaxun = (By.ID, 'afis_menu_node_a_36')
    locator_kucunlishichaxun = (By.ID, 'afis_menu_node_a_37')
    locator_kucuncaozuojilu = (By.ID, 'afis_menu_node_a_38')

    locator_jiaoshouguanli = (By.ID, 'afis_menu_node_a_63')
    locator_pipeichaxun = (By.ID, 'afis_menu_node_a_64')
    locator_jiaoshoushenhe = (By.ID, 'afis_menu_node_a_65')
    locator_jiesuanshenhe = (By.ID, 'afis_menu_node_a_66')
    locator_jiaoshouchuli = (By.ID, 'afis_menu_node_a_67')

    # 登陆界面定位器
    locator_name = (By.NAME, 'name')
    locator_pwd = (By.NAME, 'pwd')
    locator_vercode = (By.NAME, 'vercode')
    locator_btn = (By.XPATH, '/html/body/div/div/div/div[2]/div[4]/input')

    def login(self, username, password):
        self.find_element_type(username, self.locator_name)
        self.find_element_type(password, self.locator_pwd)
        self.find_element_type('1234', self.locator_vercode)
        self.find_element_click(self.locator_btn)

    def into_jiaoshoushenhe(self):
        """进入交收审核界面"""
        self.find_element_click(self.locator_jiaoshouguanli)
        self.find_element_click(self.locator_jiaoshoushenhe)

    def into_jiesuanshenhe(self):
        """进入结算审核界面"""
        self.find_element_click(self.locator_jiaoshouguanli)
        self.find_element_click(self.locator_jiesuanshenhe)

    def into_jiaoshouchuli(self):
        """进入交收处理界面"""
        self.find_element_click(self.locator_jiaoshouguanli)
        self.find_element_click(self.locator_jiaoshouchuli)


if __name__ == '__main__':
    process = Process_Back()
    process.open_url('http://192.168.1.43:8090/')
    process.login('zwh', '123456')
    process.into_jiaoshoushenhe()
