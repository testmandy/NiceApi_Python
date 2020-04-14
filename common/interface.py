# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 15:40
# @Author  : mandy
# 导入枚举类
from enum import Enum


# 继承枚举类
class Interface(Enum):
    SYSTEMLIB_SEARCH = 'systemLib_search_uri'
    QUESTION_PAGELIST = 'question_pageList_uri'
    # 注意BROWN的值和YELLOW的值相同，这是允许的，此时的BROWN相当于YELLOW的别名
    RED = 2
    GREEN = 3
    PINK = 4

