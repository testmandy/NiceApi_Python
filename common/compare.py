# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 14:16
# @Author  : mandy
from utils.opmysql import OperationMySQL


class Compare:
    def __init__(self):
        self.op = OperationMySQL()

    def compare_code(self, res_json):
        res_code = res_json['code']
        assert res_code == 0

    def compare_msg(self, res_json):
        res_msg = res_json['msg']
        assert res_msg == 'success'

    def compare_insert_id(self, res_json, table_name):
        res_id = res_json['data'][0]['list'][0]['id']
        print(r'插入数据id为：%s' % str(res_id))
        stmt = "select id from " + table_name + " order by id desc"
        expect = self.op.select(stmt)
        expect_id = expect[0]
        print(r'表查询id为：%s' % str(expect_id))
        assert expect_id == res_id
        # 删除插入的测试数据
        # if expect_id == res_id:
        #     self.op.delete_one_by_id(res_id, table_name)

