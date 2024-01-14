import entity.NewCreate as n
import enums.StatusCodeEnum as s
import util.OSUtil as OSUtil

NewCreate = n.NewCreate
StatusCodeEnum = s.StatusCodeEnum


def validParams(params: NewCreate):
    """
    新建保存参数校验
    :param params: 实体对象
    :return: 校验结果代码值
    """
    if not params:
        return StatusCodeEnum.GET_PARAMS_EXCEPTION.code
    # 校验名称
    if not params.name:
        return StatusCodeEnum.NAME_EMPTY.code
    # 校验名称长度
    if not (0 < len(params.name) <= 12):
        return StatusCodeEnum.STR_LEN_ILLEGAL.code
    # 校验命令行内容/文件选择内容
    if not params.runCmd:
        return StatusCodeEnum.RUN_CMD_EMPTY.code
    # 校验执行时间
    if not params.runTime:
        return StatusCodeEnum.RUN_TIME_EMPTY.code
    # 当执行类型为【循环】时，执行结束时间校验
    if params.opType == "循环" and not params.stopTime:
        return StatusCodeEnum.STOP_TIME_EMPTY.code
    # 当执行类型为【循环】时，结束时间需要大于开始时间
    elif OSUtil.strToTimeStamp(params.stopTime) <= OSUtil.strToTimeStamp(params.runTime):
        return StatusCodeEnum.STOP_TIME_LT_RUN_TIME.code
    # 执行类型为【循环】时，执行周期校验
    if params.opType == "循环" and not params.cycleVal:
        return StatusCodeEnum.CYCLE_VALUE_EMPTY.code
    try:
        # 执行周期数据类型校验
        if params.cycleVal:
            int(params.cycleVal)
    except ValueError:
        return StatusCodeEnum.DATA_TYPE_ERROR.code
    return StatusCodeEnum.OK.code
