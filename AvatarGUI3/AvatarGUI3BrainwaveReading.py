# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AvatarGUI3BrainwaveReading.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Avatar(object):
    def setupUi(self, Avatar):
        Avatar.setObjectName("Avatar")
        Avatar.resize(830, 799)
        self.centralwidget = QtWidgets.QWidget(Avatar)
        self.centralwidget.setStyleSheet("QWidget{\n"
"    background:\"#4a5b7b\"\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 811, 751))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setStyleSheet("QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.BrainwaveReading = QtWidgets.QWidget()
        self.BrainwaveReading.setObjectName("BrainwaveReading")
        self.manualcontrol = QtWidgets.QRadioButton(self.BrainwaveReading)
        self.manualcontrol.setGeometry(QtCore.QRect(50, 20, 121, 16))
        self.manualcontrol.setStyleSheet("QRadioButton{\n"
"color:white;\n"
"}\n"
"")
        self.manualcontrol.setObjectName("manualcontrol")
        self.autopilot = QtWidgets.QRadioButton(self.BrainwaveReading)
        self.autopilot.setGeometry(QtCore.QRect(200, 20, 99, 20))
        self.autopilot.setStyleSheet("QRadioButton{\n"
"color:white;\n"
"}\n"
"")
        self.autopilot.setObjectName("autopilot")
        self.readmymind = QtWidgets.QPushButton(self.BrainwaveReading)
        self.readmymind.setGeometry(QtCore.QRect(60, 60, 141, 121))
        self.readmymind.setStyleSheet("QPushButton {\n"
"    background-color: rgb(36, 44, 77); /* Default background color */\n"
"    background-image: url(:/Img/brain.png);\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white; /* Change background to white on hover */\n"
"    color: black;\n"
"}\n"
"")
        self.readmymind.setObjectName("readmymind")
        self.manualcontrol_2 = QtWidgets.QPushButton(self.BrainwaveReading)
        self.manualcontrol_2.setGeometry(QtCore.QRect(60, 580, 141, 121))
        self.manualcontrol_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(36, 44, 77); /* Default background color */\n"
"    background-image: url(:/Img/Connect.png);\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white; /* Change background to white on hover */\n"
"    color: black;\n"
"}\n"
"")
        self.manualcontrol_2.setObjectName("manualcontrol_2")
        self.themodelsays = QtWidgets.QLabel(self.BrainwaveReading)
        self.themodelsays.setGeometry(QtCore.QRect(60, 200, 121, 16))
        self.themodelsays.setStyleSheet("QLabel{\n"
"color:white;\n"
"}\n"
"")
        self.themodelsays.setObjectName("themodelsays")
        self.countlabel = QtWidgets.QTableWidget(self.BrainwaveReading)
        self.countlabel.setGeometry(QtCore.QRect(60, 230, 191, 61))
        self.countlabel.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.countlabel.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.countlabel.setObjectName("countlabel")
        self.countlabel.setColumnCount(2)
        self.countlabel.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.countlabel.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.countlabel.setHorizontalHeaderItem(1, item)
        self.notwhatiwasthinking = QtWidgets.QPushButton(self.BrainwaveReading)
        self.notwhatiwasthinking.setGeometry(QtCore.QRect(40, 310, 151, 51))
        self.notwhatiwasthinking.setStyleSheet("QPushButton {\n"
"    background-color: rgb(36, 44, 77); /* Default background color */\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white; /* Change background to white on hover */\n"
"    color:black;\n"
"}\n"
"")
        self.notwhatiwasthinking.setObjectName("notwhatiwasthinking")
        self.execute = QtWidgets.QPushButton(self.BrainwaveReading)
        self.execute.setGeometry(QtCore.QRect(219, 311, 101, 51))
        self.execute.setStyleSheet("QPushButton {\n"
"    background-color: rgb(36, 44, 77); /* Default background color */\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white; /* Change background to white on hover */\n"
"    color:black;\n"
"}\n"
"")
        self.execute.setObjectName("execute")
        self.keepdronealive = QtWidgets.QPushButton(self.BrainwaveReading)
        self.keepdronealive.setGeometry(QtCore.QRect(380, 380, 131, 41))
        self.keepdronealive.setStyleSheet("QPushButton {\n"
"    background-color: rgb(36, 44, 77); /* Default background color */\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white; /* Change background to white on hover */\n"
"    color:black;\n"
"}\n"
"")
        self.keepdronealive.setObjectName("keepdronealive")
        self.dronealivetext = QtWidgets.QTextEdit(self.BrainwaveReading)
        self.dronealivetext.setGeometry(QtCore.QRect(50, 380, 301, 41))
        self.dronealivetext.setStyleSheet("QTextEdit{\n"
"    background-color: white;\n"
"}\n"
"")
        self.dronealivetext.setObjectName("dronealivetext")
        self.flightlog = QtWidgets.QLabel(self.BrainwaveReading)
        self.flightlog.setGeometry(QtCore.QRect(30, 440, 71, 16))
        self.flightlog.setStyleSheet("QLabel{\n"
"        color: white;\n"
"}")
        self.flightlog.setObjectName("flightlog")
        self.consolelog = QtWidgets.QLabel(self.BrainwaveReading)
        self.consolelog.setGeometry(QtCore.QRect(590, 460, 81, 20))
        self.consolelog.setStyleSheet("QLabel{\n"
"        color: white;\n"
"}")
        self.consolelog.setObjectName("consolelog")
        self.flightlogspace = QtWidgets.QTextEdit(self.BrainwaveReading)
        self.flightlogspace.setGeometry(QtCore.QRect(40, 480, 191, 71))
        self.flightlogspace.setStyleSheet("QTextEdit{\n"
"    background-color: white;\n"
"}\n"
"")
        self.flightlogspace.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.flightlogspace.setObjectName("flightlogspace")
        self.consolelogspace = QtWidgets.QTextEdit(self.BrainwaveReading)
        self.consolelogspace.setGeometry(QtCore.QRect(590, 490, 201, 111))
        self.consolelogspace.setStyleSheet("QTextEdit{\n"
"    background-color: white;\n"
"}\n"
"")
        self.consolelogspace.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.consolelogspace.setObjectName("consolelogspace")
        self.prediction = QtWidgets.QTableWidget(self.BrainwaveReading)
        self.prediction.setGeometry(QtCore.QRect(450, 80, 321, 291))
        self.prediction.setStyleSheet("/* Header section - default style */\n"
"QHeaderView::section {\n"
"    color: black; /* Default text color */\n"
"    background-color: white; /* Background color */\n"
"}\n"
"\n"
"/* Header section - hover style */\n"
"QHeaderView::section:hover {\n"
"    color: white; /* Change text to black on hover */\n"
"    background-color: black; /* Optional hover background color */\n"
"    font-weight: medium; /* Make text bold on hover */\n"
"}\n"
"\n"
"")
        self.prediction.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.prediction.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.prediction.setObjectName("prediction")
        self.prediction.setColumnCount(3)
        self.prediction.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.prediction.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.prediction.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.prediction.setHorizontalHeaderItem(2, item)
        self.tabWidget.addTab(self.BrainwaveReading, "")
        Avatar.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Avatar)
        self.statusbar.setObjectName("statusbar")
        Avatar.setStatusBar(self.statusbar)

        self.retranslateUi(Avatar)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Avatar)

    def retranslateUi(self, Avatar):
        _translate = QtCore.QCoreApplication.translate
        Avatar.setWindowTitle(_translate("Avatar", "MainWindow"))
        self.manualcontrol.setText(_translate("Avatar", "Manual Contol"))
        self.autopilot.setText(_translate("Avatar", "Autopilot"))
        self.readmymind.setText(_translate("Avatar", "Read my mind.."))
        self.manualcontrol_2.setText(_translate("Avatar", "Connect"))
        self.themodelsays.setText(_translate("Avatar", "The model says..."))
        item = self.countlabel.horizontalHeaderItem(0)
        item.setText(_translate("Avatar", "Count"))
        item = self.countlabel.horizontalHeaderItem(1)
        item.setText(_translate("Avatar", "Label"))
        self.notwhatiwasthinking.setText(_translate("Avatar", "Not what I was thinking"))
        self.execute.setText(_translate("Avatar", "Execute"))
        self.keepdronealive.setText(_translate("Avatar", "Keep Drone Alive"))
        self.flightlog.setText(_translate("Avatar", "Flight Log"))
        self.consolelog.setText(_translate("Avatar", "Console Log "))
        item = self.prediction.horizontalHeaderItem(0)
        item.setText(_translate("Avatar", "Prediction Count"))
        item = self.prediction.horizontalHeaderItem(1)
        item.setText(_translate("Avatar", "Server Prediction"))
        item = self.prediction.horizontalHeaderItem(2)
        item.setText(_translate("Avatar", "Prediction Label"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BrainwaveReading), _translate("Avatar", "BrainwaveReading"))