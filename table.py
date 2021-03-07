# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(676, 548)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(50, 50, 551, 191))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
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

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("1")
        self.comboBox.addItem("2")
        self.comboBox.addItem("3")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        # self.gridLayout.addWidget(self.lineEdit)

        self.tableWidget.setCellWidget(1,1,self.comboBox)
        # self.tableWidget.setCellWidget(1,1,self.lineEdit)

        # self.gridLayout = QtWidgets.QGridLayout(self.tableWidget.item(1,1))
        # self.gridLayout.setContentsMargins(0, 0, 0, 0)
        # self.gridLayout.setSpacing(0)
        # self.gridLayout.setObjectName("gridLayout")
        #

        #
        # self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        # self.lineEdit_3.setObjectName("lineEdit_3")
        # self.gridLayout.addWidget(self.lineEdit_3, 0, 0, 1, 1)


        # self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 1)
        # self.gridLayout.setColumnStretch(0, 1)
        # self.gridLayout.setColumnStretch(1, 2)
        # self.gridLayout.setColumnStretch(2, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

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

        # self.comboBox.setItemText(0, _translate("Dialog", "1"))
        # self.comboBox.setItemText(1, _translate("Dialog", "2"))
        # self.comboBox.setItemText(2, _translate("Dialog", "3"))

import sys
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()    #创建窗体对象
    ui = Ui_Dialog()                    #调用PyQt设计的窗体对象
    ui.setupUi(Dialog)                  #调用PyQt窗体的方法对窗体对象进行初始化
    Dialog.show()                       #显示窗体
    sys.exit(app.exec_())                   #程序关闭时退出进程
