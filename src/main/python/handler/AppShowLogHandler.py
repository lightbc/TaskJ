import logging


class AppShowLogHandler(logging.Handler):
    """
    程序日志UI显示处理程序
    """

    def __init__(self, show):
        super(AppShowLogHandler, self).__init__()
        self.show = show

    def emit(self, record):
        # 内容格式化
        msg = self.format(record)
        # 承载显示UI组件
        self.show.append(msg)
