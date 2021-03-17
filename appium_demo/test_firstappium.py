from appium import webdriver

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
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.implicitly_wait(10)
driver.find_element_by_id('com.xueqiu.android:id/home_search').click()
driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('alibaba')
driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()


driver.back()
driver.quit()
