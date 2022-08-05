#encoding = utf-8

"""
     @describe: Kmeans cluster
"""

import numpy as np
import math
import os

class KMean:

    def __init__(self):
        self.__cluster_center = None   # cluster center
        self.__SSE = 0.0         # sum of squared error

    def Train(self, sample, label, cls=3):
        """
        train model
        :param sample: sample dataset
        :param label: label of sample
        :param cls: cluster amount
        :return:
        """