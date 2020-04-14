# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 14:07
# @Author  : mandy
import json
import unittest
import pytest
from common.Init import TestInit


class TestSystemLib(TestInit):
    def test_01(self):
        print("-----------------------------------test01 is running now---------------------------------")

    def test_systemLib_search(cls):
        print(r'请求地址：%s' % cls.systemLib_search_url)
        data = {"table_name": "nice_question_lib_system_book", "condition": []}
        res = cls.http.main('post', cls.systemLib_search_url, json.dumps(data), cls.header)
        res = json.loads(res)
        actual = res['data'][0]['id']
        print(r'第一个data下的id为：%s' % str(actual))
        statement = "select * from course"
        expect = cls.op.select(statement)
        assert actual in expect

    def test_question_pageList(cls):
        print(r'请求地址：%s' % cls.question_pageList_url)
        data = {"page.currPage": 1, "page.pageSize": 10, "vo.id": 3}
        res = cls.http.main('post', cls.question_pageList_url, data, cls.header)
        res = json.loads(res)
        actual = res['code']
        assert actual == 500


if __name__ == '__main__':
    pytest.main()

