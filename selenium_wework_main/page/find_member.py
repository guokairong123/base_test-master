from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_wework_main.page.base import Base


class FindMember(Base):
    def find_member(self, value):
        WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.ww_checkbox')))
        elements = self._driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_tr_Inactive>td:nth-child(2)')
        for element in elements:
            print(element.get_attribute("title"))
            if value == element.get_attribute("title"):
                return True