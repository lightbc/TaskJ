import logging


class AppShowLogHandler(logging.Handler):
    """
    程序日志UI显示处理程序
    """

    def __init__(self, show, showType=None):
        super(AppShowLogHandler, self).__init__()
        self.show = show
        self.showType = showType

    def emit(self, record):
        # 内容格式化
        msg = self.format(record)
        # 承载显示UI组件
        msg = levelInfo(msg, record.levelname) if record.levelname else msg
        # 显示指定日志级别日志
        if self.showType:
            if self.showType == record.levelname:
                self.show.append(msg)
        else:
            self.show.append(msg)


def levelInfo(msg, levelName):
    if levelName:
        if levelName == logging.getLevelName(logging.INFO):
            return info(msg)
        elif levelName == logging.getLevelName(logging.WARNING):
            return warn(msg)
        elif levelName == logging.getLevelName(logging.ERROR):
            return error(msg)
    return None


def info(msg):
    return "<b style='color:#0FC32D; white-space: pre;'>" + msg + "</b>"


def warn(msg):
    return "<b style='color:#FFA500; white-space: pre;'>" + msg + "</b>"


def error(msg):
    return "<b style='color:#FF4B5A; white-space: pre;'>" + msg + "</b>"
