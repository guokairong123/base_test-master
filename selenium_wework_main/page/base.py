from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class Base:
    _driver = None
    _base_url = ""

    # 构造方法，每次引用类时都会调用
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            # 复用当前浏览器
            self._driver = webdriver.Chrome(options=option)
            # 隐性等待
            self._driver.implicitly_wait(3)
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

