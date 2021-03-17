from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_demo.page.main import Main


class TestWork2:
    def setup_class(self):
        self.main = Main()

    @pytest.mark.skip
    # @pytest.mark.parametrize('name, gender, number',[
    #     ('service', '男', '17876254444'),
    #     ('test1', '女', '17876254578'),
    #     ('test2', '女', '17876253546'),
    #     ('test3', '男', '17876253666')
    # ])
    @pytest.mark.parametrize('name, gender, number', yaml.safe_load(open('./add.yaml', encoding='utf-8')))
    # 添加成员
    def test_work2_add(self, name, gender, number):
        self.main.goto_address_list().goto_add_member().input_name(name).select_gender(gender)\
        .input_iphone_num(number).click_save().goto_address_list()
        # toast = self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']").text
        # #print(self.driver.page_source)
        # assert toast == '添加成功'

    #@pytest.mark.skip
    # @pytest.mark.parametrize('name', [
    #     'service',
    #     'test1',
    #     'test2',
    #     'test3'
    # ])
    @pytest.mark.parametrize('name', yaml.safe_load(open('./delete.yaml', encoding='utf-8')))
    # 删除成员
    def test_work2_delete(self, name):
        self.main.goto_address_list().set_member().goto_member_information(name).delete_member()\
            .goto_address_list()

    def teardown_class(self):
        self.main.stop_driver()
