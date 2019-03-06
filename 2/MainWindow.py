# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(248, 127)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.uniButton = QtWidgets.QPushButton(self.centralwidget)
        self.uniButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.uniButton.setObjectName("uniButton")
        self.binButton = QtWidgets.QPushButton(self.centralwidget)
        self.binButton.setGeometry(QtCore.QRect(140, 10, 75, 23))
        self.binButton.setObjectName("binButton")
        self.geomButton = QtWidgets.QPushButton(self.centralwidget)
        self.geomButton.setGeometry(QtCore.QRect(10, 60, 75, 23))
        self.geomButton.setObjectName("geomButton")
        self.puasButton = QtWidgets.QPushButton(self.centralwidget)
        self.puasButton.setGeometry(QtCore.QRect(140, 60, 75, 23))
        self.puasButton.setObjectName("puasButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.uniButton.setText(_translate("MainWindow", "Uniform"))
        self.binButton.setText(_translate("MainWindow", "Binomial"))
        self.geomButton.setText(_translate("MainWindow", "Geom"))
        self.puasButton.setText(_translate("MainWindow", "Puasson"))


