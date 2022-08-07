# encoding = utf-8

"""
   @describe: 修饰器
"""
import numpy as np
import os
import logging
import tqdm
import sys
import time

def changename(f):
    """更改函数名"""
    cname = f.__name__
    c_doc = f.__doc__
    def name(*arg, **kwargs):
        res = None
        if kwargs or arg:
            res = f(*arg, **kwargs)
        else:
            res = f()
        return res
    name.__name__ = cname
    name.__doc__ = c_doc
    return name


class Logging:

    def __init__(self):
        self.__logging = logging.getLogger()  # init
        self.__logging.setLevel(logging.INFO)
        self.__sh = logging.StreamHandler(stream=sys.stdout)

    def __call__(self, fun):
        @changename
        def wrap(*arg, **kwargs):
            res = None
            if kwargs or arg:
                res = fun(*arg, **kwargs)
            else:
                res = fun()
            return res
        return wrap

if __name__ == "__main__":
    pass
