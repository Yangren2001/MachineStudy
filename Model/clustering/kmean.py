#encoding = utf-8

"""
     @describe: Kmeans Model
"""

import numpy as np
import math
import os

from Model.Model import Model
from utils.utils import *

class KMean(Model):

    def __init__(self):
        super(KMean, self).__init__()
        self.__cluster_center = None   # Model center
        self.__SSE = 0.0         # sum of squared error

    def build(self, feature, label):
        """
        构建模型
        :param feature: 特征集
        :param label: 标签集
        :return:
        """
        if isdata(feature) is not np.ndarray:
            feature = np.array(feature)   # 转换为矩阵

    def model(self, sample, label, cluster_amount=3):
        """
        model
        :param sample: sample dataset
        :param label: label of sample
        :param cluster_amount: Model amount
        :return:
        """
        pass