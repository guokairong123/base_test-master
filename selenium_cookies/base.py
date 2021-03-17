from selenium import webdriver


class Base():
    def setup(self):
        self.driver =  webdriver.Chrome()

    def teardown(self):
        self.driver.quit()