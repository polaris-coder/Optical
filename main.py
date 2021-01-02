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
from PyQt5.QtWidgets import *
from Geometric_optics.main_aberrationAndDistortion import Tool
from Geometric_optics_ui.connectDB import connection, connection2
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 1000)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        # 设置工具栏中按钮的显示方式为：文字显示在图标的下方
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.qaction1 = QtWidgets.QAction(QtGui.QIcon("image/img2.ico"),"二维光线图") # 创建点列图按钮对象
        self.qaction2 = QtWidgets.QAction(QtGui.QIcon("image/img2.ico"),"像差曲线") # 创建像差曲线按钮对象
        self.qaction3 = QtWidgets.QAction(QtGui.QIcon("image/img2.ico"),"畸变曲线") # 创建畸变曲线按钮对象
        self.qaction4 = QtWidgets.QAction(QtGui.QIcon("image/img2.ico"),"点列图") # 创建二维光线图按钮对象
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
        self.verticalLayout_2.setContentsMargins(3, 6, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # 主界面左侧参数栏，添加ToolBox控件
        self.toolBox = QtWidgets.QToolBox(self.widget)
        self.toolBox.setObjectName("toolBox")

        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_4.setContentsMargins(-1, 3, -1, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_6 = QtWidgets.QLabel(self.page_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self.page_4)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 1, 1, 1, 1)

        self.lineEdit_12 = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_4.addWidget(self.lineEdit_12, 0, 1, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 2, 0, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 2, 1, 1, 1)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem3, 3, 1, 1, 1)
        self.toolBox.addItem(self.page_4, "")

        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 166, 180))
        self.page.setObjectName("page")
        self.gridLayout = QtWidgets.QGridLayout(self.page)
        self.gridLayout.setContentsMargins(-1, 3, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.page)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.toolBox.addItem(self.page, "")

        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 166, 180))
        self.page_2.setObjectName("page_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_2.setContentsMargins(-1, 3, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 3, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 5, 1, 1, 1)
        self.toolBox.addItem(self.page_2, "")

        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_3.setContentsMargins(-1, 3, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_3.addWidget(self.lineEdit_7, 0, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_3.addWidget(self.lineEdit_8, 1, 1, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_3.addWidget(self.lineEdit_9, 2, 1, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_3.addWidget(self.lineEdit_10, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 4, 1, 1, 1)
        self.toolBox.addItem(self.page_3, "")

        self.verticalLayout_2.addWidget(self.toolBox)

        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)
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
        self.tableWidget.setGeometry(QtCore.QRect(5, 5, 1150, 390))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['Surface Type', 'Radius', 'thickness', 'Refractive index', 'Material']) # 设置表格中的水平标题

        for row in range (0, self.tableWidget.rowCount()) :
            self.addComboBox(row)

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
        self.toolBox.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        # 实例化QSplitter控件并设置初始为水平方向布局
        splitter1 = QSplitter(Qt.Horizontal)
        # 向Splitter内添加控件,并设定控件初始比例
        splitter1.addWidget(self.widget)
        splitter1.addWidget(self.widget_2)
        splitter1.setStretchFactor(0, 2)
        splitter1.setStretchFactor(1, 12)
        self.horizontalLayout.addWidget(splitter1)
        # 实例化QSplitter控件并设置垂直方向布局
        splitter2 = QSplitter(Qt.Vertical)
        # 向Splitter内添加控件,并设定控件初始比例
        splitter2.addWidget(self.widget_3)
        splitter2.addWidget(self.widget_4)
        splitter2.setStretchFactor(0,2)
        splitter2.setStretchFactor(1,2)
        self.verticalLayout.addWidget(splitter2)

        self.pushButton.clicked.connect(self.connectDB)
        self.pushButton_2.clicked.connect(self.table_insert)
        self.pushButton_3.clicked.connect(self.table_delete)

    # 增加表格的列
    def table_insertVol(self):
        print(self.comobox.currentIndex())
        column = self.tableWidget.columnCount()
        for i in range (0,6) :
            self.tableWidget.insertColumn(column)
        self.tableWidget.setHorizontalHeaderLabels(
                    ['Surface Type', 'Radius', 'thickness', 'Refractive index', 'Material', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6'])  # 设置表格中的水平标题

    # 删除表格的某一行
    def table_delete(self):
        row_select = self.tableWidget.selectedItems()
        if len(row_select) == 0:
            return

        row = row_select[0].row()
        self.tableWidget.removeRow(row)

    # 表格增加一行
    def table_insert(self):
        # rowCount()获取现有表格控件中的行数,在此基础上插入一行insertRow()
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        self.addComboBox(row)

    def addComboBox(self, row):
        # 将表格第1列设置为ComboBox下拉列表
        self.comobox = QComboBox()
        self.comobox.addItems(['Standard', 'sphere', 'asphere', 'extended polynomial'])  # 为下拉列表设置数据源
        self.comobox.setCurrentIndex(0)  # 默认选中第一项
        self.tableWidget.setCellWidget(row, 0, self.comobox)  # 将创建的下拉列表显示在表格中

        item_Radius = QTableWidgetItem("0.0")
        item_thickness = QTableWidgetItem("0.0")
        item_Refractive_index = QTableWidgetItem("0.0")
        item_Material = QTableWidgetItem("None")
        item_r1 = QTableWidgetItem("0.0")
        item_r2 = QTableWidgetItem("0.0")
        item_r3 = QTableWidgetItem("0.0")
        item_r4 = QTableWidgetItem("0.0")
        item_r5 = QTableWidgetItem("0.0")
        item_r6 = QTableWidgetItem("0.0")
        # 设置单元格中的内容
        self.tableWidget.setItem(row, 1, item_Radius)
        self.tableWidget.setItem(row, 2, item_thickness)
        self.tableWidget.setItem(row, 3, item_Refractive_index)
        self.tableWidget.setItem(row, 4, item_Material)
        self.tableWidget.setItem(row, 5, item_r1)
        self.tableWidget.setItem(row, 6, item_r2)
        self.tableWidget.setItem(row, 7, item_r3)
        self.tableWidget.setItem(row, 8, item_r4)
        self.tableWidget.setItem(row, 9, item_r5)
        self.tableWidget.setItem(row, 10, item_r6)

        # self.comobox.currentIndexChanged.connect(self.connectDB2)

        self.tableWidget.resizeColumnsToContents()  # 使表格列的宽度跟随内容改变
        self.tableWidget.resizeRowsToContents()  # 使表格行的高度跟随内容改变

    # 连接数据库并获取数据
    def connectDB(self):
        # 连接数据库，获取数据
        result, row, vol = connection()
        # 将数据填入表格
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(vol)
        # self.tableWidget.setHorizontalHeaderLabels(
        #         ['Surface Type', 'Radius', 'thickness', 'Refractive index', 'Material', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6'])  # 设置表格中的水平标题
        # self.tableWidget.setHorizontalHeaderLabels(['Surface Type', 'Radius', 'thickness', 'Refractive index', 'Material']) # 设置表格中的水平标题
        for i in range(row):
            for j in range(vol):
                # 为表格第一列的单元格添加下拉菜单
                if j == 0:
                    self.comobox = QComboBox()
                    self.comobox.addItems(['Standard', 'sphere','asphere','extended polynomial'])
                    self.comobox.setCurrentIndex(0)
                    self.tableWidget.setCellWidget(i,0,self.comobox)
                else:
                    data = QTableWidgetItem(str(result[i][j]))
                    self.tableWidget.setItem(i, j, data)
                # data.setForeground(QtGui.QBrush(QtGui.QColor("gray"))) # 设置单元格的文本颜色
                # data.setBackground(QtGui.QBrush(QtGui.QColor("gray"))) # 设置单元格背景颜色
        # self.tableWidget.setAlternatingRowColors(True) # 设置表格颜色交错显示

    # 连接数据库并获取数据
    def connectDB2(self):
        # 连接数据库，获取数据
        result, row, vol = connection2()
        # 将数据填入表格
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(vol)
        self.tableWidget.setHorizontalHeaderLabels(
                ['Surface Type', 'Radius', 'thickness', 'Refractive index', 'Material', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6'])  # 设置表格中的水平标题
        # self.tableWidget.setHorizontalHeaderLabels(['Surface Type', 'Radius', 'thickness', 'Refractive index', 'Material']) # 设置表格中的水平标题
        for i in range(row):
            for j in range(vol):
                # 为表格第一列的单元格添加下拉菜单
                if j == 0:
                    self.comobox = QComboBox()
                    self.comobox.addItems(['Standard', 'sphere','asphere','extended polynomial'])
                    self.comobox.setCurrentIndex(0)
                    self.tableWidget.setCellWidget(i,0,self.comobox)
                    self.comobox.currentIndexChanged.connect(self.table_insertVol)
                else:
                    data = QTableWidgetItem(str(result[i][j]))
                    self.tableWidget.setItem(i, j, data)
                # data.setForeground(QtGui.QBrush(QtGui.QColor("gray"))) # 设置单元格的文本颜色
                # data.setBackground(QtGui.QBrush(QtGui.QColor("gray"))) # 设置单元格背景颜色
        # self.tableWidget.setAlternatingRowColors(True) # 设置表格颜色交错显示

    # 为工具栏中的控件绑定槽函数
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
            # 创建工具类对象，计算横向像差点列图，径向像差曲线，畸变曲线
            self.tool = Tool(Lens, pupilRadius, pupiltheta, pupilPosition, thetas, apertureRays, apertureRays2)
            self.tool.Ppint_diagram()
            # 在GUI的tabWidget中创建一个布局，用于添加Tool类的实例(实例被看作为一个控件)
            self.gridlayout = QGridLayout(self.tab_6)
            self.gridlayout.addWidget(self.tool, 0, 0,QtCore.Qt.AlignCenter)  # 将Tool的实例添加到布局中去
        elif m.text() == "像差曲线":
            # 绘制像差曲线函数
            self.tool_1 = Tool(Lens, pupilRadius, pupiltheta, pupilPosition, thetas, apertureRays, apertureRays2)
            self.tool_1.radial_aberration_curve()
            self.gridlayout_1 = QGridLayout(self.tab_4)
            self.gridlayout_1.addWidget(self.tool_1, 0, 0,QtCore.Qt.AlignCenter)
        elif m.text() == "畸变曲线":
            # 绘制畸变曲线
            self.tool_2 = Tool(Lens, pupilRadius, pupiltheta, pupilPosition, thetas, apertureRays, apertureRays2)
            self.tool_2.distortion_curve()
            self.gridlayout_2 = QGridLayout(self.tab_5)
            self.gridlayout_2.addWidget(self.tool_2, 0, 0,QtCore.Qt.AlignCenter)
        elif m.text() == "二维光线图":
            # 绘制二维光线图
            self.tool_3 = Tool(Lens, pupilRadius, pupiltheta, pupilPosition, thetas, apertureRays, apertureRays2)
            self.tool_3.ray_tracing()
            self.gridLayout_3 = QGridLayout(self.tab_3)
            self.gridLayout_3.addWidget(self.tool_3, 0, 0,QtCore.Qt.AlignCenter)
        elif m.text() == "图像仿真":
            # 图像仿真
            print("图像仿真")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "光学设计系统"))

        self.label_5.setText(_translate("MainWindow", "入瞳位置："))
        self.label.setText(_translate("MainWindow", "入瞳孔径："))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "入瞳孔径与位置"))
        self.label_3.setText(_translate("MainWindow", "视场角："))
        self.label_2.setText(_translate("MainWindow", "最大视场角："))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "视场角"))
        self.label_4.setText(_translate("MainWindow", "波长："))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "波长"))
        self.label_6.setText(_translate("MainWindow", "镜面个数："))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton_2.setText(_translate("MainWindow", "添加"))
        self.pushButton_3.setText(_translate("MainWindow", "删除"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("MainWindow", "Lensdata"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "lensdata1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "二维光线图"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "像差曲线"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "畸变曲线"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "点列图"))
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
