# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Thu May 21 09:56:39 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(288, 718)
        MainWindow.setMaximumSize(QtCore.QSize(329, 750))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setMaximumSize(QtCore.QSize(320, 360))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.verticalLayout_3.addWidget(self.webView)
        self.toolBox = QtGui.QToolBox(self.centralwidget)
        self.toolBox.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.toolBox.setFont(font)
        self.toolBox.setFrameShape(QtGui.QFrame.StyledPanel)
        self.toolBox.setObjectName("toolBox")
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 266, 234))
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lblUser = QtGui.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.lblUser.setFont(font)
        self.lblUser.setObjectName("lblUser")
        self.horizontalLayout_7.addWidget(self.lblUser)
        self.cbQualifier = QtGui.QComboBox(self.page)
        self.cbQualifier.setObjectName("cbQualifier")
        self.cbQualifier.addItem(QtCore.QString())
        self.cbQualifier.addItem(QtCore.QString())
        self.cbQualifier.addItem(QtCore.QString())
        self.horizontalLayout_7.addWidget(self.cbQualifier)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.txtMsg = QtGui.QLineEdit(self.page)
        self.txtMsg.setMaxLength(140)
        self.txtMsg.setObjectName("txtMsg")
        self.horizontalLayout_9.addWidget(self.txtMsg)
        self.btnEmo1 = QtGui.QToolButton(self.page)
        self.btnEmo1.setObjectName("btnEmo1")
        self.horizontalLayout_9.addWidget(self.btnEmo1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.btnPlurk = QtGui.QPushButton(self.page)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btnPlurk.setFont(font)
        self.btnPlurk.setObjectName("btnPlurk")
        self.verticalLayout_2.addWidget(self.btnPlurk)
        self.line = QtGui.QFrame(self.page)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lblName = QtGui.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.lblName.setFont(font)
        self.lblName.setObjectName("lblName")
        self.horizontalLayout_6.addWidget(self.lblName)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtGui.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.lblKarma = QtGui.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.lblKarma.setFont(font)
        self.lblKarma.setObjectName("lblKarma")
        self.horizontalLayout_5.addWidget(self.lblKarma)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblInfo1 = QtGui.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.lblInfo1.setFont(font)
        self.lblInfo1.setObjectName("lblInfo1")
        self.horizontalLayout_3.addWidget(self.lblInfo1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblInfo2 = QtGui.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.lblInfo2.setFont(font)
        self.lblInfo2.setObjectName("lblInfo2")
        self.horizontalLayout_4.addWidget(self.lblInfo2)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 266, 231))
        self.page_2.setObjectName("page_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.page_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.cbPlurkId = QtGui.QComboBox(self.page_2)
        self.cbPlurkId.setObjectName("cbPlurkId")
        self.horizontalLayout_2.addWidget(self.cbPlurkId)
        self.btnShowResponses = QtGui.QPushButton(self.page_2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnShowResponses.setFont(font)
        self.btnShowResponses.setObjectName("btnShowResponses")
        self.horizontalLayout_2.addWidget(self.btnShowResponses)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lblProgress = QtGui.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lblProgress.setFont(font)
        self.lblProgress.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblProgress.setObjectName("lblProgress")
        self.horizontalLayout_8.addWidget(self.lblProgress)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.line_2 = QtGui.QFrame(self.page_2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblUser2 = QtGui.QLabel(self.page_2)
        self.lblUser2.setObjectName("lblUser2")
        self.horizontalLayout.addWidget(self.lblUser2)
        self.cbQualifier2 = QtGui.QComboBox(self.page_2)
        self.cbQualifier2.setObjectName("cbQualifier2")
        self.cbQualifier2.addItem(QtCore.QString())
        self.horizontalLayout.addWidget(self.cbQualifier2)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.txtResponse = QtGui.QLineEdit(self.page_2)
        self.txtResponse.setMaxLength(140)
        self.txtResponse.setObjectName("txtResponse")
        self.horizontalLayout_10.addWidget(self.txtResponse)
        self.btnEmo2 = QtGui.QToolButton(self.page_2)
        self.btnEmo2.setObjectName("btnEmo2")
        self.horizontalLayout_10.addWidget(self.btnEmo2)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.btnResponse = QtGui.QPushButton(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.btnResponse.setFont(font)
        self.btnResponse.setObjectName("btnResponse")
        self.verticalLayout.addWidget(self.btnResponse)
        self.toolBox.addItem(self.page_2, "")
        self.verticalLayout_3.addWidget(self.toolBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 288, 21))
        self.menubar.setObjectName("menubar")
        self.menuAction = QtGui.QMenu(self.menubar)
        self.menuAction.setObjectName("menuAction")
        self.menu_elp = QtGui.QMenu(self.menubar)
        self.menu_elp.setObjectName("menu_elp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLogin = QtGui.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.actionGetPlurks = QtGui.QAction(MainWindow)
        self.actionGetPlurks.setObjectName("actionGetPlurks")
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionE_xit = QtGui.QAction(MainWindow)
        self.actionE_xit.setObjectName("actionE_xit")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuAction.addAction(self.actionGetPlurks)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.actionExit)
        self.menu_elp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuAction.menuAction())
        self.menubar.addAction(self.menu_elp.menuAction())

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.lblUser.setText(QtGui.QApplication.translate("MainWindow", "unknown", None, QtGui.QApplication.UnicodeUTF8))
        self.cbQualifier.setItemText(0, QtGui.QApplication.translate("MainWindow", ":", None, QtGui.QApplication.UnicodeUTF8))
        self.cbQualifier.setItemText(1, QtGui.QApplication.translate("MainWindow", "is", None, QtGui.QApplication.UnicodeUTF8))
        self.cbQualifier.setItemText(2, QtGui.QApplication.translate("MainWindow", "has", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEmo1.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPlurk.setText(QtGui.QApplication.translate("MainWindow", "Plurk !!!", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Karma :", None, QtGui.QApplication.UnicodeUTF8))
        self.lblKarma.setText(QtGui.QApplication.translate("MainWindow", "0.00", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QtGui.QApplication.translate("MainWindow", "Page 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Plurk Id", None, QtGui.QApplication.UnicodeUTF8))
        self.btnShowResponses.setText(QtGui.QApplication.translate("MainWindow", "Show Responses", None, QtGui.QApplication.UnicodeUTF8))
        self.lblProgress.setText(QtGui.QApplication.translate("MainWindow", "LblProgrss", None, QtGui.QApplication.UnicodeUTF8))
        self.lblUser2.setText(QtGui.QApplication.translate("MainWindow", "unknown", None, QtGui.QApplication.UnicodeUTF8))
        self.cbQualifier2.setItemText(0, QtGui.QApplication.translate("MainWindow", "says", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEmo2.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btnResponse.setText(QtGui.QApplication.translate("MainWindow", "Respond to this Plurk", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QtGui.QApplication.translate("MainWindow", "Page 2", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAction.setTitle(QtGui.QApplication.translate("MainWindow", "&Plurk", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_elp.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLogin.setText(QtGui.QApplication.translate("MainWindow", "&Login", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGetPlurks.setText(QtGui.QApplication.translate("MainWindow", "&GetPlurks", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "&Open Plurk Web", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionE_xit.setText(QtGui.QApplication.translate("MainWindow", "E&xit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "E&xit", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
