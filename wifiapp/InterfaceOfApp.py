# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_last.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WifiPasswordApp(object):
    def setupUi(self, WifiPasswordApp):
        WifiPasswordApp.setObjectName("WifiPasswordApp")
        WifiPasswordApp.resize(566, 460)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("wifiIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WifiPasswordApp.setWindowIcon(icon)
        WifiPasswordApp.setIconSize(QtCore.QSize(50, 50))
        self.centralwidget = QtWidgets.QWidget(WifiPasswordApp)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.wifiPasswordTitleField = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.wifiPasswordTitleField.setFont(font)
        self.wifiPasswordTitleField.setObjectName("wifiPasswordTitleField")
        self.verticalLayout.addWidget(self.wifiPasswordTitleField)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 542, 361))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.wifiIsimSifre = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.wifiIsimSifre.setFont(font)
        self.wifiIsimSifre.setObjectName("wifiIsimSifre")
        self.verticalLayout_2.addWidget(self.wifiIsimSifre)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.GosterButonu = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GosterButonu.setFont(font)
        self.GosterButonu.setObjectName("GosterButonu")
        self.verticalLayout.addWidget(self.GosterButonu)
        WifiPasswordApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(WifiPasswordApp)
        self.GosterButonu.clicked.connect(WifiPasswordApp.my_slot) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(WifiPasswordApp)

    def retranslateUi(self, WifiPasswordApp):
        _translate = QtCore.QCoreApplication.translate
        WifiPasswordApp.setWindowTitle(_translate("WifiPasswordApp", "WifiPasswordMonitor"))
        self.wifiPasswordTitleField.setText(_translate("WifiPasswordApp", "<html><head/><body><p align=\"center\">WIFI - PASSWORD</p></body></html>"))
        self.GosterButonu.setText(_translate("WifiPasswordApp", "Göster"))