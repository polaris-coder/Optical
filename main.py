# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from PyQt5.Qt import (QWidget, QHBoxLayout, QFrame,
    QSplitter, QStyleFactory, QApplication)
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from Geometric_optics_ui.connectDB import connection
from PyQt5.QtWidgets import *
from Geometric_optics_ui import aberration
from Geometric_optics.main_aberrationAndDistortion import Tool
from Geometric_optics_ui.connectDB import connection
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        # 设置工具栏中按钮的显示方式为：文字显示在图标的下方
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.qaction1 = QtWidgets.QAction(QtGui.QIcon("image/img2.ico"),"点列图") # 创建点列图按钮对象
        self.qaction2 = QtWidgets.QAction(QtGui.QIcon("image/img2.ico"),"像差曲线") # 创建像差曲线按钮对象
        self.qaction3 = QtWidgets.QAction(QtGui.QIcon("image/img2.ico"),"畸变曲线") # 创建畸变曲线按钮对象
        self.qaction4 = QtWidgets.QAction(QtGui.QIcon("image/img2.ico"),"二维光线图") # 创建二维光线图按钮对象
        self.qaction5 = QtWidgets.QAction(QtGui.QIcon("image/img2.ico"),"图像仿真") # 创建图像仿真按钮对象
        # 将创建的QAction添加到工具栏中
        self.toolBar.addActions([self.qaction1,self.qaction2,self.qaction3,self.qaction4,self.qaction5])
        # 设置工具栏按钮的大小
        self.toolBar.setIconSize(QtCore.QSize(20,20))
        # 设置工具栏可以移动
        self.toolBar.setMovable(True)
        # 为工具栏中的QAction绑定triggered信号
        self.toolBar.actionTriggered[QtWidgets.QAction].connect(self.getvalue)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.treeWidget = QtWidgets.QTreeWidget(self.widget)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.verticalLayout_2.addWidget(self.treeWidget)
        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.tabWidget = QtWidgets.QTabWidget(self.widget_3)
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.tabWidget.addTab(self.tab, "")

        # 给self.tab中添加表格
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(5, 5, 1015, 425))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        # self.horizontalLayout_4.addWidget(self.tableWidget)

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.tabWidget_2 = QtWidgets.QTabWidget(self.widget_4)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tabWidget_2.setTabsClosable(True) # 给tab添加删除标志

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget_2.addTab(self.tab_3, "")

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")

        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget_2.addTab(self.tab_5, "")

        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget_2.addTab(self.tab_6, "")

        self.horizontalLayout_3.addWidget(self.tabWidget_2)
        self.verticalLayout.addWidget(self.widget_4)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 2)
        self.horizontalLayout.addWidget(self.widget_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 6)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1165, 23))
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
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        # 实例化QSplitter控件并设置初始为水平方向布局
        splitter1 = QSplitter(Qt.Horizontal)
        # 向Splitter内添加控件,并设定控件初始比例
        splitter1.addWidget(self.widget)
        splitter1.addWidget(self.widget_2)
        splitter1.setStretchFactor(0, 1)
        splitter1.setStretchFactor(1, 12)
        self.horizontalLayout.addWidget(splitter1)
        # 实例化QSplitter控件并设置垂直方向布局
        splitter2 = QSplitter(Qt.Vertical)
        # 向Splitter内添加控件,并设定控件初始比例
        splitter2.addWidget(self.widget_3)
        splitter2.addWidget(self.widget_4)
        splitter2.setStretchFactor(0,3)
        splitter2.setStretchFactor(1,2)
        self.verticalLayout.addWidget(splitter2)

        self.treeWidget.clicked.connect(self.onClicked)

    def onClicked(self):
        item=self.treeWidget.currentItem()
        if item.text(0) == "镜面参数":
            self.connectDB()
        elif item.text(0) == "系统参数":
            self.ui = aberration.Ui_MainWindow() # 创建窗体对象
            self.ui.show() # 显示窗体

    def connectDB(self):
        # 连接数据库，获取数据
        result, row, vol = connection()
        # 将数据填入表格
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(vol)
        self.tableWidget.setHorizontalHeaderLabels(['id', 'Surface Type', 'Radius', 'thickness', 'Refractive index', 'Material'])
        for i in range(row):
            for j in range(vol):
                data = QTableWidgetItem(str(result[i][j]))
                self.tableWidget.setItem(i, j, data)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setAlternatingRowColors(True)

    def getvalue(self,m):

        # 获取数据库中的Lensdata数据
        result, row, vol = connection()

        obj = {'C': 0.0, 't': 10.0, 'n': 1.0}
        surf1 = {'C': 1.0 / 40.94, 't': 8.74, 'n': 1.617}
        surf2 = {'C': 0.0, 't': 11.05, 'n': 1.0}
        surf3 = {'C': -1.0 / 55.65, 't': 2.78, 'n': 1.649}
        surf4 = {'C': 1.0 / 39.75, 't': 7.63, 'n': 1.0}
        surf5 = {'C': 1.0 / 107.56, 't': 9.54, 'n': 1.617}
        surf6 = {'C': -1.0 / 43.33, 't': 0.0, 'n': 1.0}
        img = {'C': 0, 't': 0, 'n': 1.0}
        Lens = [obj, surf1, surf2, surf3, surf4, surf5, surf6, img]

        pupilRadius = 18.5  # 入瞳孔径大小
        pupiltheta = 20  # 最大视场角
        pupilPosition = 4  # 入瞳位置
        # 2. 绘制横向像差点列图
        thetas = np.array([0, 8, 14, 20])  # 视场角
        apertureRays = 18.5  # 光束孔径设置为18.5
        # 3. 绘制径向像差曲线
        apertureRays2 = 2  # 光束孔径设置为2

        if m.text() == "点列图":
            # 绘制点列图
            print("点列图")
            # 创建工具类对象，计算横向像差点列图，径向像差曲线，畸变曲线
            self.tool = Tool(Lens, pupilRadius, pupiltheta, pupilPosition, thetas, apertureRays, apertureRays2)
            self.tool.Ppint_diagram()
            # 在GUI的tabWidget中创建一个布局，用于添加Tool类的实例(实例被看作为一个控件)
            self.gridlayout = QGridLayout(self.tab_3)
            self.gridlayout.addWidget(self.tool, 0, 0)  # 将Tool的实例添加到布局中去
        elif m.text() == "像差曲线":
            # 绘制像差曲线函数
            print("像差曲线")
            # 径向像差曲线
            self.tool_1 = Tool(Lens, pupilRadius, pupiltheta, pupilPosition, thetas, apertureRays, apertureRays2)
            self.tool_1.radial_aberration_curve()
            self.gridlayout_1 = QGridLayout(self.tab_4)
            self.gridlayout_1.addWidget(self.tool_1, 0, 0)
        elif m.text() == "畸变曲线":
            # 绘制畸变曲线
            print("畸变曲线")
            # 畸变曲线
            self.tool_2 = Tool(Lens, pupilRadius, pupiltheta, pupilPosition, thetas, apertureRays, apertureRays2)
            self.tool_2.distortion_curve()
            self.gridlayout_2 = QGridLayout(self.tab_5)
            self.gridlayout_2.addWidget(self.tool_2, 0, 0)
        elif m.text() == "二维光线图":
            # 绘制二维光线图
            print("二维光线图")
            # 光线追迹
            self.tool_3 = Tool(Lens, pupilRadius, pupiltheta, pupilPosition, thetas, apertureRays, apertureRays2)
            self.tool_3.ray_tracing()
            self.gridLayout_3 = QGridLayout(self.tab_6)
            self.gridLayout_3.addWidget(self.tool_3, 0, 0)
        elif m.text() == "图像仿真":
            # 图像仿真
            print("图像仿真")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "光学设计系统"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "参数"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "追迹光学系统"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "镜面参数"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "系统参数"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "新建项目"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "新建子项目"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "新建项目"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "新建子项目"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "新建项目"))
        self.treeWidget.topLevelItem(3).child(0).setText(0, _translate("MainWindow", "新建子项目"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "lensdata1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Tab 1"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Tab 2"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Tab 3"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "Tab 4"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑"))
        self.menu_3.setTitle(_translate("MainWindow", "设置"))
        self.menu_4.setTitle(_translate("MainWindow", "窗口"))
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
