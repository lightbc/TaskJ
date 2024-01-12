# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TaskJWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(808, 531)
        MainWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/images/logo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(3, 0, 3, 3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMinimumSize(QtCore.QSize(800, 500))
        self.splitter.setBaseSize(QtCore.QSize(0, 0))
        self.splitter.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.splitter.setAcceptDrops(False)
        self.splitter.setInputMethodHints(QtCore.Qt.ImhNone)
        self.splitter.setMidLineWidth(0)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(2)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.taskList = QtWidgets.QTableWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taskList.sizePolicy().hasHeightForWidth())
        self.taskList.setSizePolicy(sizePolicy)
        self.taskList.setMinimumSize(QtCore.QSize(150, 0))
        self.taskList.setSizeIncrement(QtCore.QSize(0, 0))
        self.taskList.setBaseSize(QtCore.QSize(0, 0))
        self.taskList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.taskList.setStyleSheet("")
        self.taskList.setInputMethodHints(QtCore.Qt.ImhNone)
        self.taskList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.taskList.setAutoScrollMargin(10)
        self.taskList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.taskList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.taskList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.taskList.setGridStyle(QtCore.Qt.NoPen)
        self.taskList.setRowCount(0)
        self.taskList.setColumnCount(2)
        self.taskList.setObjectName("taskList")
        self.taskList.horizontalHeader().setVisible(False)
        self.taskList.horizontalHeader().setCascadingSectionResizes(False)
        self.taskList.horizontalHeader().setDefaultSectionSize(150)
        self.taskList.horizontalHeader().setHighlightSections(True)
        self.taskList.horizontalHeader().setMinimumSectionSize(25)
        self.taskList.horizontalHeader().setStretchLastSection(True)
        self.taskList.verticalHeader().setVisible(False)
        self.taskList.verticalHeader().setCascadingSectionResizes(False)
        self.taskList.verticalHeader().setDefaultSectionSize(25)
        self.taskList.verticalHeader().setMinimumSectionSize(25)
        self.taskList.verticalHeader().setStretchLastSection(False)
        self.showLog = QtWidgets.QTextEdit(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showLog.sizePolicy().hasHeightForWidth())
        self.showLog.setSizePolicy(sizePolicy)
        self.showLog.setMinimumSize(QtCore.QSize(200, 0))
        self.showLog.setBaseSize(QtCore.QSize(0, 0))
        self.showLog.setReadOnly(True)
        self.showLog.setObjectName("showLog")
        self.verticalLayout_5.addWidget(self.splitter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menubianji = QtWidgets.QMenu(self.menubar)
        self.menubianji.setObjectName("menubianji")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menut = QtWidgets.QMenu(self.menu_3)
        self.menut.setObjectName("menut")
        MainWindow.setMenuBar(self.menubar)
        self.help_action = QtWidgets.QAction(MainWindow)
        self.help_action.setObjectName("help_action")
        self.new_create_action = QtWidgets.QAction(MainWindow)
        self.new_create_action.setObjectName("new_create_action")
        self.exit_action = QtWidgets.QAction(MainWindow)
        self.exit_action.setObjectName("exit_action")
        self.clear_log_action = QtWidgets.QAction(MainWindow)
        self.clear_log_action.setObjectName("clear_log_action")
        self.script_action = QtWidgets.QAction(MainWindow)
        self.script_action.setObjectName("script_action")
        self.all_stop_action = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../resources/images/stop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.all_stop_action.setIcon(icon1)
        self.all_stop_action.setObjectName("all_stop_action")
        self.all_log = QtWidgets.QAction(MainWindow)
        self.all_log.setObjectName("all_log")
        self.info_log = QtWidgets.QAction(MainWindow)
        self.info_log.setObjectName("info_log")
        self.warn_log = QtWidgets.QAction(MainWindow)
        self.warn_log.setObjectName("warn_log")
        self.error_log = QtWidgets.QAction(MainWindow)
        self.error_log.setObjectName("error_log")
        self.menu.addAction(self.new_create_action)
        self.menu.addAction(self.exit_action)
        self.menu_2.addAction(self.clear_log_action)
        self.menu_2.addAction(self.help_action)
        self.menubianji.addAction(self.script_action)
        self.menut.addAction(self.all_log)
        self.menut.addAction(self.info_log)
        self.menut.addAction(self.warn_log)
        self.menut.addAction(self.error_log)
        self.menu_3.addAction(self.all_stop_action)
        self.menu_3.addAction(self.menut.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menubianji.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TaskJ"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.menubianji.setTitle(_translate("MainWindow", "编辑"))
        self.menu_3.setTitle(_translate("MainWindow", "运行"))
        self.menut.setTitle(_translate("MainWindow", "显示日志"))
        self.help_action.setText(_translate("MainWindow", "关于"))
        self.help_action.setToolTip(_translate("MainWindow", "关于"))
        self.new_create_action.setText(_translate("MainWindow", "新建"))
        self.new_create_action.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.exit_action.setText(_translate("MainWindow", "退出"))
        self.clear_log_action.setText(_translate("MainWindow", "日志清除"))
        self.clear_log_action.setToolTip(_translate("MainWindow", "日志清除"))
        self.script_action.setText(_translate("MainWindow", "脚本"))
        self.script_action.setToolTip(_translate("MainWindow", "脚本"))
        self.script_action.setShortcut(_translate("MainWindow", "Ctrl+Alt+S"))
        self.all_stop_action.setText(_translate("MainWindow", "全部停止"))
        self.all_stop_action.setToolTip(_translate("MainWindow", "全部停止"))
        self.all_stop_action.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.all_log.setText(_translate("MainWindow", "ALL"))
        self.info_log.setText(_translate("MainWindow", "INFO"))
        self.warn_log.setText(_translate("MainWindow", "WARNING"))
        self.warn_log.setToolTip(_translate("MainWindow", "WARNING"))
        self.error_log.setText(_translate("MainWindow", "ERROR"))
