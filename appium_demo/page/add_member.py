from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_demo.page.base import Base


class AddMember(Base):

    # 输入姓名
    def input_name(self, name):
        self.find(MobileBy.XPATH, "//*[@text='姓名　']/../*[@class='android.widget.EditText']").send_keys(
            name)
        return self

    # 选择性别
    def select_gender(self, gender):
        self.find(MobileBy.XPATH, "//*[@text='性别']/../*[@class='android.widget.RelativeLayout']").click()
        self.find(MobileBy.XPATH, f"//*[@text='{gender}']").click()
        return self

    # 输入手机号码
    def input_iphone_num(self, number):
        self.find(MobileBy.XPATH, "//*[@text='手机号']").send_keys(number)
        return self

    # 点击保存
    def click_save(self):
        self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gvk']").click()
        return self

    # 回到通讯录页面
    def goto_address_list(self):
        locator = (MobileBy.ID, 'com.tencent.wework:id/gv3')
        WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        self.find(locator).click()
        from appium_demo.page.address_list import AddressList
        return AddressList(self._driver)
