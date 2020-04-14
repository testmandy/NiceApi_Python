# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 14:58
# @Author  : mandy
import pytest

from common.interface import Interface
from utils.properties import Properties


class Url:
    def __init__(self):
        self.prop = Properties()

    def read(self, key):
        base_url = self.prop.get('base_url')
        uri = self.prop.get(key)
        url = base_url + uri
        return url

    def get_url(self, key):
        if key == Interface.SYSTEMLIB_SEARCH.value:
            return self.read(Interface.SYSTEMLIB_SEARCH.value)
        if key == Interface.QUESTION_PAGELIST.value:
            return self.read(Interface.QUESTION_PAGELIST.value)


# if __name__ == '__main__':
#     url = Url().get_url(Interface.SYSTEMLIBSEARCH.value)
#     print(Interface.SYSTEMLIBSEARCH.value)
#     print(url)
