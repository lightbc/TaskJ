from entity.NewCreate import NewCreate
from enums.StatusCodeEnum import StatusCodeEnum
from util import OSUtil


def validParams(params: NewCreate):
    """
    新建保存参数校验
    :param params: 实体对象
    :return: 校验结果代码值
    """
    if not params:
        return StatusCodeEnum.GET_PARAMS_EXCEPTION.code
    if not params.name:  # 校验名称
        return StatusCodeEnum.NAME_EMPTY.code
    if not (0 < len(params.name) <= 12):  # 校验名称长度
        return StatusCodeEnum.STR_LEN_ILLEGAL.code
    if not params.runCmd:  # 校验命令行内容/文件选择内容
        return StatusCodeEnum.RUN_CMD_EMPTY.code
    if not params.runTime:  # 校验执行时间
        return StatusCodeEnum.RUN_TIME_EMPTY.code
    if params.opType == "循环" and not params.stopTime:  # 当执行类型为【循环】时，执行结束时间校验
        return StatusCodeEnum.STOP_TIME_EMPTY.code
    elif OSUtil.strToTimeStamp(params.stopTime) <= OSUtil.strToTimeStamp(params.runTime):  # 当执行类型为【循环】时，结束时间需要大于开始时间
        return StatusCodeEnum.STOP_TIME_LT_RUN_TIME.code
    if params.opType == "循环" and not params.cycleVal:  # 执行类型为【循环】时，执行周期校验
        return StatusCodeEnum.CYCLE_VALUE_EMPTY.code
    try:
        int(params.cycleVal)  # 执行周期数据类型校验
    except Exception:
        return StatusCodeEnum.DATA_TYPE_ERROR.code
    return StatusCodeEnum.OK.code
