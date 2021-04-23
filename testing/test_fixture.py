from time import sleep

import pytest


@pytest.mark.run(order=3)
@pytest.mark.usefixtures("login")
def test_case1():
    print("用例1")


@pytest.mark.run(order=4)
@pytest.mark.parametrize('a', [1, 2, 3])
def test_case2(a):
    sleep(2)
    print("用例2")


@pytest.mark.run(order=2)
def test_case3(login, conn_db):
    print(login)
    print(conn_db)
    print("用例3")


@pytest.mark.run(order=1)
def test_case4():
    pytest.assume(True)
    pytest.assume(False)
