# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'droidsec.ui'
#
# Created: Thu Jun 18 11:44:08 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1250, 750)
        MainWindow.setMinimumSize(QtCore.QSize(1250, 750))
        MainWindow.setMaximumSize(QtCore.QSize(1250, 750))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.loadedAPK_label = QtGui.QLabel(self.centralwidget)
        self.loadedAPK_label.setGeometry(QtCore.QRect(20, 10, 601, 31))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.loadedAPK_label.setFont(font)
        self.loadedAPK_label.setObjectName(_fromUtf8("loadedAPK_label"))
        self.chooseAPKBtn = QtGui.QPushButton(self.centralwidget)
        self.chooseAPKBtn.setGeometry(QtCore.QRect(679, 10, 121, 32))
        self.chooseAPKBtn.setObjectName(_fromUtf8("chooseAPKBtn"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(9, 39, 1231, 661))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 10, 501, 291))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.permsTable = QtGui.QTableWidget(self.groupBox_3)
        self.permsTable.setGeometry(QtCore.QRect(10, 30, 481, 251))
        self.permsTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.permsTable.setShowGrid(True)
        self.permsTable.setObjectName(_fromUtf8("permsTable"))
        self.permsTable.setColumnCount(1)
        self.permsTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.permsTable.setHorizontalHeaderItem(0, item)
        self.groupBox_2 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 300, 501, 321))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.logArea = QtGui.QTextBrowser(self.groupBox_2)
        self.logArea.setEnabled(True)
        self.logArea.setGeometry(QtCore.QRect(10, 30, 481, 251))
        self.logArea.setAutoFillBackground(False)
        self.logArea.setStyleSheet(_fromUtf8("background-color:black;"))
        self.logArea.setObjectName(_fromUtf8("logArea"))
        self.clearLogBtn = QtGui.QPushButton(self.groupBox_2)
        self.clearLogBtn.setGeometry(QtCore.QRect(10, 290, 110, 32))
        self.clearLogBtn.setObjectName(_fromUtf8("clearLogBtn"))
        self.saveLogBtn = QtGui.QPushButton(self.groupBox_2)
        self.saveLogBtn.setGeometry(QtCore.QRect(130, 290, 110, 32))
        self.saveLogBtn.setObjectName(_fromUtf8("saveLogBtn"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.groupBox = QtGui.QGroupBox(self.tab_4)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 281, 621))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.treeWidget = QtGui.QTreeWidget(self.groupBox)
        self.treeWidget.setGeometry(QtCore.QRect(10, 30, 256, 581))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.sourceTextWidget = QtGui.QWidget(self.tab_4)
        self.sourceTextWidget.setGeometry(QtCore.QRect(300, 10, 911, 621))
        self.sourceTextWidget.setObjectName(_fromUtf8("sourceTextWidget"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1250, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "DroidSec", None))
        self.loadedAPK_label.setText(_translate("MainWindow", "No APK Loaded", None))
        self.chooseAPKBtn.setText(_translate("MainWindow", "Choose APK...", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Permissions", None))
        item = self.permsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Uses permissions", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Log", None))
        self.clearLogBtn.setText(_translate("MainWindow", "Clear", None))
        self.saveLogBtn.setText(_translate("MainWindow", "Save ...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "APK", None))
        self.groupBox.setTitle(_translate("MainWindow", "Sources", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Sources", None))
