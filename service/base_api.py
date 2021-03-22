import json

import requests


class BaseApi:
    params = {}
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": "ww5025f4943fd0f90a",
                "corpsecret": "sZVwEvsJ5u6-GeJA5lR_TaXbZ-yC2gTNoE4Byg1mLlE"
            }
        }
        # r = requests.get(
        #     'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        #     params={
        #         "corpid": "ww5025f4943fd0f90a",
        #         "corpsecret": "sZVwEvsJ5u6-GeJA5lR_TaXbZ-yC2gTNoE4Byg1mLlE"
        #     }
        # )
        r = self.send(data)
        print(json.dumps(r.json(), indent=2))
        token = r.json()['access_token']
        return token

    def send(self, kwargs):
        # raw_data = json.dumps(kwargs)
        # for key, value in self.params.items():
        #     raw_data = raw_data.replace("${"+key+"}", value)
        # data = json.loads(raw_data)
        r = requests.request(**kwargs)
        return r
