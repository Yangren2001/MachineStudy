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
from config.data_conf import WRAPPER_UPDATES, WRAPPER_ASSIGNMENTS


class ModifierType:
    """
    修饰器元类
    """
    __this = None        # 单例模式
    res = None

    def __new__(cls, *args, **kwargs):
        cls.__this = super(ModifierType, cls).__new__(cls)
        try:
            fun = args[0]
        except IndexError:
            raise ValueError("没有发现参数*args")
        if IsFunction(fun) is not None:
            cls.__this.__init__(fun)
            return cls.__this.__call__()
        else:
            raise TypeError("被修饰对象类型错误")

    def __init__(self, fun):
        self.res = fun

    def __call__(self, *args, **kwargs):
        return self.__this

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
            f = ModifierType.temple
        for attr in WRAPPER_ASSIGNMENTS:
            try:
                value = getattr(fun, attr)
            except AttributeError:
                pass
            else:
                setattr(f, attr, value)
        for attr in WRAPPER_UPDATES:
            getattr(f, attr).update(getattr(fun, attr, {}))
        return f

    @staticmethod
    def createModifierClassFun(obj, fun, f=None, *args, **kwargs):
        """
            创建一个修饰器功能函数
            :param fun: 被修饰函数
            :param f: 修饰器功能函数
            :param args:
            :param kwargs:
            :return:
        """
        rf = ModifierType.createModifierFun(fun, f, *args, **kwargs)
        rf.modifier = obj
        return rf

class Logging(ModifierType):
    __msg: str
    __level: int
    __loglevel_index_dict: dict
    __this = None

    def __new__(cls, *args, **kwargs):
        return super(Logging, cls).__new__(cls, *args, **kwargs)

    def __init__(self, mth):
        """
        :param mth: class or function
        """
        super(Logging, self).__init__(mth)
        loglevel = ["debug","info","warning","error","critical"]
        self.__loglevel_index_dict = dict(zip(loglevel, [i for i in range(len(loglevel))]))
        self.__logging = logging.getLogger()  # init
        self.__logging.setLevel(logging.INFO)
        # self.__sh = logging.StreamHandler(stream=sys.stdout)
        # self.__sh.setLevel(logging.INFO)
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

    def recv(self, msg="", fm="", level="info", old_flag=True):
        """
        接收消息
        :param old_flag: 是否保留初始格式
        :param msg:
        :param fm: 输出格式, format + msg
        :param level:debug,info,warning,error,critical
        :return:
        """
        init_fm = "{} ".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        if not old_flag:
            init_fm = ""
        self.__level = self.__loglevel_index_dict[level]
        self.__msg = init_fm + fm + msg
        self.send(self.__msg)

    def send(self, msg):
        self.__msg_level_dict[self.__level](msg)

    def __call__(self, *args, **kwargs):
        def wrap(*arg, **kwargs):
            if IsFunction(self.res) is not None:
                pass
            else:
                raise TypeError("mth 参数错误")
            if kwargs or arg:
                return self.res(*arg, **kwargs)
            else:
                return self.res()
        return self.createModifierClassFun(self, self.res, wrap)


if __name__ == "__main__":
    @Logging
    def b(x):
        print(b.modifier.recv("aaaas"))
        print(x)
    x = b(12)
    print(b.__name__)
