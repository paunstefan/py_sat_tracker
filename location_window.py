# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choose_location.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChooseLocation(object):
    def setupUi(self, ChooseLocation):
        ChooseLocation.setObjectName("ChooseLocation")
        ChooseLocation.resize(510, 216)
        ChooseLocation.setMinimumSize(QtCore.QSize(510, 216))
        ChooseLocation.setMaximumSize(QtCore.QSize(510, 216))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/FP_Satellite_icon.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ChooseLocation.setWindowIcon(icon)
        self.labelName = QtWidgets.QLabel(ChooseLocation)
        self.labelName.setGeometry(QtCore.QRect(11, 20, 54, 17))
        self.labelName.setObjectName("labelName")
        self.tbName = QtWidgets.QLineEdit(ChooseLocation)
        self.tbName.setGeometry(QtCore.QRect(10, 40, 171, 27))
        self.tbName.setObjectName("tbName")
        self.labelCoordinates = QtWidgets.QLabel(ChooseLocation)
        self.labelCoordinates.setGeometry(QtCore.QRect(11, 90, 171, 17))
        self.labelCoordinates.setObjectName("labelCoordinates")
        self.tbCoordinates = QtWidgets.QLineEdit(ChooseLocation)
        self.tbCoordinates.setGeometry(QtCore.QRect(10, 110, 171, 27))
        self.tbCoordinates.setObjectName("tbCoordinates")
        self.lvLocations = QtWidgets.QListWidget(ChooseLocation)
        self.lvLocations.setGeometry(QtCore.QRect(190, 10, 301, 181))
        self.lvLocations.setObjectName("lvLocations")
        self.btnAddLocation = QtWidgets.QPushButton(ChooseLocation)
        self.btnAddLocation.setGeometry(QtCore.QRect(10, 150, 71, 26))
        self.btnAddLocation.setObjectName("btnAddLocation")
        self.btnDeleteLocation = QtWidgets.QPushButton(ChooseLocation)
        self.btnDeleteLocation.setGeometry(QtCore.QRect(100, 150, 71, 26))
        self.btnDeleteLocation.setObjectName("btnDeleteLocation")

        self.retranslateUi(ChooseLocation)
        QtCore.QMetaObject.connectSlotsByName(ChooseLocation)

    def retranslateUi(self, ChooseLocation):
        _translate = QtCore.QCoreApplication.translate
        ChooseLocation.setWindowTitle(_translate("ChooseLocation", "Choose location"))
        self.labelName.setText(_translate("ChooseLocation", "Name"))
        self.labelCoordinates.setText(_translate("ChooseLocation", "Coordinates (Y.YY N, X.XX E)"))
        self.btnAddLocation.setText(_translate("ChooseLocation", "Add"))
        self.btnDeleteLocation.setText(_translate("ChooseLocation", "Delete"))

