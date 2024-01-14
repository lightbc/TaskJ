import enum

Enum = enum.Enum


class StatusCodeEnum(Enum):
    """
    状态枚举类
    """
    OK = (0, "成功")
    ERROR = (-1, "错误")
    GET_PARAMS_EXCEPTION = (1000, "获取参数异常！")
    NAME_EMPTY = (1001, "名称不能为空！")
    RUN_CMD_EMPTY = (1002, "执行命令不能为空！")
    RUN_TIME_EMPTY = (1003, "执行时间不能为空！")
    STOP_TIME_EMPTY = (1004, "结束时间不能为空！")
    CYCLE_VALUE_EMPTY = (1005, "执行周期不能为空！")
    STOP_TIME_LT_RUN_TIME = (1006, "结束时间需要大于开始时间！")
    # 动态提示内容
    STR_LEN_ILLEGAL = (1007, "【%s】字符串长度非法，字符串长度不能超过%d个字符长度！")
    DATA_TYPE_ERROR = (1008, "数据类型错误，请填写【%s】！")

    @property
    def code(self):
        return self.value[0]

    @property
    def msg(self):
        return self.value[1]

    def getMsg(self, code, *args):
        """
        占位提示内容替换
        :param code: 状态码
        :param args: 替换参数动态列表
        :return: 替换后的提示内容
        """
        values = [m.value for m in self]
        for value in values:
            if code == value[0] and len(args) > 0:
                # 将传递的参数动态替换提示信息占位内容
                ns = str(value[1]) % args
                return ns
            elif code == value[0]:
                return value[1]
