import json
from util import FileUtil
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


def delete(nid):
    """
    删除指定配置信息
    :param nid: 识别主键
    :return: true-删除成功，false-删除失败
    """
    delete_array = FileUtil.getCfg()
    if delete_array and len(delete_array) > 0:
        for o in delete_array:
            if o and len(o) > 0:
                # 根据识别主键匹配数据
                if o["nId"] == nid:
                    # 删除匹配数据
                    delete_array.remove(o)
                    # 重新保存新的配置数据
                    cl = json.dumps(delete_array)
                    b = FileUtil.writeCfg(cl)
                    return b

    return False


def invertData(nid):
    """
    反显数据
    :param nid: 识别主键
    :return: 反显数据
    """
    array = FileUtil.getCfg()
    if array and len(array) > 0:
        for o in array:
            if o and len(o) > 0:
                if o["nId"] == nid:
                    return o

    return None


def loadTaskList(taskList: QTableWidget):
    """
    加载任务列表UI显示
    :param taskList: 任务显示列表
    :return:
    """
    cfg = FileUtil.getCfg()
    if cfg and len(cfg) > 0:
        # 设置显示任务列表的行数
        taskList.setRowCount(len(cfg))
        row = 0
        for o in cfg:
            if o and len(o) > 0:
                # 表格第一列为任务名称，显示
                item = QTableWidgetItem(o["name"])
                taskList.setItem(row, 0, item)
                # 表格第二列为识别主键，不显示
                item = QTableWidgetItem(o["nId"])
                taskList.setItem(row, 1, item)
            row += 1
    else:
        taskList.setRowCount(0)
