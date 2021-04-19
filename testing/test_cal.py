import pytest
import yaml

from pythoncode.calculator import Calculator


def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    return [add_datas, add_ids]


def steps(calc, a, b, expect):
    with open("./datas/add_steps.yml") as f:
        steps = yaml.safe_load(f)
    for step in steps:
        if 'add' == step:
            print("step: add")
            result = calc.add(a, b)
        elif 'add1' == step:
            print("step: add1")
            result = calc.add1(a, b)
        assert expect == result


class TestCal(Calculator):
    def setup(self):
        self.calc = Calculator()

    @pytest.mark.parametrize("a, b, expect", get_datas()[0], ids=get_datas()[1])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    def test_sub(self):
        result = self.calc.sub(5, 3)
        assert result == 5

    def test_mul(self):
        result = self.calc.mul(3, 7)
        assert result == 21

    def test_div(self):
        result = self.calc.div(6, 2)
        assert result == 3

    def test_add_steps(self):
        a = 1
        b = 2
        expect = 3
        # assert 2 == self.calc.add(1, 1)
        # assert 3 == self.calc.add1(1, 2)
        # assert 0 == self.calc.add(-1, 1)
        steps(self.calc, a, b, expect)
