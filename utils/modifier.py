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

class Logging:

    def __init__(self, fun):
        self.__logging = logging.getLogger()  # init
        self.__logging.setLevel(logging.INFO)
        self.__sh = logging.StreamHandler(stream=sys.stdout)
        self.res = fun

    def __call__(self,*arg, **kwargs):
        if kwargs or arg:
            return self.res(*arg, **kwargs)
        else:
            return self.res()

class Modifier:

    def __new__(cls, *args, **kwargs):
        return super(Modifier, cls).__new__(cls, *args, **kwargs)

    def __init__(self):
        pass

    @staticmethod
    def changename(fun):
        """更改函数名"""
        cname = fun.__name__
        c_doc = fun.__doc__
        def change(f):
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
        return change

    @staticmethod
    def changeFunName(f):
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

    @classmethod
    def abc(cls, a):
        print(cls, a)
        def r(res):
            print(res)
            @Modifier.changename(res)
            def wrap(*arg, **kwargs):
                if kwargs or arg:
                    return res(*arg, **kwargs)
                else:
                    return res()
            return wrap
        return r


if __name__ == "__main__":
    @Modifier.abc(Modifier)
    def b():
        print(1)
    b()
    print(b.__name__)
