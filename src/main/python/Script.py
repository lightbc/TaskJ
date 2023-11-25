# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Script.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(540, 403)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.script_toolbar = QtWidgets.QVBoxLayout()
        self.script_toolbar.setObjectName("script_toolbar")
        self.verticalLayout.addLayout(self.script_toolbar)

        # 工具栏
        res_path = "../resources/images/"
        self.toolBar = QtWidgets.QToolBar()
        self.toolBar.setObjectName("toolBar")
        self.save_action = QtWidgets.QAction()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(res_path + "save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_action.setIcon(icon)
        self.save_action.setObjectName("save_action")
        self.run_action = QtWidgets.QAction()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(res_path + "run_script.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.run_action.setIcon(icon1)
        self.run_action.setObjectName("run_action")
        self.toolBar.addAction(self.save_action)
        self.toolBar.addAction(self.run_action)
        self.script_toolbar.addWidget(self.toolBar)

        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_4.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "脚本编辑"))
        # 工具栏工具动作
        self.save_action.setText(_translate("Form", "保存(Ctrl+S)"))
        self.save_action.setToolTip(_translate("Form", "保存(Ctrl+S)"))
        self.save_action.setShortcut(_translate("Form", "Ctrl+S"))
        self.run_action.setText(_translate("Form", "运行(Ctrl+R)"))
        self.run_action.setToolTip(_translate("Form", "运行(Ctrl+R)"))
        self.run_action.setShortcut(_translate("Form", "Ctrl+R"))