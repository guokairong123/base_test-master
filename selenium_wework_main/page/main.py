from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_wework_main.page.add_member import AddMember
from selenium_wework_main.page.base import Base


class Main(Base):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_addmenber(self):
        self._driver.find_element(By.CSS_SELECTOR, '#menu_contacts').click()
        locator = (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1) .js_add_member')
        # 显性等待
        WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self._driver.find_element(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1) .js_add_member').click()
        return AddMember(self._driver)
