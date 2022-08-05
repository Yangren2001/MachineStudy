# encoding = utf-8

"""
   @describe: 修饰器
"""
import numpy as np
import os


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
    print(2)
    return name

class Modifier:

    def __init__(self):
        self._data_type = [list, tuple, dict, int ]

    @changename
    def isdata(self, sample=None):
        """
        is type of data?
        :param sample:
        :param kwargs:
        :return:type
        """
        for t in self._data_type:
            if isinstance(sample, t):
                return t
        return None

if __name__ == "__main__":
    m = Modifier()
    print(m.isdata.__name__)