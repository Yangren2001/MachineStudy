# encoding = utf-8

"""
    @describe: 全局功能
"""
import numpy as np

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

if __name__ == "__main__":
    t = isdata(np.array(1))
    print(t is np.ndarray)