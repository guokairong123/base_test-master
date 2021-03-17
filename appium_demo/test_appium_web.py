from time import sleep

from appium import webdriver


class TestAppiumWeb:
    def setup(self):

        desired_caps = {'platformName': 'Android',
                        'platformVersion': '6.0',
                        'deviceName': '127.0.0.1:7555',
                        'noReset': 'true',
                        'dontStopAppOnReset': 'true',
                        'unicodeKeyboard': 'true',
                        'resetKeyboard': 'true',
                        'browserName': 'Browser',
                        'chromedriverExecutable': 'E:/Files/chromedriver/52.0/chromedriver.exe'
                    }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass

    def test_appium_web(self):
        self.driver.get("https://m.baidu.com")
        sleep(3)