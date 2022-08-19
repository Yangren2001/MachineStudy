#encoding = utf-8

"""
     @describe: Kmeans Model
"""

import numpy as np
import math
import os
import tqdm as tq
import random

from Model.Model import Model
from Utils.utils import *
from Utils.modifier import Logging


class KMean(Model):
    def __new__(cls, *args, **kwargs):
        return super(KMean, cls).__new__(cls, *args, **kwargs)

    def __init__(self, cluster_num=3, init_cluster_center=None):
        super(KMean, self).__init__()
        self.__cluster_center = []   # Model center
        self.__SSE = 0.0         # sum of squared error
        self.__OLD_SSE = np.inf
        self.__cluster_num = cluster_num   # 聚类数
        self.__init_cluster_center = init_cluster_center
        self.__history = {}   # 记录损失和指标
        if init_cluster_center is not None:
            self.__init_flag = False
        else:
            self.__init_flag = True

    def build(self, feature, label):
        """
        构建模型
        :param label: 标签集
        :param feature: 特征集
        :return:
        """
        if isdata(feature) is not np.ndarray:
            feature = np.array(feature)   # 转换为矩阵
        if isdata(label) is not list:
            if isdata(label) is np.ndarray:
                label = label.tolist()
            else:
                label = list(label)
        self.__feature_shape = feature.shape
        # 构建模型逻辑
        self.model(feature, label, self.__cluster_num)

    @Logging
    def model(self, sample, label, cluster_amount=3):
        """
        model
        :param label: 标签集
        :param sample: sample dataset
        :param cluster_amount: Model amount
        :return:
        """
        # 初始化模型，簇中心初始化
        if self.__init_flag:
            self.init_cluster_center(sample)
        log_obj = self.model.modifier
        index_ = 1
        while True:
            labels = []  # 聚类标签集
            self.__SSE = 0.0
            for i in range(self.__feature_shape[0]):  # 遍历每一个样本
                min_dist = (np.inf, 0)  # (dist, label)
                for j in range(self.__cluster_num):  # 遍历簇中心
                    dist = self.loss(sample[i, :], self.__cluster_center[j])
                    if dist < min_dist[0]:
                        min_dist = (dist, j)
                labels.append(min_dist[1])
                self.__SSE += min_dist[0]

            log_obj.recv(msg="epoch {}:SSE: {}  ACC:{}".format(index_, self.__SSE, self.countAcc(label, labels)), fm="", old_flag=True, level="info")
            index_ += 1
            # 调整模型
            if self.__SSE >= self.__OLD_SSE:
                return
            else:
                self.__OLD_SSE = self.__SSE
                for i in range(self.__cluster_num):
                    m = sample[np.nonzero(np.array(labels) == i),:]
                    if m.size == 0:
                        continue
                    self.__cluster_center[i] = np.mean(m, axis=1)
            self.history = ("loss", [self.__SSE])
            self.history = ("labels", [labels])

    def checkClusterPoint(self, sample, num):
        """
        选取k个点
        :param sample: 样本
        :param num: 点数
        :return:
        """
        return [np.reshape(sample[random.randint(0, self.__feature_shape[0] - 1), :], (1, *self.__feature_shape[1:])) for i in range(num)]

    @property
    def history(self):
        return self.__history

    @history.setter
    def history(self, v):
        if not (isinstance(v, tuple) and isinstance(v[1], list)):
            raise TypeError("数据应该为(key, values(list))!")
        if self.__history.get(v[0]) is None:
            self.__history[v[0]] = v[1]
        else:
            self.__history[v[0]] += v[1]

    def countAcc(self,true_label, pre_label):
        """
        计算准确率
        :param true_label:
        :param pre_label:
        :return:
        """
        t_l = len(true_label)
        try:
            assert t_l == len(pre_label)
        except AssertionError:
            raise ValueError("样本标签与真实标签长度不一致{}和{}".format(t_l, len(pre_label)))
        s = 0
        for i in range(t_l):
            if true_label[i] == pre_label[i]:
                s += 1
        return s / t_l

    def init_cluster_center(self, data):
        """
        初始化簇中心
        :param data:
        :return:
        """
        if self.__init_flag:
            self.__cluster_center = self.checkClusterPoint(data, self.__cluster_num)
        else:
            pass

    def set_seed(self, num):
        """
        设置初始化种子
        :param num:
        :return:
        """
        random.seed(num)

    def loss(self, x1, x2):
        """
        计算损失函数
        :param x1:
        :param x2:
        :return: loss values
        """
        return np.sqrt(np.sum(np.square(np.subtract(x1, x2))))

    def fit(self, x, y):
        self.build(x, y)
        return self.__history

    def predict(self, x):
        """
        预测
        :param x:
        :return:
        """
        pass