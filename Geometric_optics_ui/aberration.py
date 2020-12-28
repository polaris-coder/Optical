# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xiangcha2.ui'
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
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMainWindow, QGridLayout
from Geometric_optics import drawDiagram
import numpy as np
from Geometric_optics.main_aberrationAndDistortion import Tool
import time
from Geometric_optics_ui.connectDB import connection


class Ui_MainWindow(QMainWindow):

    #构造
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        # self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint) # 只显示最小化和关闭按钮
        self.setupUi(self) # 初始化窗体设置

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 850)
        font = QtGui.QFont()
        font.setPointSize(5)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")

        self.widget_3 = QtWidgets.QWidget(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.widget_3.setFont(font)
        self.widget_3.setObjectName("widget_3")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setContentsMargins(1, 5, 1, 1)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.groupBox = QtWidgets.QGroupBox(self.widget_3)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.tabWidget = QtWidgets.QTabWidget(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.widget_4)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 3)
        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setContentsMargins(1, 5, 1, 1)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 181, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 5, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 7, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 8, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 6, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 9, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.horizontalLayout.addWidget(self.widget_2)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        # 实例化QSplitter控件并设置初始为水平方向布局
        splitter1 = QSplitter(Qt.Horizontal)
        # 向Splitter内添加控件,并设定控件初始比例
        splitter1.addWidget(self.widget)
        splitter1.addWidget(self.widget_2)
        splitter1.setStretchFactor(0, 2)
        splitter1.setStretchFactor(1, 1)
        self.horizontalLayout.addWidget(splitter1)
        # 实例化QSplitter控件并设置垂直方向布局
        splitter2 = QSplitter(Qt.Vertical)
        # 向Splitter内添加控件,并设定控件初始比例
        splitter2.addWidget(self.widget_3)
        splitter2.addWidget(self.widget_4)
        splitter2.setStretchFactor(0, 3)
        splitter2.setStretchFactor(1, 4)
        self.verticalLayout.addWidget(splitter2)

        self.pushButton.clicked.connect(self.compute1)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def compute1(self):
        start = time.time()
        # 获取数据库中的镜面数据
        result, row, vol = connection()
        # 1. 初始化光学系统

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
        thetas = np.array([0, 8, 14, 20]) # 视场角
        apertureRays = 18.5  # 光束孔径设置为18.5
        # 3. 绘制径向像差曲线
        apertureRays2 = 2  # 光束孔径设置为2

        # 创建工具类对象，计算横向像差点列图，径向像差曲线，畸变曲线
        self.tool=Tool(Lens,pupilRadius,pupiltheta,pupilPosition,thetas,apertureRays,apertureRays2)
        self.tool.Ppint_diagram()
        # 在GUI的tabWidget中创建一个布局，用于添加Tool类的实例(实例被看作为一个控件)
        self.gridlayout = QGridLayout(self.tab)
        self.gridlayout.addWidget(self.tool,0,0) # 将Tool的实例添加到布局中去
        # 径向像差曲线
        self.tool_1 = Tool(Lens, pupilRadius, pupiltheta, pupilPosition, thetas, apertureRays,apertureRays2)
        self.tool_1.radial_aberration_curve()
        self.gridlayout_1 = QGridLayout(self.tab_2)
        self.gridlayout_1.addWidget(self.tool_1,0,0)
        # 畸变曲线
        self.tool_2 = Tool(Lens, pupilRadius, pupiltheta, pupilPosition, thetas, apertureRays,apertureRays2)
        self.tool_2.distortion_curve()
        self.gridlayout_2 = QGridLayout(self.tab_3)
        self.gridlayout_2.addWidget(self.tool_2, 0, 0)
        # 光线追迹
        self.tool_3 = Tool(Lens, pupilRadius, pupiltheta, pupilPosition, thetas, apertureRays, apertureRays2)
        self.tool_3.ray_tracing()
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.addWidget(self.tool_3,0,0)

        end = time.time()
        print('aberration', end - start)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "追迹并可视化光学系统的像差"))
        self.groupBox.setTitle(_translate("MainWindow", "光线追迹示意图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "横向像差点列图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "径向像差曲线"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "畸变曲线"))
        self.groupBox_2.setTitle(_translate("MainWindow", "光学系统参数"))
        self.label.setText(_translate("MainWindow", "入瞳孔径"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>光束孔径</p><p>(径向像差)</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>光束孔径</p><p>(横向像差)</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "视场角"))
        self.label_3.setText(_translate("MainWindow", "入瞳位置"))
        self.label_2.setText(_translate("MainWindow", "最大视场角"))
        self.pushButton.setText(_translate("MainWindow", "计算"))


import sys
#程序入口，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()    #创建窗体对象
    ui = Ui_MainWindow()                      #调用PyQt设计的窗体对象
    ui.setupUi(MainWindow)                  #调用PyQt窗体的方法对窗体对象进行初始化
    MainWindow.show()                       #显示窗体
    sys.exit(app.exec_())                   #程序关闭时退出进程
