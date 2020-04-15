# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 11:19
# @Author  : mandy
import json

import conftest
from common.Init import TestInit


class TestQuestionLib(TestInit):
    def test_question_lib_add_question(cls):
        print("-----------------------------------test is running now---------------------------------")
        table_name = "nice_question_lib_question"
        print(r'接口请求地址：%s' % cls.core_tablerecord_insert_url)
        data = conftest.data
        res = cls.http.main('post', cls.core_tablerecord_insert_url, json.dumps(data), cls.header)
        res_json = json.loads(res)
        print(r'接口请求结果为：%s' % str(res))
        cls.com.compare_code(res_json)
        cls.com.compare_msg(res_json)
        cls.com.compare_insert_id(res_json, table_name)



