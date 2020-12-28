from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

def connection():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123456", "lensdata")
    cursor = db.cursor()
    cursor.execute("select * from lensdata1")
    result = cursor.fetchall()
    row = cursor.rowcount
    vol = len(result[0])
    cursor.close()
    db.close()
    return result, row, vol
