# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\CSTI-ModEditor\Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(884, 723)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.treeView = QtWidgets.QTreeView(self.layoutWidget)
        self.treeView.setEnabled(True)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 884, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menuLanguage = QtWidgets.QMenu(self.menu_2)
        self.menuLanguage.setObjectName("menuLanguage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_newMod = QtWidgets.QAction(MainWindow)
        self.action_newMod.setObjectName("action_newMod")
        self.action_loadMod = QtWidgets.QAction(MainWindow)
        self.action_loadMod.setObjectName("action_loadMod")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.action_ResizeMode = QtWidgets.QAction(MainWindow)
        self.action_ResizeMode.setObjectName("action_ResizeMode")
        self.action_ExportZip = QtWidgets.QAction(MainWindow)
        self.action_ExportZip.setObjectName("action_ExportZip")
        self.actionChinese = QtWidgets.QAction(MainWindow)
        self.actionChinese.setObjectName("actionChinese")
        self.actionEnglish = QtWidgets.QAction(MainWindow)
        self.actionEnglish.setObjectName("actionEnglish")
        self.menu.addAction(self.action_newMod)
        self.menu.addAction(self.action_loadMod)
        self.menu.addAction(self.action_save)
        self.menu.addAction(self.action_ExportZip)
        self.menuLanguage.addAction(self.actionChinese)
        self.menuLanguage.addAction(self.actionEnglish)
        self.menu_2.addAction(self.action_ResizeMode)
        self.menu_2.addAction(self.menuLanguage.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ModEditor"))
        self.pushButton.setText(_translate("MainWindow", "Open"))
        self.menu.setTitle(_translate("MainWindow", "File"))
        self.menu_2.setTitle(_translate("MainWindow", "Setting"))
        self.menuLanguage.setTitle(_translate("MainWindow", "Language"))
        self.action_newMod.setText(_translate("MainWindow", "New Mod Project"))
        self.action_loadMod.setText(_translate("MainWindow", "Load Mod Project"))
        self.action_save.setText(_translate("MainWindow", "Save Mod Project"))
        self.action_ResizeMode.setText(_translate("MainWindow", "Turn off auto contents resize"))
        self.action_ExportZip.setText(_translate("MainWindow", "Export Mod as Zip Format"))
        self.action_ExportZip.setToolTip(_translate("MainWindow", "Export Mod as Zip Format"))
        self.actionChinese.setText(_translate("MainWindow", "Chinese"))
        self.actionEnglish.setText(_translate("MainWindow", "English"))
