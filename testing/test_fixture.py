import pytest


@pytest.fixture
def login():
    # setup 操作
    print("登录操作")
    # yield 相当于 return 操作
    yield ['tom', '123456']
    # teardown 操作
    print("登出操作")


@pytest.mark.usefixtures("login")
def test_case1():
    print("用例1")


def test_case2():
    print("用例2")


def test_case3(login):
    print(login)
    print("用例3")
