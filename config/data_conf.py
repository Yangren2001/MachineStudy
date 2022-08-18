# enocoding = utf-8

"""
    @describe: 数据集参数
"""
import numpy as np

DATATYPE = [list, tuple, dict, np.ndarray]    # 支持的数据类型 elem： class
WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__doc__', '__qualname__',
                       '__annotations__')
WRAPPER_UPDATES = ('__dict__',)