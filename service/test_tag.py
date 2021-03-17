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
        ['ettrhEDwAApRUtlv5QLoPY8nGvamIyVg', 'tag_new'],
        ['ettrhEDwAApRUtlv5QLoPY8nGvamIyVg', '中文'],
        ['ettrhEDwAApRUtlv5QLoPY8nGvamIyVg', '你是']
    ])
    def test_tag_list(self, tag_id, name):
        tag_name = name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M"))
        group_name = '测试'
        self.tag.update(id=tag_id, name=tag_name)
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
        group_name = "test"
        tag = [
            {"name": "test2"},
            {"name": "test4"},
            {"name": "test5"}
        ]
        self.tag.add(group_name=group_name, tag=tag)

    def test_delete_group(self):
        group_id = "ettrhEDwAAVEzFZl-qf_FJtlwxN4ERLQ"
        self.tag.delete_group(group_id=group_id)

    def test_delete_id(self):
        tag_id = "ettrhEDwAAVEzFZl-qf_FJtlwxN4ERLQ"
        self.tag.delete_tag(tag_id=tag_id)