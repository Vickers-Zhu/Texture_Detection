# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Prediction_UI.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindowLuoandZhu")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.importImage.setText(_translate("MainWindow", "Import"))
        self.predict.setText(_translate("MainWindow", "Predict"))


