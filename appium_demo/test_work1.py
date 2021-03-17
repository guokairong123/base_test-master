import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *


class TestWork1:
    def setup_class(self):
        #print("这是setup_class方法")
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.common.MainActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    @pytest.mark.parametrize('searchKeys, type, except_price',[
        ('alibaba', 'BABA', 190),
        ('jd', 'JD', 50),
        ('xiaomi', '01810', 11),
        ('google', 'GOOGL', 1300)
    ])
    def test_work1(self, searchKeys, type, except_price):
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/home_search').click()
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/search_input_text').send_keys(searchKeys)
        self.driver.find_element_by_xpath(f"//*[@text='{type}']").click()
        current_price = float(self.driver.find_element(MobileBy.XPATH, f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        assert_that(current_price, close_to(except_price, except_price*0.1))

    def teardown(self):
        #print("这是teardown方法")
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/action_close').click()

    def teardown_class(self):
        #print("这是teardown_class方法")
        self.driver.quit()