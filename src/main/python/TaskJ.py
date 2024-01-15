import sys
import About
import TaskJWin
import dialog.NewCreateDialog as NewCreateDialog
import dialog.ClearLogDialog as ClearLogDialog
import dialog.EditScriptDialog as EditScriptDialog
import util.TaskListUtil as TaskListUtil
import util.QuartzUtil as QuartzUtil
import util.LoggerUtil as LoggerUtil
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui

version = "v1.1.0"
# 唯一日志记录对象，避免消息重复输出
logger = LoggerUtil.getLogger()


class TaskJ(QtWidgets.QMainWindow, TaskJWin.Ui_MainWindow):
    """应用程序入口"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.qz = None
        self.menuActionListener()
        self.splitter.setSizes([200, 600])
        # 任务列表第二列识别主键列隐藏
        self.taskList.setColumnHidden(1, True)
        TaskListUtil.loadTaskList(self.taskList)
        # 任务列表右键监听
        self.taskList.customContextMenuRequested.connect(self.loadTaskListMenu)

        # 日志UI输出
        if logger:
            logHandler = LoggerUtil.showLogHandler(self.showLog)
            logger.addHandler(logHandler)

    def loadTaskListMenu(self, pos):
        """
        加载任务列表右键菜单项
        :param pos: 位置
        :return:
        """
        row = self.taskList.rowAt(pos.y())
        col = self.taskList.columnAt(pos.x())
        if row is not -1 and col is 0:
            popMenu = QtWidgets.QMenu()
            # 创建操作动作
            run_action = QtWidgets.QAction("运行", popMenu)
            run_stop_action = QtWidgets.QAction("停止", popMenu)
            update_action = QtWidgets.QAction("修改", popMenu)
            del_action = QtWidgets.QAction("删除", popMenu)
            # 菜单添加动作列表
            popMenu.addAction(run_action)
            popMenu.addAction(run_stop_action)
            popMenu.addAction(update_action)
            popMenu.addAction(del_action)
            # 添加触发动作
            name = self.taskList.item(row, 0).text()
            nid = self.taskList.item(row, 1).text()
            run_action.triggered.connect(lambda: self.taskRun(nid))
            run_stop_action.triggered.connect(lambda: self.taskRunStop(nid))
            update_action.triggered.connect(lambda: self.taskListUpdate(nid))
            del_action.triggered.connect(lambda: self.taskListDelete(nid, name))

            popMenu.exec_(QtGui.QCursor.pos())

    def taskRun(self, nid):
        """
        任务运行
        :param nid:识别主键
        :return:
        """
        # 先删除，再创建调度任务执行对象
        if self.qz:
            del self.qz
        self.qz = QuartzUtil.QuartzUtil(logger)
        self.qz.createJob(nid)

    def taskRunStop(self, nid):
        """
        任务停止
        :param nid:识别主键
        :return:
        """
        if self.qz:
            self.qz.removeJob(nid)

    def showAssignLogs(self):
        """显示指定级别的日志内容"""
        self.all_log.triggered.connect(lambda: LoggerUtil.showAssignLevelLog(logger, self.showLog))
        self.info_log.triggered.connect(
            lambda: LoggerUtil.showAssignLevelLog(logger, self.showLog, self.info_log.text()))
        self.warn_log.triggered.connect(
            lambda: LoggerUtil.showAssignLevelLog(logger, self.showLog, self.warn_log.text()))
        self.error_log.triggered.connect(
            lambda: LoggerUtil.showAssignLevelLog(logger, self.showLog, self.error_log.text()))

    def taskListUpdate(self, nid):
        """
        任务保存信息更新
        :param nid: 识别主键
        :return:
        """
        dialog = NewCreateDialog.NewCreateDialog(self)
        data = TaskListUtil.invertData(nid)
        dialog.invertShow(data)
        dialog.save.clicked.connect(lambda: NewCreateDialog.NewCreateDialog.updateAction(dialog, nid, self.taskList))

    def taskListDelete(self, nid, name):
        """
        任务列表任务删除
        :param nid: 识别主键
        :param name: 任务名称
        :return:
        """
        result = QtWidgets.QMessageBox.question(self, "提示", "是否确认删除任务【%s】？" % name)
        # 确认删除
        if result == QtWidgets.QMessageBox.Yes:
            TaskListUtil.delete(nid)
            TaskListUtil.loadTaskList(self.taskList)

    def menuActionListener(self):
        """菜单事件监听"""
        self.newCreate()
        self.exit()
        self.script()
        self.allStop()
        self.showAssignLogs()
        self.clearLog()
        self.about()

    def newCreate(self):
        """新建"""
        self.new_create_action.triggered.connect(self.create)

    def create(self):
        """新建执行方法"""
        dialog = NewCreateDialog.NewCreateDialog(self)
        dialog.save.clicked.connect(lambda: NewCreateDialog.NewCreateDialog.saveAction(dialog, self.taskList))

    def exit(self):
        """退出程序"""
        self.exit_action.triggered.connect(self.appExit)

    def script(self):
        """脚本编辑"""
        self.script_action.triggered.connect(self.EditScript)

    def EditScript(self):
        """脚本编辑动作事件"""
        EditScriptDialog.EditScriptDialog(self)

    def allStop(self):
        """全部任务停止运行"""
        self.all_stop_action.triggered.connect(self.allStopRun)

    def allStopRun(self):
        """全部任务停止运行动作事件"""
        if self.qz:
            self.qz.allRunTaskStop()

    def clearLog(self):
        """日志清理"""
        self.clear_log_action.triggered.connect(self.clear)

    def clear(self):
        """日志起立动作事件"""
        dialog = ClearLogDialog.ClearLogDialog(logger, self.showLog)
        dialog.clearOk.clicked.connect(lambda: ClearLogDialog.ClearLogDialog.clearAction(dialog))

    def about(self):
        """关于"""
        about = AboutDialog(self)
        self.help_action.triggered.connect(about.open)

    def appExit(self):
        """退出程序动作事件"""
        sys.exit(-1)


class AboutDialog(QtWidgets.QDialog, About.Ui_widget):
    """新建对话框"""

    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent)
        self.setupUi(self)
        self.version.setText(version)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = TaskJ()
    window.show()
    sys.exit(app.exec_())
