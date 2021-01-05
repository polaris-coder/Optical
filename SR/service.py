from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


# 打开数据库连接
def open():
    db = pymysql.connect("localhost", "root", "123456", "lensdata")
    return db

# 获取Lensdata2数据
def connection(sql, *keys):
    db = open() # 连接数据库
    cursor = db.cursor() # 使用cursor()方法获取操作游标
    cursor.execute(sql) # 执行查询SQL语句
    result = cursor.fetchall() # 记录查询结果
    row = cursor.rowcount
    vol = len(result[0])
    cursor.close() # 关闭游标
    db.close() # 关闭数据库连接
    return result, row, vol # 返回查询结果

# 执行数据的增删改操作
def exec(sql, values):
    db = open() # 连接数据库
    cursor = db.cursor()
    try:
        cursor.execute(sql, values) # 执行增删改的SQL语句
        db.commit() # 提交数据
        return 1 # 执行成功
    except:
        db.rollback() # 发生错误时回滚
        return 0 # 执行失败
    finally:
        cursor.close() # 关闭游标
        db.close() # 关闭数据库连接
