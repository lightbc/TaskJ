# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClearLog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(263, 165)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.timeRange = QtWidgets.QComboBox(Form)
        self.timeRange.setMinimumSize(QtCore.QSize(0, 26))
        self.timeRange.setObjectName("timeRange")
        self.timeRange.addItem("")
        self.timeRange.addItem("")
        self.timeRange.addItem("")
        self.timeRange.addItem("")
        self.timeRange.addItem("")
        self.timeRange.addItem("")
        self.gridLayout.addWidget(self.timeRange, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.clearOk = QtWidgets.QPushButton(Form)
        self.clearOk.setMinimumSize(QtCore.QSize(0, 26))
        self.clearOk.setObjectName("clearOk")
        self.horizontalLayout_2.addWidget(self.clearOk)
        self.clearCancel = QtWidgets.QPushButton(Form)
        self.clearCancel.setMinimumSize(QtCore.QSize(0, 26))
        self.clearCancel.setObjectName("clearCancel")
        self.horizontalLayout_2.addWidget(self.clearCancel)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "日志清除"))
        self.timeRange.setItemText(0, _translate("Form", "时间不限"))
        self.timeRange.setItemText(1, _translate("Form", "过去1小时"))
        self.timeRange.setItemText(2, _translate("Form", "过去1天"))
        self.timeRange.setItemText(3, _translate("Form", "过去7天"))
        self.timeRange.setItemText(4, _translate("Form", "过去1个月"))
        self.timeRange.setItemText(5, _translate("Form", "过去1年"))
        self.label.setText(_translate("Form", "时间范围："))
        self.clearOk.setText(_translate("Form", "确认清除"))
        self.clearCancel.setText(_translate("Form", "取消"))
