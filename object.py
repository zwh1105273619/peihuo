from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class Page:
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver=webdriver.PhantomJS()
        self.driver.maximize_window()

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return WebDriverWait(
            self.driver, 8).until(
            expected_conditions.visibility_of_element_located(
                *locator))

    def find_elements_id(self, id):
        return self.driver.find_elements_by_id(id)

    def find_element_xpath(self, xpath):
        return self.driver.find_elements_by_xpath(xpath)

    def find_element_click(self, *locator):
        WebDriverWait(
            self.driver, 8).until(
            expected_conditions.visibility_of_element_located(
                *locator)).click()

    def find_elements_by_tag(self, tag):
        return self.driver.find_elements_by_tag_name(tag)

    def find_element_type(self, content, *locator):
        ele = WebDriverWait(
            self.driver, 8).until(
            expected_conditions.visibility_of_element_located(
                *locator))
        ele.clear()
        ele.send_keys(content)

    def select_by_text(self, text, *locator):
        ele = WebDriverWait(
            self.driver, 8).until(
            expected_conditions.visibility_of_element_located(
                *locator))
        Select(ele).select_by_visible_text(text)

    def select_by_text_ele(self, text, ele):
        Select(ele).select_by_visible_text(text)

    def select_by_index(self, index, *locator):
        ele = WebDriverWait(
            self.driver, 8).until(
            expected_conditions.visibility_of_element_located(
                *locator))
        Select(ele).select_by_index(index)

    def get_select_options(self, *locator):
        ele = WebDriverWait(
            self.driver, 8).until(
            expected_conditions.visibility_of_element_located(
                *locator))
        return Select(ele).options

    def find_elements_xpath(self, xpath):
        eles = self.driver.find_elements_by_xpath(xpath)
        return eles

    def get_text(self, *locator):
        ele = WebDriverWait(
            self.driver, 8).until(
            expected_conditions.visibility_of_element_located(
                *locator))
        return ele.text

    def fresh(self):
        self.driver.refresh()

    def get_html(self):
        return self.driver.page_source

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def move_ele(self, target):
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def move(self, width, height):
        js = "window.scrollTo({},{})".format(width, height)
        self.driver.execute_script(js)

    def move_top(self):
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def move_botton(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def run_js(self, js):
        self.driver.execute_script(js)

    def deal_premium(self, premium):
        data = premium.replace(',', '')
        data = data.replace('￥', '')
        data = float(data)
        data = data * 1000
        data = int(data)
        data = str(data)
        return data

    def close(self):
        self.driver.close()
