import time
import TaskJWin
import ClearLog
from enums.TimeRangeEnum import TimeRangEnum
from util import LoggerUtil, FileUtil
from PyQt5.QtWidgets import QDialog, QMessageBox

# 日志保存路径
log_dir = LoggerUtil.savePath


class ClearLogDialog(QDialog, ClearLog.Ui_Form, TaskJWin.Ui_MainWindow):
    """
    日志清除UI界面
    """

    def __init__(self, logger, showLog, parent=None):
        super(ClearLogDialog, self).__init__(parent)
        self.logger = logger
        self.sh = showLog
        # 移除日志记录器的处理器，否则清理日志文件时会报错：文件被占用
        LoggerUtil.removeHandlers(logger)
        self.setupUi(self)
        # 打开对话框
        self.open()
        self.clearCancel.clicked.connect(self.close)

    def clearAction(self):
        """清除操作"""
        b = self.clearRange()
        if b:
            # 日志内容清除后，日志显示UI中的日志文本内容也需要同步清理
            self.sh.setPlainText("")
            QMessageBox.information(self, "提示", "清除成功！")
            self.close()
        else:
            QMessageBox.warning(self, "警告", "清除失败！")
            self.close()
        # 日志文件处理完毕后，再将处理器添加回去
        LoggerUtil.addHandlers(self.logger, self.sh)

    def clearRange(self):
        """
        清理指定时间内的日志数据
        :return: true：清理成功，false：清理失败
        """
        b = False
        try:
            time_range = self.timeRange.currentText()
            current_time = int(time.time())
            if time_range == TimeRangEnum.TIME_UNLIMITED:
                r = -1
                clear(current_time, r)
            elif time_range == TimeRangEnum.ONE_HOUR:
                r = 60 * 60
                clear(current_time, r)
            elif time_range == TimeRangEnum.ONE_DAY:
                r = 60 * 60 * 24
                clear(current_time, r)
            elif time_range == TimeRangEnum.SEVEN_DAY:
                r = 60 * 60 * 24 * 7
                clear(current_time, r)
            elif time_range == TimeRangEnum.ONE_MONTH:
                r = 60 * 60 * 24 * 30
                clear(current_time, r)
            elif time_range == TimeRangEnum.ONE_YEAR:
                r = 60 * 60 * 24 * 365
                clear(current_time, r)
            b = True
        except Exception as e:
            raise e
        finally:
            return b


def clear(curTime, r):
    """
    清除符合清理条件的日志文件
    :param curTime: 系统当前时间
    :param r: 日志清除时间上限
    :return:
    """
    # 获取日志保存目录下的日志文件路径
    files_path = FileUtil.getDirFilesAbsolutePath(log_dir)
    if files_path and len(files_path) > 0:
        for file_path in files_path:
            # 获取文件的创建时间
            file_create_time = FileUtil.getFileCreateTime(file_path)
            create_time = int(file_create_time)
            if r == -1:  # 时间不限
                FileUtil.removeFile(file_path)
                continue
            elif r > 0 and r >= curTime - create_time:  # 指定时间范围内
                FileUtil.removeFile(file_path)
