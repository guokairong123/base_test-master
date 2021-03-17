from appium import webdriver

class TestAppiumPytest:
    def setup(self):
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

    def teardowm(self):
        self.driver.back()
        self.driver.quit()

    def test_appiumpytest(self):
        self.driver.find_element_by_id('com.xueqiu.android:id/home_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id('com.xueqiu.android:id/current_price').text)
        assert current_price > 200