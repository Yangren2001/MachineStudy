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
    return name

if __name__ == "__main__":
    pass