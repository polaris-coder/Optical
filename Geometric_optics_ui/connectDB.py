from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

# 获取Lensdata2前5列数据
def connection():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123456", "lensdata")
    cursor = db.cursor()
    cursor.execute("select `Surface Type`,`Radius`,`thickness`,`Refractive index`,`Material` from lensdata2")
    result = cursor.fetchall()
    row = cursor.rowcount
    vol = len(result[0])
    cursor.close()
    db.close()
    return result, row, vol

# 获取Lensdata2所有列数据
def connection2():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123456", "lensdata")
    cursor = db.cursor()
    cursor.execute("select * from lensdata2")
    result = cursor.fetchall()
    row = cursor.rowcount
    vol = len(result[0])
    cursor.close()
    db.close()
    return result, row, vol