# encoding = utf-8

"""
   @describe: 修饰器
"""
import numpy as np
import os
import config.modifier_conf as m_conf

def changename(f):
    """更改函数名"""
    cname = f.__name__

    def name(*arg, **kwargs):
        res = None
        if kwargs or arg:
            res = f(*arg, **kwargs)
        else:
            res = f()
        return res
    name.__name__ = cname
    return name

def isdata(data):
    """
    is type of data?
    :param sample:
    :param kwargs:
    :return:type
    """
    for t in m_conf.DATATYPE:
        if isinstance(data, t):
            return t
    return None

if __name__ == "__main__":
    print(isdata.__name__)