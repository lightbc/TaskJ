import json


class NewCreate:
    """
    任务信息实体类
    """

    def __init__(self, nId=None, name=None, opType=None, runMode=None, runCmd=None, runTime=None, stopTime=None,
                 cycleVal=None, cycleType=None):
        # 识别主键
        self.nId = nId
        # 任务名称
        self.name = name
        # 执行类型
        self.opType = opType
        # 执行方式
        self.runMode = runMode
        # 执行命令/文件
        self.runCmd = runCmd
        # 执行时间（首次）
        self.runTime = runTime
        # 结束时间
        self.stopTime = stopTime
        # 执行周期
        self.cycleVal = cycleVal
        # 执行周期单位
        self.cycleType = cycleType

    def __str__(self):
        """
        实体转换json字符串
        :return: json 字符串
        """
        nj = json.dumps(self.__dict__)
        return nj

    def to_dict(self):
        """
        字典类型
        :return: dict
        """
        return self.__dict__

    def from_dict(self, data):
        """
        将dict转换成实体
        :param data: dict 数据
        :return: self 实体
        """
        if data:
            for key in self.__dict__.keys():
                setattr(self, key, data[key])
            return self
        return None
