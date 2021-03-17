from appium.webdriver.common.mobileby import MobileBy

from appium_demo.page.base import Base


class AddressList(Base):
    # 进入到添加用户页面
    def goto_add_member(self):
        self.find(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        from appium_demo.page.add_member import AddMember
        return AddMember(self._driver)

    # 点击管理成员
    def set_member(self):
        self.find(MobileBy.ID, 'com.tencent.wework:id/gvi').click()
        return self

    # 进入到用户信息页
    def goto_member_information(self, name):
        self.find(MobileBy.XPATH,
                                 f"//*[@text='{name}']/../../../..//*[@resource-id='com.tencent.wework:id/fdh']").click()
        from appium_demo.page.member_information import MemberInformation
        return MemberInformation(self._driver)