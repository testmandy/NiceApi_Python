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
    "database": "renren_fast"
}


token = "eb944a0d61c45c54b9f9e4f9344ff1ee"

def get_logger():
    filename = errorLog_dir
    logging.basicConfig(filename=filename, level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    logger = logging.getLogger(__name__)
    return logger


data = [
  {
    "list": [
      {
        "subject": 72,
        "volume": 42,
        "textbook_version": 261,
        "question_type": 298,
        "sub_type":0,
        "body": "填空含答案,选择题含选项",
        "solution": "{}",
        "analysis": "",
        "level": 1,
        "solve_type": 308,
        "classify": 312,
        "label1":1,
        "label2":2,
        "label3":3,
        "label4":4,
        "label5":5,
        "sub_flag":0,
        "file_path": "",
        "explain_path": "",
        "status": 314,
        "private_flag": 321,
        "process_status": 324,
        "reference_and_question":[
            {
              "node_id":37
            }
          ]
      }
    ],
    "table_name": "nice_question_lib_question"
  }
]
