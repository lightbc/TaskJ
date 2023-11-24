import json
from PyQt5.QtWidgets import QMessageBox, QDialog
from util import FileUtil, SaveValidUtil, TaskListUtil
from entity.NewCreate import NewCreate
from enums.StatusCodeEnum import StatusCodeEnum


def save(params: NewCreate, parent: QDialog):
    """
    任务数据保存方法
    :param params: 任务数据实体
    :param parent: 父级UI组件
    :return:
    """
    if params:
        # 数据校验
        v = SaveValidUtil.validParams(params)
        if v == StatusCodeEnum.OK.code:
            # 先删除已存在的数据，然后重新插入保存数据
            TaskListUtil.delete(params.nId)
            lt = FileUtil.getCfg()
            # 向已保存的任务配置信息中追加新的配置信息
            lt.append(params.to_dict())
            cl = json.dumps(lt)
            b = FileUtil.writeCfg(cl)
            if b:
                QMessageBox.information(parent, "提示", "保存成功！")
            else:
                QMessageBox.warning(parent, "警告", "保存失败！")
            # 关闭父级对话框
            parent.close()
        else:
            # 显示未校验通过提示内容
            if v == StatusCodeEnum.STR_LEN_ILLEGAL.code:
                QMessageBox.warning(parent, "校验未通过", StatusCodeEnum.getMsg(StatusCodeEnum, v, "名称", 12))
            elif v == StatusCodeEnum.DATA_TYPE_ERROR.code:
                QMessageBox.warning(parent, "校验未通过", StatusCodeEnum.getMsg(StatusCodeEnum, v, "整数类型"))
            else:
                QMessageBox.warning(parent, "校验未通过", StatusCodeEnum.getMsg(StatusCodeEnum, v))
