import datetime
import json

import pytest

from service.tag import Tag


class TestClassic:
    def setup_class(self):
        self.tag = Tag()
        # r = self.tag.add()
        # self.tag_id = r.json()['tag_group']['tag']['id']

    @pytest.mark.parametrize('tag_id,name', [
        ['ettrhEDwAAJ68kxUxAVsQ8xwDCK5KOTg', 'tag_new'],
        ['ettrhEDwAAGxx8807ekDQoSb1xd5-1Kw', '中文'],
        ['ettrhEDwAA8zLl_-JiC5KSB0hADr1SgA', '你是']
    ])
    def test_tag_list(self, tag_id, name):
        tag_name = name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M"))
        group_name = '测试'
        self.tag.update(tag_id, tag_name)
        r = self.tag.list()
        print(json.dumps(r.json(), indent=2))
        tag = [
            tag
            for group in r.json()['tag_group'] if group['group_name'] == group_name
            for tag in group['tag'] if tag['name'] == tag_name
        ]
        print(tag)
        assert tag != []

    def test_clean(self):
        pass

    def test_get_list(self):
        self.tag.list()

    def test_add(self):
        r = self.tag.add()
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

    def test_before_add(self):
        group_name = "test1111"
        tag = [
            {"name": "test1"},
            {"name": "test2"},
            {"name": "test3"}
        ]
        r = self.tag.before_add(group_name, tag)
        assert r

    # 40068 invalid tagid
    # 删除的元素不存在
    def test_delete_group(self):
        group_id = "ettrhEDwAAVEzFZl-qf_FJtlwxN4ERLQ"
        self.tag.delete_group(group_id=group_id)

    def test_delete_id(self):
        tag_id = "ettrhEDwAAVEzFZl-qf_FJtlwxN4ERLQ"
        self.tag.delete_tag(tag_id=tag_id)

    def test_delete_and_detect_group(self):
        group_id = ["ettrhEDwAAloLp0iUKFO6kShc9C23-7w"]
        self.tag.delete_and_detect_group(group_id)