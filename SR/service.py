from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


# 打开数据库连接
def open():
    db = pymysql.connect("localhost", "root", "123456", "lensdata")
    return db

# 获取Lensdata2数据
def connection():
    sql = "select `Surface Type`,`Radius`,`thickness`,`Refractive index`,`Material` from lensdata2"
    db = open() # 连接数据库
    cursor = db.cursor() # 使用cursor()方法获取操作游标
    cursor.execute(sql) # 执行查询SQL语句
    result = cursor.fetchall() # 记录查询结果
    row = cursor.rowcount
    vol = len(result[0])
    cursor.close() # 关闭游标
    db.close() # 关闭数据库连接
    return result, row, vol # 返回查询结果

#获取lensdata3的数据
def getLensdata3():
    sql = "select `Surface Type`,`Radius`,`thickness`,`Refractive index`,`Material` from lensdata3"
    db = open()  # 连接数据库
    cursor = db.cursor()  # 使用cursor()方法获取操作游标
    cursor.execute(sql)  # 执行查询SQL语句
    result = cursor.fetchall()  # 记录查询结果
    row = cursor.rowcount
    vol = len(result[0])
    cursor.close()  # 关闭游标
    db.close()  # 关闭数据库连接
    return result, row, vol  # 返回查询结果

#获取materials的数据
def queryMaterials():
    sql = "select `material`,`K1`,`L1`,`K2`,`L2`,`K3`,`L3`,`nd`,`vd` from materials"
    db = open()  # 连接数据库
    cursor = db.cursor()  # 使用cursor()方法获取操作游标
    cursor.execute(sql)  # 执行查询SQL语句
    result = cursor.fetchall()  # 记录查询结果
    row = cursor.rowcount
    vol = len(result[0])
    cursor.close()  # 关闭游标
    db.close()  # 关闭数据库连接
    return result, row, vol  # 返回查询结果

#查询表lensdata3的记录数
def queryCoun():
    sql = "select count(*) from lensdata3"
    db = open()  # 连接数据库
    cursor = db.cursor()  # 使用cursor()方法获取操作游标
    cursor.execute(sql)  # 执行查询SQL语句
    result = cursor.fetchall()  # 记录查询结果
    count = result[0][0]
    return count

#向lensdata3中插入数据
def insertLen3(data,row):
    count = queryCoun()
    if(count < 8):
        for i in range(row):
            sql = "insert into lensdata3(`Radius`,`thickness`,`Refractive index`,`Material`) values (%s,%s,%s,%s)"
            exec(sql,(data[i][0],data[i][1],data[i][2],data[i][3]))

#将修改后的表格数据保存到数据库中
def updateLen3(data,row):
    for i in range(row):
        sql = "update lensdata3 set `Radius`=%s,`thickness`=%s,`Refractive index`=%s,`Material`=%s where `id`=%s";
        exec(sql,(data[i][0],data[i][1],data[i][2],data[i][3],i+1))

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

#向materials中插入数据
def insertMate(data):
    sql = "insert into materials(`material`,`K1`,`L1`,`K2`,`L2`,`K3`,`L3`,`nd`,`vd`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    exec(sql, (data[0], data[1], data[2], data[3], data[4],data[5], data[6], data[7], data[8]))
