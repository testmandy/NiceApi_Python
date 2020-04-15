# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 14:03
# @Author  : mandy
import os
import pytest

if __name__ == '__main__':
    os.system("py.test testcases/ --alluredir ./result/")
    os.system("allure generate ./result/ -o ./report/ --clean")
    # pytest.main(['-m', '–alluredir report / allure /'])
    print(r"测试报告地址：E:\PycharmProjects\NiceApi_Python\report\index.html")
