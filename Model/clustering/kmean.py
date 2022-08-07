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

    def __init__(self, cluster_num, init_cluster_center=None):
        super(KMean, self).__init__()
        self.__cluster_center = []   # Model center
        self.__SSE = 0.0         # sum of squared error
        self.__cluster_num = cluster_num   # 聚类数
        self.__init_cluster_center = init_cluster_center
        if init_cluster_center is not None:
            self.__init_flag = False
        else:
            self.__init_flag = True

    def build(self, feature, label):
        """
        构建模型
        :param feature: 特征集
        :param label: 标签集
        :return:
        """
        if isdata(feature) is not np.ndarray:
            feature = np.array(feature)   # 转换为矩阵
        self.__feature_shape = feature.shape
        # 初始化模型，簇中心初始化
        self.init_cluster_center()
        # 构建模型逻辑
        self.model(feature, label, self.__cluster_num)

    def model(self, sample, label, cluster_amount=3):
        """
        model
        :param sample: sample dataset
        :param label: label of sample
        :param cluster_amount: Model amount
        :return:
        """
        pass

    def init_cluster_center(self):
        """
        初始化簇中心
        :return:
        """
        if self.__init_flag:
            self.__cluster_center = [np.random.random(self.__feature_shape) for i in range(self.__cluster_num)]
        else:
            pass

    def set_seed(self, num):
        """
        设置初始化种子
        :param num:
        :return:
        """
        np.random.seed(num)