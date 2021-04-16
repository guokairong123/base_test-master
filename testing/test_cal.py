import pytest

from pythoncode.calculator import Calculator


class TestCal(Calculator):
    def setup(self):
        self.calc = Calculator()

    @pytest.mark.parametrize("a, b", [
        (2, 3),
        (1, 3)
    ])
    def test_add(self, a, b):
        result = self.calc.add(a, b)
        assert result == a+b

    def test_sub(self):
        result = self.calc.sub(5, 3)
        assert result == 2

    def test_mul(self):
        result = self.calc.mul(3, 7)
        assert result == 21

    def test_div(self):
        result = self.calc.div(6, 2)
        assert result == 3
