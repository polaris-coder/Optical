# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableTest.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(893, 698)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(9, 9, 551, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(7)
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
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
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

        # self.lineEdit = QtWidgets.QLineEdit()
        # # self.lineEdit.setText("aqwe")
        # self.lineEdit.setObjectName("lineEdit")
        # self.tableWidget.setCellWidget(0, 0, self.lineEdit)
        self.tableWidget.itemChanged.connect(self.leave)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def leave(self):
        print("鼠标离开")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "新建行"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "新建行"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "新建行"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "新建行"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "新建行"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "新建行"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "新建行"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "新建列"))

import sys
#程序入口，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()    #创建窗体对象
    ui = Ui_Dialog()                    #调用PyQt设计的窗体对象
    ui.setupUi(Dialog)                  #调用PyQt窗体的方法对窗体对象进行初始化
    Dialog.show()                       #显示窗体
    sys.exit(app.exec_())                   #程序关闭时退出进程
