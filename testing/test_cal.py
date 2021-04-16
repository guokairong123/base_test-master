
from pythoncode.calculator import Calculator


class TestCal(Calculator):
    def setup(self):
        self.calc = Calculator()
    
    def test_add(self):
        result = self.calc.add(2, 3)
        assert result == 5

    def test_sub(self):
        result = self.calc.sub(5, 3)
        assert result == 2

    def test_mul(self):
        result = self.calc.mul(3, 7)
        assert result == 21

    def test_div(self):
        result = self.calc.div(6, 2)
        assert result == 3
