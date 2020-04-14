# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 15:51
# @Author  : mandy
import unittest

import conftest
from common.get_url import Url
from common.http_method import HttpMethod
from common.interface import Interface
from utils.opmysql import OperationMySQL


class Init(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.op = OperationMySQL()
        cls.question_pageList_url = Url().get_url(Interface.QUESTION_PAGELIST.value)
        cls.http = HttpMethod()
        cls.header = {"Content-Type": "application/json", "token": conftest.token}
        cls.systemLib_search_url = Url().get_url(Interface.SYSTEMLIB_SEARCH.value)
        print(r"--------------------Before Class--------------------")

    @classmethod
    def tearDown(self) -> None:
        print(r"--------------------After Class--------------------")



