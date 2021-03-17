import shelve
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestWXWrokLogin():
    def setup(self):
        # 复用当前浏览器
        options = Options()
        # cmd输入 chrome --remote-debugging-port=9222，端口自由定义
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # self.driver.find_element_by_id("menu_contacts").click()

        # 持久化存储，文件名为cookies，对象为db，第一次使用open类似set，再次使用open即为get
        db = shelve.open("cookies")

        # 把网页的cookies报存在db['cookie']中
        # db['cookie'] = self.driver.get_cookies()
        cookies = db['cookie']
        for cookie in cookies:
            # 去除掉影响数据
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(3)

        # 同步并关闭对象db
        db.close()
