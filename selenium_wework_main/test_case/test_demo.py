from selenium_wework_main.page.main import Main


class TestDemo:
    def setup(self):
        self.main = Main()

    def test_demo(self):
        add_member = self.main.goto_addmenber().add_member()
        assert add_member.find_member("hello world")
