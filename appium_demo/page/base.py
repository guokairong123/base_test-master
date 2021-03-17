import logging

from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class Base:
    _driver = None
    _black_list = [
        (MobileBy.XPATH, "//*[@text='确认']"),
        (MobileBy.XPATH, "//*[@text='确定']"),
        (MobileBy.XPATH, "//*[@text='同意']"),
        (MobileBy.XPATH, "//*[@text='允许']")
    ]

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            print("初始化driver")
            desired_caps = {'platformName': 'Android',
                            'platformVersion': '6.0',
                            'deviceName': '127.0.0.1:7555',
                            'appPackage': 'com.tencent.wework',
                            'appActivity': '.launch.WwMainActivity',
                            'dontStopAppOnReset': 'true',
                            'noReset': 'true',
                            'skipServerInstallation': 'true',
                            'skipDeviceInitialization': 'true',
                            'unicodeKeyboard': 'true',
                            'resetKeyboard': 'true'
                            }
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self._driver.implicitly_wait(10)
        else:
            self._driver = driver

    def find(self, locator, value: str = None):

        element: WebElement

        try:
            # 列表推导式
            element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(locator, value)
            # if isinstance(locator, tuple):
            #     return self._driver.find_element(*locator)
            # else:
            #     return self._driver.find_element(locator, value)
            self._driver.implicitly_wait(10)
            return element
        except Exception as e:
            # 找不到元素，可能有弹窗，先对弹窗进行处理
            print("处理弹窗")
            self._driver.implicitly_wait(1)
            for locator1 in self._black_list:
                ele = self._driver.find_elements(*locator1)
                logging.info(ele)
                if len(ele) > 0:
                    ele[0].click()
                    return self.find(locator, value)
            raise e

    def stop_driver(self):
        self._driver.quit()