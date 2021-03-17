from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_demo.page.base import Base


class MemberInformation(Base):
    # 删除成功
    def delete_member(self):
        # 滚动查找，需加深理解
        self._driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("删除成员"))').click()
        self.find(MobileBy.XPATH, "//*[@text='确定']").click()
        return self

    # 回到通讯录页面
    def goto_address_list(self):
        locator = (MobileBy.ID, 'com.tencent.wework:id/gvd')
        WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        self.find(locator).click()
        from appium_demo.page.address_list import AddressList
        return AddressList(self._driver)
