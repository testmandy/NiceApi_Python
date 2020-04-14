# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 14:29
# @Author  : mandy
import json
import requests


class HttpMethod:
    def get(self, url, param=None, headers=None):
        res = requests.get(url=url, params=param, headers=headers).json()
        res = json.dumps(res, indent=2)
        return res

    def post(self, url, data, headers=None):
        res = requests.post(url=url, data=data, headers=headers).json()
        print(res)
        res = json.dumps(res, indent=2)
        return res

    def main(self, method, url, param=None, headers=None):
        if method == 'get':
            res = self.get(url, param, headers)
        else:
            res = self.post(url, param, headers)
        return res


