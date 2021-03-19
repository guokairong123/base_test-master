import json

import requests

from service.base_api import BaseApi


class Tag(BaseApi):

    def __init__(self):
        super().__init__()

    def is_group_name_exits(self, group_name):
        for group in self.list().json()["tag_group"]:
            print(group)
            # 查询元素是否存在，如果不存在，报错
            if group_name in group["group_name"]:
                return group["group_id"]
        # print("group name not in gout")
        # return False
        raise False

    def is_group_id_exits(self, group_id):
        for group in self.list().json()["tag_group"]:
            print(group)
            # 查询元素是否存在，如果不存在，报错
            if group_id in group["group_id"]:
                return True
        # print("group name not in gout")
        # return False
        return False

    def add(self, group_name, tag, **kwargs):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "params": {"access_token": self.token},
            "json": {
                "group_name": group_name,
                "tag": tag,
                **kwargs
            }
        }
        # r = requests.post(
        #     'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
        #     params={"access_token": self.token},
        #     json={
        #         "group_name": group_name,
        #         "tag": tag,
        #         **kwargs
        #     }
        # )
        r = self.send(data)
        print(json.dumps(r.json(), indent=2))
        return r

    def before_add(self, group_name, tag, **kwargs):
        r = self.add(group_name, tag, **kwargs)
        # 如果添加的元素已经存在
        if r.json()["errcode"] == 40071:
            group_id = self.is_group_name_exits(group_name)
            if not group_id:
                return False
            self.delete_group(group_id)
            self.add(group_name, tag, **kwargs)

        result = self.is_group_name_exits(group_name)
        if not result:
            print("add not success")
        return result

    def list(self):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={"access_token": self.token},
            json={
                'json': []
            }
        )
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        print(json.dumps(r.json(), indent=2))
        return r

    def update(self, id='', name=''):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            params={"access_token": self.token},
            json={
                'id': id,
                'name': name
            }
        )
        # print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

# 查询tag_id -> 删除tag_id
#
    def delete_group(self, group_id):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={"access_token": self.token},
            json={
                "group_id": group_id
            }
        )
        print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        return r

    def delete_tag(self, tag_id):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={"access_token": self.token},
            json={
                "tag_id": tag_id
            }
        )
        print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        return r

    def delete_and_detect_group(self, groud_ids):
        deleted_group_ids = []
        r = self.delete_group(groud_ids)
        if r.json()['errcode'] == 40068:
            for group_id in groud_ids:
                if not self.is_group_id_exits(group_id):
                    new_group_id = self.before_add("tmp", [{"name": "test"}])
                    deleted_group_ids.append(new_group_id)
                else:
                    deleted_group_ids.append(group_id)
            r = self.delete_group(deleted_group_ids)
        return r

