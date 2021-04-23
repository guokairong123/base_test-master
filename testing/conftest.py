import pytest


#  autouse=True 默认所有测试用例都使用这个方法
@pytest.fixture(scope="function")
def login():
    # setup 操作
    print("登录操作")
    # yield 相当于 return 操作
    yield ['tom', '123456']
    # teardown 操作
    print("登出操作")


@pytest.fixture(autouse=True, scope="session")
def conn_db():
    print("数据库链接")
    yield "database"
    print("关闭数据库链接")


def pytest_collection_modifyitems(session, config, items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')