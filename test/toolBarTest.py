# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'toolBarTest.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)

        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        # 设置工具栏中按钮的显示方式为：文字显示在图标的下方
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.addAction(QtGui.QIcon("img1.ico"),"新建") # 为工具栏添加QAction

        # 创建打开按钮对象
        self.open = QtWidgets.QAction(QtGui.QIcon("img1.ico"),"打开")
        # 创建关闭按钮对象
        self.close = QtWidgets.QAction(QtGui.QIcon("img1.ico"),"关闭")
        self.toolBar.addActions([self.open,self.close]) # 将创建的两个QAction到工具栏中
        # 创建一个ComboBox下拉列表控件
        self.combobox = QtWidgets.QComboBox()
        # 定义职位列表
        list = ["总经理","副总经理","主任","员工","财务部经理"]
        self.combobox.addItems(list)
        self.toolBar.addWidget(self.combobox)

        self.toolBar.setIconSize(QtCore.QSize(16,16))

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "文件"))
        self.menu_3.setTitle(_translate("MainWindow", "编辑"))
        self.menu_4.setTitle(_translate("MainWindow", "系统"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

import sys
#程序入口，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()    #创建窗体对象
    ui = Ui_MainWindow()                      #调用PyQt设计的窗体对象
    ui.setupUi(MainWindow)                  #调用PyQt窗体的方法对窗体对象进行初始化
    MainWindow.show()                       #显示窗体
    sys.exit(app.exec_())                   #程序关闭时退出进程
