import pytest


@pytest.mark.usefixtures("login")
def test_case1():
    print("用例1")


def test_case2():
    print("用例2")


def test_case3(login, conn_db):
    print(login)
    print(conn_db)
    print("用例3")


def test_case4():
    pytest.assume(True)
    pytest.assume(False)
