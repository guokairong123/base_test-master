import pytest


@pytest.mark.login
def test_login1():
    print("登录用例1")


@pytest.mark.login
def test_login2():
    print("登录用例2")


@pytest.mark.search
def test_search1():
    print("搜索用例1")


@pytest.mark.search
def test_search2():
    print("搜索用例2")