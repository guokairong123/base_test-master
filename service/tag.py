import json

import requests


class Tag:

    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={
                "corpid": "ww5025f4943fd0f90a",
                "corpsecret": "sZVwEvsJ5u6-GeJA5lR_TaXbZ-yC2gTNoE4Byg1mLlE"
            }
        )
        print(json.dumps(r.json(), indent=2))
        token = r.json()['access_token']
        return token

    def add(self, group_name, tag, **kwargs):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            params={"access_token": self.token},
            json={
                "group_name": group_name,
                "tag": tag,
                **kwargs
            }
        )
        print(json.dumps(r.json(), indent=2))
        assert r.json()['errcode'] == 0
        assert r.status_code == 200
        return r

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
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    def delete_tag(self, tag_id):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={"access_token": self.token},
            json={
                "tag_id": tag_id
            }
        )
        assert r.status_code == 200
        assert r.json()['errcode'] == 0