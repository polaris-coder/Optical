# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'materials.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys

from SR.service import queryMaterials

sys.path.append("../")


class Ui_Dialog(QDialog):

    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(726, 230)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
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
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 4)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)

        self.tableWidget.verticalHeader().setVisible(False)#隐藏垂直标题

        #为表格项添加数据
        result,row,vol = queryMaterials()#获取数据库中的数据
        for i in range(row):
            for j in range(vol):
                data = QTableWidgetItem(str(result[i][j]))
                self.tableWidget.setItem(i, j, data)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "材料库"))
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
        self.pushButton_2.setText(_translate("Dialog", "取  消"))
        self.pushButton.setText(_translate("Dialog", "确  定"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()    #创建窗体对象
    ui = Ui_Dialog()                    #调用PyQt设计的窗体对象
    ui.setupUi(Dialog)                  #调用PyQt窗体的方法对窗体对象进行初始化
    Dialog.show()                       #显示窗体
    sys.exit(app.exec_())                   #程序关闭时退出进程
