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

from copy import deepcopy

from Utils.utils import *


class ModifierType:
    """
    修饰器元类
    """
    __this = None        # 单例模式
    res = None

    def __new__(cls, *args, **kwargs):
        if cls.__this is None:
            cls.__this = super(ModifierType, cls).__new__(cls, *args, **kwargs)
        return cls.__this

    def __init__(self, fun):
        self.res = fun

    @staticmethod
    def temple(*args, **kwargs):
        """
        修饰器模板
        :param args:
        :param kwargs:
        :return:
        """
        if kwargs or args:
            return ModifierType.res(*args, **kwargs)
        else:
            return ModifierType.res()

    @staticmethod
    def setFun(fun):
        ModifierType.res = fun

    @staticmethod
    def createModifierFun(fun, f=None, *args, **kwargs):
        """
        创建一个修饰器功能函数
        :param fun: 被修饰函数
        :param f: 修饰器功能函数
        :param args:
        :param kwargs:
        :return:
        """
        assert callable(fun)
        if f is None:
            fun.__call__ = ModifierType.temple.__call__
        else:
            fun.__call__ = f.__call__
        return fun



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

    def __call__(self):
        def wrap(*arg, **kwargs):
            print(11)
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
        f = deepcopy(self.res)
        f.__call__ = wrap.__call__
        f()


if __name__ == "__main__":
    @Logging
    def b():
        print(b)
        print(1)
    x = b()
    print(x)
