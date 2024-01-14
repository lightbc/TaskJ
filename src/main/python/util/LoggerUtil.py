import logging
import os
import util.OSUtil as OSUtil
import util.FileUtil as FileUtil
import handler.AppShowLogHandler as AppShowLogHandler

# 日志保存目录名称
logDir = "log"
# 默认日志名称
default_log_name = "TaskJ_%s" % OSUtil.getDate()
# 日志文件拓展名
ext_log = ".log"
# 日志文件保存目录路径
savePath = OSUtil.getAppDir() + os.sep + logDir
# 日志默认输出格式
fmt = "[%(asctime)s] [%(levelname)-7s] [%(filename)s:%(lineno)d] : %(message)s"


def getLogger(fileName=None, level=None, *args):
    """
    获取日志对象
    :param fileName:自定义日志文件名称
    :param level: 日志输出等级
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
        file_handler = fileHandler()
        # 控制台输出处理程序
        console_handler = consoleHandler()
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    # 设置日志输出级别
    if level:
        logger.setLevel(level)
    else:
        logger.setLevel(logging.INFO)
    return logger


def fileHandler():
    """日志输出日志文件处理程序"""
    handler = logging.FileHandler(log_path, encoding="UTF-8")
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter(fmt))
    return handler


def consoleHandler():
    """日志输出控制台处理程序"""
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter(fmt))
    return handler


def showLogHandler(showLog, showType=None):
    """应用程序UI显示日志内容处理程序"""
    handler = AppShowLogHandler.AppShowLogHandler(showLog, showType)
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter(fmt))
    return handler


def shutDown():
    """关闭日志记录器"""
    logging.shutdown()


def removeHandlers(logger):
    """移除日志处理程序"""
    b = False
    try:
        if logger:
            for handler in logger.handlers:
                logger.removeHandler(handler)
            b = True
    except Exception as e:
        raise
    finally:
        return b


def showAssignLevelLog(logger, showLog=None, showType=None):
    """添加日志处理器前，先移除已存在的处理器，避免内容重复"""
    if logger and showLog:
        b = removeHandlers(logger)
        if b:
            showLog.setText("")
            addHandlers(logger, showLog, showType)


def addHandlers(logger, showLog=None, showType=None):
    """添加日志处理程序"""
    if logger:
        fh = fileHandler()
        ch = consoleHandler()
        logger.addHandler(fh)
        logger.addHandler(ch)
        if showLog:
            sh = showLogHandler(showLog, showType)
            logger.addHandler(sh)
