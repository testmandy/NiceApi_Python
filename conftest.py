# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 15:16
# @Author  : mandy
import logging
import os

project_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(project_dir, 'logs\\')
errorLog_dir = os.path.join(project_dir, 'logs\\syserror.log')
url_dir = os.path.join(project_dir, 'data\\url.properties')
report_dir = os.path.join(project_dir, 'report\\')
screenshots_dir = os.path.join(project_dir, 'screenshots\\')
screenshots_list = os.path.join(project_dir, 'screenshots')
config_dir = os.path.join(project_dir, 'config')
case_dir = os.path.join(project_dir, 'testcases\\test.py')

config = {
    "host": "101.37.82.84",
    "port": 3306,
    "user": "nice_mysql",
    "password": "Mysql2020",
    "database": "test"
}

token = "f83589090d4a7f2773d80c56adfd9602"

def get_logger():
    filename = errorLog_dir
    logging.basicConfig(filename=filename, level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    logger = logging.getLogger(__name__)
    return logger
