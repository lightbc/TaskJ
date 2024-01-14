import os
import json
import util.OSUtil as OSUtil
import util.FormatCheckUtil as FormatCheckUtil


def createFileDirs(path):
    """
    创建文件夹（单/多）
    :param path: 路径
    :return:
    """
    if path and not os.path.exists(path):
        os.makedirs(path, True)


def write(path, ct):
    """
    文件写入内容
    :param path: 路径
    :param ct: 写入内容
    :return: true-成功，false-失败
    """
    b = False
    try:
        if path and ct:
            file = open(path, 'w', encoding='UTF-8')
            file.write(ct)
            file.close()
            b = True
    except Exception as e:
        raise e
    finally:
        return b


def writeCfg(ct):
    """
     配置信息写入程序配置文件中去
    :param ct: 配置信息
    :return: true-成功，false-失败
    """
    return write(getCfgPath(), ct)


def read(path):
    """
    读取文件内容
    :param path: 路径
    :return: 文件内容
    """
    r = None
    try:
        if path and os.path.exists(path):
            file = open(path, encoding='UTF-8')
            ct = file.read()
            file.close()
            r = ct
    except Exception as e:
        raise e
    finally:
        return r


def getCfgPath():
    """
    获取程序配置文件的路径
    :return: 配置文件路径
    """
    cfg = "TaskJ.cfg"
    path = OSUtil.getAppDir() + os.sep + cfg
    return path


def getCfg():
    """
    获取程序的配置文件信息
    :return: 配置数据
    """
    path = getCfgPath()
    ct = read(path)
    b = FormatCheckUtil.isList(ct)
    if b:
        return json.loads(ct)
    else:
        return []


def getDirFiles(dirPath):
    """
    获取文件夹下的文件列表
    :param dirPath: 指定目录路径
    :return: 目录下的文件列表
    """
    return os.listdir(dirPath)


def getFileCreateTime(filePath):
    """
    获取文件的创建时间
    :param filePath: 文件路径
    :return: 文件创建时间
    """
    return os.path.getctime(filePath)


def removeFile(path):
    """
    删除文件
    :param path: 文件路径
    :return:
    """
    os.remove(path)


def getDirFilesAbsolutePath(dirPath):
    """
    获取文件夹下所有文件的绝对路径
    :param dirPath: 目录路径
    :return: 指定目录下所有文件的绝对路径
    """
    dir_files = getDirFiles(dirPath)
    file_absolute_path = []
    if dir_files:
        for dir_file in dir_files:
            abs_path = dirPath + os.sep + dir_file
            file_absolute_path.append(abs_path)
    return file_absolute_path
