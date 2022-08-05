#encoding = utf-8

"""
     @describe: Model Class
"""

class Model:

    def __new__(cls, *args, **kwargs):

        return super(Model, cls).__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        pass

    def build(self, *args, **kwargs):
        pass

    def model(self, *args, **kwargs):
        pass

    def fit(self, *args, **kwargs):
        pass

    def predict(self, *args, **kwargs):
        pass

    def loss(self, *args, **kwargs):
        pass

    def test(self, *args, **kwargs):
        pass