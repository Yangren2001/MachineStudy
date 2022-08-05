# encoding=utf-8

import math
import numpy as np

class Node:
    def __init__(self, feature=None, f=None, lnode=None, rnode=None, leaflabel=None):
        """
        树节点
        :param feature: 特征序号
        :param f: 特征值
        :param lnode: 左节点
        :param rnode: 右节点
        :param leaflabel: 叶子标签
        """
        self.feature = feature
        self.f = f
        self.lnode = lnode
        self.rnode = rnode
        self.leaflabel = leaflabel

class Cart:

    def __init__(self):
        pass

    def mean(self, sample):
        """
        计算均值
        :param sample: array
        :return: mean
        """
        return sample.mean

    def variance(self, sample):
        """
            计算样本方差
            :param sample: array
            :return: std
        """
        return sample.T.std

    def split(self, sample, feature, size):
        """
        某一特征下样本最佳划分
        :param sample: array
        :param feature: 特征序号
        :param size: 样本长度
        :return: lsample, rsample, min_res_variance_map
        """
        lsample = np.array([])
        rsample = np.array([])     # 左右样本
        min_res_variance_map = [-1, -1.0]   # 最小剩余方差 0:最小剩余方差
        test_sample = dict(zip([i for i in range(size[0])], sample[:, feature].T.tolist()))  # 样本特征值字典
        for j in range(size[1]):
            for i in test_sample.keys():     # 样本
                if sample[feature, i] >= test_sample[j]:
                    np.append(lsample, feature, axis=0)
                else:
                    np.append(rsample, feature, axis=0)
            if min_res_variance_map[1] < 0.0:
                min_res_variance_map = [test_sample[j], self.variance(lsample[:, j]) + self.variance(rsample[:, j])]
                continue
            min_res_variance = self.variance(lsample[:, j]) + self.variance(rsample[:, j])
            if min_res_variance < min_res_variance_map[1]:
                min_res_variance_map[1] = min_res_variance
                min_res_variance_map[0] = test_sample[j]          # 决策值

        return lsample, rsample, min_res_variance_map


    def build(self, sample, sam_limter=0.3):
        """
        建树
        :param sample: array
        :param sam_limter: 样本数量阈值
        :return: tree
        """
        split_varances = []       # 分割方差
        min_split_varance = None     # 最小分割方差
        size = sample.shape      # 样本大小
        for feature in range(size[1]):
            split_varances.append(self.split(sample, feature, size))    # 获取划分该特征最小方差
        min_split_varance = sorted(split_varances, key=lambda x: x[2][1])[0]



if __name__ == "__main__":
    pass