# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 13:58
# @Author  : mandy
import pymysql
import conftest


class OperationMySQL:
    def __init__(self,):
        try:
            self.db = pymysql.connect(**conftest.config)
        except pymysql.Error as e:
            print(r'连接数据库失败|Mysql Error %d : %s' % (e.args[0], e.args[1]))
            conftest.get_logger().exception(e)
        else:
            self.cursor = self.db.cursor()

    def select(self, statement):
        sql = "select * from course"
        try:
            self.cursor.execute(statement)
        except AttributeError as e:
            print(r'SQL执行失败|Error : %s' % (e.args[0]))
            conftest.get_logger().exception(e)
        else:
            row_one = self.cursor.fetchone()
            rows = self.cursor.fetchall()
            # print(r'查询的单行数据为：%s' % str(row_one))
            self.close()
            return row_one

    def insert(self, statement):
        sql = "select * from course"
        effect_row = self.cursor.execute(statement)
        self.db.commit()  # 提交数据
        print(effect_row)
        row_one = self.cursor.fetchone()
        print(row_one)
        self.close()

    def update(self, statement):
        sql = "select * from course"
        effect_row = self.cursor.execute(statement)
        self.db.commit()  # 提交数据
        print(effect_row)
        row_one = self.cursor.fetchone()
        print(row_one)
        self.close()

    def delete_one_by_id(self, id, table_name):
        stmt = "DELETE FROM " + table_name + " WHERE id= " + id
        effect_row = self.cursor.execute(stmt)
        self.db.commit()  # 提交数据
        print(effect_row)
        self.close()

    def close(self):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    op = OperationMySQL()
    op.select()

