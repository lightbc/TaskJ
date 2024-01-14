import TaskJWin
import Save
import util.AppUtil as AppUtil
import util.RandomUtil as RandomUtil
import util.TaskListUtil as TaskListUtil
import entity.NewCreate as n
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtCore as QtCore

NewCreate = n.NewCreate


class NewCreateDialog(QtWidgets.QDialog, Save.Ui_Form, TaskJWin.Ui_MainWindow):
    """新建任务对话框"""

    def __init__(self, parent=None):
        super(NewCreateDialog, self).__init__(parent)
        self.isInitUpdate = False
        self.filePath = None
        self.setupUi(self)
        # 填充执行时间默认值
        self.runTime.setDateTime(QtCore.QDateTime.currentDateTime())
        # 填充结束时间默认值，大于开始执行时间1小时
        self.stopTime.setDateTime(QtCore.QDateTime.currentDateTime().addSecs(3600))
        # 打开对话框
        self.open()
        self.cancel.clicked.connect(self.close)
        self.runMode.currentTextChanged.connect(self.runModeChange)

    def saveAction(self, taskList: QtWidgets.QTableWidget):
        """
        新建保存动作
        :param taskList: 任务列表
        :return:
        """
        self.doOpAction()
        TaskListUtil.loadTaskList(taskList)

    def updateAction(self, nid, taskList: QtWidgets.QTableWidget):
        """
        更新保存任务信息动作
        :param nid: 识别主键
        :param taskList: 任务列表
        :return:
        """
        self.doOpAction(nid, False)
        TaskListUtil.loadTaskList(taskList)

    def doOpAction(self, nid=None, isSave=True):
        """
        操作执行动作
        :param nid: 识别主键
        :param isSave: true-新建，false-更新
        :return:
        """
        if isSave:
            nid = RandomUtil.getUUID()
        name = self.name.text()
        ot = self.opType.currentText()
        rm = self.runMode.currentText()
        rc = self.runCmd.toPlainText()
        rt = self.runTime.text()
        st = self.stopTime.text()
        cv = self.cycleVal.text()
        ct = self.cycleType.currentText()
        nc = NewCreate(nid, name, ot, rm, rc, rt, st, cv, ct)
        AppUtil.save(nc, self)

    def invertShow(self, data):
        """
        反显保存任务信息
        :param data: 任务信息
        :return:
        """
        self.isInitUpdate = True
        if data:
            self.name.setText(data["name"])
            self.opType.setCurrentText(data["opType"])
            self.runMode.setCurrentText(data["runMode"])
            self.runCmd.setText(data["runCmd"])
            fmt = "yyyy-MM-dd HH:mm:ss"
            dt = QtCore.QDateTime().fromString(data["runTime"], fmt)
            st = QtCore.QDateTime().fromString(data["stopTime"], fmt)
            self.runTime.setDateTime(dt)
            self.stopTime.setDateTime(st)
            self.cycleVal.setText(data["cycleVal"])
            self.cycleType.setCurrentText(data["cycleType"])

    def runModeChange(self):
        """运行模式改变选择事件监听"""
        mode = self.runMode.currentText()
        if self.isInitUpdate:
            if mode and mode == "文件":  # 选择【文件】，文本域不可以编辑
                self.runCmd.setReadOnly(True)
            elif mode and mode == "命令行":  # 选择【命令行】，文本域可以编辑
                self.runCmd.setReadOnly(False)
            self.isInitUpdate = False
        else:
            if mode and mode == "文件":  # 选择【文件】，文本域不可以编辑
                self.runCmd.setReadOnly(True)
                fileDialog = QtWidgets.QFileDialog()
                resp = fileDialog.getOpenFileName(self, "脚本选择", "./", "BAT(*.bat)")
                self.filePath = resp[0]
                if self.filePath:
                    self.runCmd.setPlainText(self.filePath)
            elif mode and mode == "命令行":  # 选择【命令行】，文本域可以编辑
                self.runCmd.setReadOnly(False)
