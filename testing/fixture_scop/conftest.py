import pytest


@pytest.fixture
def conn_db():
    print("数据库链接aaa")
    yield "database"
    print("关闭数据库链接")