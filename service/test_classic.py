import json

import requests


class TestClassic:
    def test_get_token(self):
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={
                "corpid": "ww5025f4943fd0f90a",
                "corpsecret": "sZVwEvsJ5u6-GeJA5lR_TaXbZ-yC2gTNoE4Byg1mLlE"
            }
        )
        print(json.dumps(r.json(), indent=2))
        token = r.json()['access_token']
        print(token)
        return token

    def test_tag_list(self):
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={
                "corpid": "ww5025f4943fd0f90a",
                "corpsecret": "sZVwEvsJ5u6-GeJA5lR_TaXbZ-yC2gTNoE4Byg1mLlE"
            }
        )
        print(json.dumps(r.json(), indent=2))
        token = r.json()['access_token']

        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={"access_token": token},
            json={
                'json': []
            }
        )
        print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

        

