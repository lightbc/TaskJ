import os
import time

from util import FileUtil


def getUserPath():
    """获取Windows用户路径"""
    user_path = os.path.expanduser("~")
    return user_path


def getAppDir():
    """获取程序保存内容路径"""
    app_dir_name = "TaskJ"
    # 程序保存信息：用户路径+程序路径
    app_dir = getUserPath() + os.sep + app_dir_name
    if not os.path.exists(app_dir):
        FileUtil.createFileDirs(app_dir)
    return app_dir


def sysCurrentTime():
    """获取系统当前时间时间戳"""
    return time.time()


def sysDateTimeFormat(formatter="%Y-%m-%d %H:%M:%S"):
    """
    获取系统时间并格式化"
    :param formatter: 时间输出格式
    :return: fmt
    """""
    now = time.localtime(time.time())
    fmt = time.strftime(formatter, now)
    return fmt


def getDate(formatter="%Y-%m-%d"):
    """
    获取格式化日期
    :param formatter:日期输出格式
    :return: fmt
    """
    now = time.localtime(time.time())
    fmt = time.strftime(formatter, now)
    return fmt


def getAppTempDir():
    """系统缓存内容目录"""
    temp_dir = "temp"
    app_dir = getAppDir()
    temp_path = app_dir + os.sep + temp_dir
    if not os.path.exists(temp_path):
        FileUtil.createFileDirs(temp_path)
    return temp_path


def compareWithCurrent(tm):
    """
    比较指定时间和当前时间的大小
    :param tm: 指定时间-时间戳
    :return: -1-指定时间小于当前时间，0-指定时间等于当前时间，1-指定时间大于当前时间
    """
    curTime = time.time()
    if tm == curTime:
        return 0
    if tm < curTime:
        return -1
    if tm > curTime:
        return 1


def strToTimeStamp(tms, fmt="%Y-%m-%d %H:%M:%S"):
    """
    将指定格式的时间字符串转换成时间戳
    :param tms: 时间字符串
    :param fmt: 格式
    :return: 转化的时间戳格式
    """
    dt = time.strptime(tms, fmt)
    tt = time.mktime(dt)
    return tt
