# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'materials.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import pymysql
from SR.service import *

from SR.service import queryMaterials

sys.path.append("../")


class Ui_Dialog(QDialog):

    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(925, 530)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.result, self.row, self.vol = queryMaterials()  # 获取数据库中的数据
        self.tableWidget.setRowCount(self.row)
        for i in range(self.row):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 6)
        self.concel = QtWidgets.QPushButton(Dialog)
        self.concel.setObjectName("concel")
        self.gridLayout.addWidget(self.concel, 1, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.determine = QtWidgets.QPushButton(Dialog)
        self.determine.setIconSize(QtCore.QSize(16, 16))
        self.determine.setObjectName("determine")
        self.gridLayout.addWidget(self.determine, 1, 4, 1, 1)
        self.addMaterial = QtWidgets.QPushButton(Dialog)
        self.addMaterial.setObjectName("addMaterial")
        self.gridLayout.addWidget(self.addMaterial, 1, 0, 1, 1)
        self.batch_addition = QtWidgets.QPushButton(Dialog)
        self.batch_addition.setObjectName("batch_addition")
        self.gridLayout.addWidget(self.batch_addition, 1, 1, 1, 1)
        self.save = QtWidgets.QPushButton(Dialog)
        self.save.setObjectName("save")
        self.gridLayout.addWidget(self.save, 1, 2, 1, 1)

        self.tableWidget.verticalHeader().setVisible(False)#隐藏垂直标题
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # 设置窗口的图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/材料库.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)

        self.addMaterial.clicked.connect(self.add_mate)
        self.save.clicked.connect(self.save_mate)
        self.concel.clicked.connect(Dialog.close)
        self.determine.clicked.connect(self.deter)
        self.queryMate()

    #点击确定事件，保存添加的材料，并关闭界面
    def deter(self):
        if self.tableWidget.item(self.tableWidget.rowCount() - 1, 0).text() == "None":
            QMessageBox.information(None,'提示','请输入要添加材料的参数',QMessageBox.Ok)
        else:
            self.queryMate()
            Dialog.close()

    #为表格项添加数据
    def queryMate(self):
        for i in range(self.row):
            for j in range(self.vol):
                data = QTableWidgetItem(str(self.result[i][j]))
                self.tableWidget.setItem(i, j, data)

    #添加材料
    def add_mate(self):
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)

        #设置默认值
        item_material = QTableWidgetItem("None")
        item_K1 = QTableWidgetItem("0.0")
        item_L1 = QTableWidgetItem("0.0")
        item_K2 = QTableWidgetItem("0.0")
        item_L2 = QTableWidgetItem("0.0")
        item_K3 = QTableWidgetItem("0.0")
        item_L3 = QTableWidgetItem("0.0")
        item_nd = QTableWidgetItem("None")
        item_vd = QTableWidgetItem("None")
        self.tableWidget.setItem(rowCount, 0, item_material)
        self.tableWidget.setItem(rowCount, 1, item_K1)
        self.tableWidget.setItem(rowCount, 2, item_L1)
        self.tableWidget.setItem(rowCount, 3, item_K2)
        self.tableWidget.setItem(rowCount, 4, item_L2)
        self.tableWidget.setItem(rowCount, 5, item_K3)
        self.tableWidget.setItem(rowCount, 6, item_L3)
        self.tableWidget.setItem(rowCount, 7, item_nd)
        self.tableWidget.setItem(rowCount, 8, item_vd)

    #删除材料
    def delete_mate(self):
        print("删除材料")

    #批量添加材料
    def add_materials(self):
        print("批量添加材料")

    #保存到数据库
    def save_mate(self):
        n = self.tableWidget.rowCount() - 1
        m = self.tableWidget.columnCount()
        if self.tableWidget.item(n, 0).text() == "None":
            QMessageBox.information(None,'提示','请输入要添加材料的参数',QMessageBox.Ok)
        else:
            self.table_data = []
            for i in range(m):
                if i == 0 or i == m-2 or i == m-1:
                    self.table_data.append(self.tableWidget.item(n,i).text())
                else:
                    self.table_data.append(float(self.tableWidget.item(n,i).text()))
            insertMate(self.table_data)#向数据库中插入数据
            self.queryMate()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "材料库"))
        self.addMaterial.setText(_translate("Dialog", "添加材料"))
        self.batch_addition.setText(_translate("Dialog", "批量添加材料"))
        self.save.setText(_translate("Dialog", "保存"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "SSK4A"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "SF12"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "Sk2"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "SK16"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "F5"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "material"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "K1"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "L1"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "K2"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "L2"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "K3"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "L3"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "nd"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "vd"))
        self.concel.setText(_translate("Dialog", "取  消"))
        self.determine.setText(_translate("Dialog", "确  定"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()    #创建窗体对象
    ui = Ui_Dialog()                    #调用PyQt设计的窗体对象
    ui.setupUi(Dialog)                  #调用PyQt窗体的方法对窗体对象进行初始化
    Dialog.show()                       #显示窗体
    sys.exit(app.exec_())                   #程序关闭时退出进程