import logging
import os

from util import OSUtil, FileUtil
from handler import AppShowLogHandler

# 日志保存目录名称
logDir = "log"
# 默认日志名称
default_log_name = "TaskJ_%s" % OSUtil.getDate()
# 日志文件拓展名
ext_log = ".log"
# 日志文件保存目录路径
savePath = OSUtil.getAppDir() + os.sep + logDir
# 日志默认输出格式
fmt = "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] : %(message)s"


def getLogger(fileName=None, level=None, showLog=None, *args):
    """
    获取日志对象
    :param fileName:自定义日志文件名称
    :param level: 日志输出等级
    :param showLog: 程序显示日志内容UI组件对象
    :param args: 日志处理handler
    :return: 日志处理对象
    """
    # 声明全局变量
    global log_path
    # 创建日志保存目录
    FileUtil.createFileDirs(savePath)
    if fileName:  # 自定义日志文件名称
        log_path = savePath + os.sep + fileName + ext_log
    else:  # 默认日志文件名称
        log_path = savePath + os.sep + default_log_name + ext_log
    logger = logging.getLogger("logger")
    if args:  # 设置自定义handler
        for arg in args:
            logger.addHandler(arg)
    else:  # 设置默认handler
        # 文件输出处理程序
        file_handler = fileHandler(level)
        # 控制台输出处理程序
        console_handler = consoleHandler(level)
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        # 应用程序UI显示组件处理程序
        if showLog:
            show_log_handler = showLogHandler(showLog, level)
            logger.addHandler(show_log_handler)

    # 设置日志输出级别
    if level:
        logger.setLevel(level)
    else:
        logger.setLevel(logging.INFO)
    return logger


def fileHandler(level=None, formatter=None):
    """
    文件处理程序
    :param level: 日志级别
    :param formatter: 输出格式
    :return: handler
    """
    handler = logging.FileHandler(log_path, encoding="UTF-8")
    if level:
        handler.setLevel(level)
    else:
        handler.setLevel(logging.INFO)
    if formatter:
        handler.setFormatter(formatter)
    else:
        handler.setFormatter(logging.Formatter(fmt))
    return handler


def consoleHandler(level=None, formatter=None):
    """
    控制台处理程序
    :param level:日志级别
    :param formatter: 输出格式
    :return: handler
    """
    handler = logging.StreamHandler()
    if level:
        handler.setLevel(level)
    else:
        handler.setLevel(logging.INFO)
    if formatter:
        handler.setFormatter(logging.Formatter(formatter))
    else:
        handler.setFormatter(logging.Formatter(fmt))
    return handler


def showLogHandler(showLog, level=None, formatter=None):
    """
    应用程序输出UI组件处理程序
    :param showLog: 日志显示UI组件
    :param level: 日志级别
    :param formatter: 输出格式
    :return: handler
    """
    handler = AppShowLogHandler.AppShowLogHandler(showLog)
    if level:
        handler.setLevel(level)
    else:
        handler.setLevel(logging.INFO)
    if formatter:
        handler.setFormatter(logging.Formatter(formatter))
    else:
        handler.setFormatter(logging.Formatter(fmt))
    return handler


def shutDown():
    """关闭日志记录器"""
    logging.shutdown()
