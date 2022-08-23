# encoding = utf-8

"""
    @describe: 全局功能
"""
import numpy as np
import tqdm
import config.data_conf as d_conf

def isdata(data):
    """
    is type of data?
    :param sample:
    :param kwargs:
    :return:type
    """
    t = type(data)
    if t in d_conf.DATATYPE:
        return t
    return None

def IsFunction(obj:object):
    """
    判断是否为函数
    :param obj:
    :return: false: 类
    """
    if isinstance(obj, type):  # 判断函数是类
        return False
    elif callable(obj):
        return True
    else:
        return None

def GetDictIndex(d: dict, values, flag=True):
    """
    获取值的字典索引
    :param d: 字典
    :param values:值
    :param flag:是否只返回一个
    :return:
    """
    index = []
    for kv in d.items():
        if values in kv:
            index.append(kv[0])
    if len(index) > 0:
        if flag:
            return index[0]
        else:
            return index
    raise ValueError("values '{}' not exists dict".format(values))


def AsArray(data):
    """
    如果数据不是一个数组，那么转化为数组
    :param data:
    :return:
    """
    try:
        if isdata(data) is not np.ndarray:
            return np.array(data)  # 转换为矩阵
        else:
            return data
    except Exception:
        return None



if __name__ == "__main__":
    t = isdata(np.array(1))
    print(t is np.ndarray)