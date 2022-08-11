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

from Utils.utils import *

class Logging:
    __msg: str
    __level: int
    __loglevel_index_dict: dict

    def __init__(self, mth):
        """

        :param mth: class or function
        """
        loglevel = ["debug","info","warning","error","critical"]
        self.__loglevel_index_dict = dict(zip(loglevel, [i for i in range(len(loglevel))]))
        self.__logging = logging.getLogger()  # init
        self.__logging.setLevel(logging.INFO)
        # self.__sh = logging.StreamHandler(stream=sys.stdout)
        # self.__sh.setLevel(logging.INFO)
        self.res = mth
        self.__msg = ""

    def setLogLevel(self, level:logging.INFO):
        """
        设置日志输出等级
        :param level: logging
        :return:
        """
        self.__logging.setLevel(level)

    @property
    def __msg_level_dict(self):
        return {
            0: logging.debug,
            1: logging.info,
            2: logging.warning,
            3: logging.error,
            4: logging.critical,
        }

    @__msg_level_dict.getter
    def msg_level_dict(self, value):
        return self.__msg_level_dict[value]


    def recv(self, msg="", level="info"):
        """
        接收消息
        :param msg:
        :param level:debug,info,warning,error,critical
        :return:
        """
        self.__level = self.__loglevel_index_dict[level]
        self.__msg = "{} ".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + msg
        self.send(self.__msg)

    def send(self, msg):
        self.__msg_level_dict[self.__level](msg)

    def __call__(self, *arg, **kwargs):
        if isinstance(self.res, type):   # 判断函数是类
            pass
        elif callable(self.res):
            pass
        else:
            raise TypeError("mth 参数错误")
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
    @Logging
    def b():
        b.recv("aaaaaa")
        print(1)
    b()
    # print(b.__name__)
