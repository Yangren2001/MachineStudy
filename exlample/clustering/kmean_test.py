# encoding = utf-8

"""
    @describe: kmeans model test
"""
from Model.clustering.kmean import KMean

import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("../dataset/iris.csv")
    x = data.values[:, :-1]
    k = KMean()
    h = k.fit(x)
    print(h)