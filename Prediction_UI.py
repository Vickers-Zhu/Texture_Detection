# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Prediction_UI.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LuoAndZhu(object):
    def setupUi(self, LuoAndZhu):
        LuoAndZhu.setObjectName("LuoAndZhu")
        LuoAndZhu.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(LuoAndZhu)
        self.centralwidget.setObjectName("centralwidget")
        self.originalVIew = QtWidgets.QGraphicsView(self.centralwidget)
        self.originalVIew.setGeometry(QtCore.QRect(20, 0, 320, 280))
        self.originalVIew.setObjectName("originalVIew")
        self.importImage = QtWidgets.QPushButton(self.centralwidget)
        self.importImage.setGeometry(QtCore.QRect(230, 410, 111, 32))
        self.importImage.setObjectName("importImage")
        self.predict = QtWidgets.QPushButton(self.centralwidget)
        self.predict.setGeometry(QtCore.QRect(470, 410, 111, 32))
        self.predict.setObjectName("predict")
        self.labeledView = QtWidgets.QGraphicsView(self.centralwidget)
        self.labeledView.setGeometry(QtCore.QRect(460, 0, 320, 280))
        self.labeledView.setObjectName("labeledView")
        LuoAndZhu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LuoAndZhu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        LuoAndZhu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LuoAndZhu)
        self.statusbar.setObjectName("statusbar")
        LuoAndZhu.setStatusBar(self.statusbar)

        self.retranslateUi(LuoAndZhu)
        QtCore.QMetaObject.connectSlotsByName(LuoAndZhu)

    def retranslateUi(self, LuoAndZhu):
        _translate = QtCore.QCoreApplication.translate
        LuoAndZhu.setWindowTitle(_translate("LuoAndZhu", "LuoAndZhu"))
        self.importImage.setText(_translate("LuoAndZhu", "Import"))
        self.predict.setText(_translate("LuoAndZhu", "Predict"))


