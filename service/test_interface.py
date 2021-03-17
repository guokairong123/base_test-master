import requests
from jsonpath import jsonpath
from hamcrest import *
from requests.auth import HTTPBasicAuth


class TestInterface:
    def test_hogwarts_json(self):
        r = requests.get("https://ceshiren.com/categories.json")
        print(r.text)
        assert r.status_code == 200
        assert r.json()["category_list"]["categories"][0]["name"] == "开源项目"
        print(jsonpath(r.json(), '$..name'))
        assert jsonpath(r.json(), '$..name')[0] == "开源项目"

    def test_hamcrest(self):
        r = requests.get("https://ceshiren.com/categories.json")
        print(r.text)
        assert r.status_code == 200
        assert_that(r.json()["category_list"]["categories"][0]["name"], equal_to("开源项目"))

    def test_auth(self):
        r = requests.get(url="https://httpbin.testing-studio.com/basic-auth/guokairong/123",
                         auth=HTTPBasicAuth("guokairong", "123"))
        print(r.text)