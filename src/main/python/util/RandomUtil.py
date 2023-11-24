import random
import time
import uuid


def getRandom():
    """随机数：时间戳+五位随机数"""
    # 生成0-1之间的随机数
    r = random.random()
    # 保留五位小数位
    pr = format(r, '.5f')
    # 转换成整数
    ipr = int((float(pr) * 100000))
    # 当前时间时间戳
    timestamp = time.time()
    # 新随机数
    nr = str(int(timestamp)) + str(ipr)
    return nr


def getUUID():
    """UUID:移除-"""
    uid = uuid.uuid1()
    return str(uid).replace("-", "")
