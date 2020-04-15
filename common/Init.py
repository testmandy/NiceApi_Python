# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 15:51
# @Author  : mandy
import pytest

import conftest
from common.compare import Compare
from common.get_url import Url
from common.http_method import HttpMethod
from common.interface import Interface
from utils.opmysql import OperationMySQL


class TestInit(object):
    def setup_class(cls) -> None:
        cls.op = OperationMySQL()
        cls.com = Compare()
        cls.question_pageList_url = Url().get_url(Interface.QUESTION_PAGELIST.value)
        cls.http = HttpMethod()
        cls.header = {"Content-Type": "application/json", "token": conftest.token}
        cls.systemLib_search_url = Url().get_url(Interface.SYSTEMLIB_SEARCH.value)
        cls.core_tablerecord_insert_url = Url().get_url(Interface.CORE_TABLERECORD_INSERT.value)
        print(r"--------------------Before Class--------------------")

    def teardown_class(self) -> None:
        print(r"--------------------After Class--------------------")



