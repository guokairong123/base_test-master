from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_wework_main.page.base import Base
from selenium_wework_main.page.find_member import FindMember


class AddMember(Base):

    def add_member(self):
        self._driver.find_element_by_id('username').send_keys('hello world')
        self._driver.find_element_by_id('memberAdd_acctid').send_keys('good')
        self._driver.find_element_by_id('memberAdd_phone').send_keys('12345678912')
        self._driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()
        return FindMember(self._driver)
