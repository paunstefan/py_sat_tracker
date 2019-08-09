# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 240)
        MainWindow.setMinimumSize(QtCore.QSize(650, 240))
        MainWindow.setMaximumSize(QtCore.QSize(650, 240))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/FP_Satellite_icon.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnAddLocation = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddLocation.setGeometry(QtCore.QRect(10, 40, 291, 26))
        self.btnAddLocation.setObjectName("btnAddLocation")
        self.tbLocation = QtWidgets.QComboBox(self.centralwidget)
        self.tbLocation.setGeometry(QtCore.QRect(10, 70, 291, 27))
        self.tbLocation.setObjectName("tbLocation")
        self.tbTle = QtWidgets.QLineEdit(self.centralwidget)
        self.tbTle.setGeometry(QtCore.QRect(360, 70, 281, 27))
        self.tbTle.setToolTip("")
        self.tbTle.setObjectName("tbTle")
        self.labelSatellite = QtWidgets.QLabel(self.centralwidget)
        self.labelSatellite.setGeometry(QtCore.QRect(20, 130, 101, 17))
        self.labelSatellite.setObjectName("labelSatellite")
        self.tbChooseSatellite = QtWidgets.QComboBox(self.centralwidget)
        self.tbChooseSatellite.setGeometry(QtCore.QRect(10, 150, 291, 27))
        self.tbChooseSatellite.setObjectName("tbChooseSatellite")
        self.btnPredict = QtWidgets.QPushButton(self.centralwidget)
        self.btnPredict.setGeometry(QtCore.QRect(360, 125, 161, 51))
        self.btnPredict.setObjectName("btnPredict")
        self.btnLoadTle = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadTle.setGeometry(QtCore.QRect(360, 40, 201, 26))
        self.btnLoadTle.setObjectName("btnLoadTle")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "py_sat_tracker"))
        self.btnAddLocation.setText(_translate("MainWindow", "Add location"))
        self.labelSatellite.setText(_translate("MainWindow", "Choose satellite"))
        self.btnPredict.setText(_translate("MainWindow", "Predict passes"))
        self.btnLoadTle.setText(_translate("MainWindow", "Load TLEs"))

