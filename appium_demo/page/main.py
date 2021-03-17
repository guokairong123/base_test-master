from appium.webdriver.common.mobileby import MobileBy

from appium_demo.page.address_list import AddressList
from appium_demo.page.base import Base


# 点击底部的通讯录
class Main(Base):
    def goto_address_list(self):
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressList(self._driver)
