import json


def isList(params):
    """
    判读字符串是否是json数组类型
    :param params: 字符串
    :return: true-json数组，false-非json数组
    """
    b = False
    try:
        nj = json.loads(params)
        if type(nj) is list:
            b = True
    except Exception as e:
        raise e
    finally:
        return b
