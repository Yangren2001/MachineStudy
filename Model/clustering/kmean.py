#encoding = utf-8

"""
     @describe: Kmeans Model
"""

import numpy as np
import math
import os

from Model.Model import Model

class KMean(Model):

    def __init__(self):
        super(KMean, self).__init__()
        self.__cluster_center = None   # Model center
        self.__SSE = 0.0         # sum of squared error

    def model(self, sample, label, cluster_amount=3):
        """
        fit model
        :param sample: sample dataset
        :param label: label of sample
        :param cluster_amount: Model amount
        :return:
        """
        pass